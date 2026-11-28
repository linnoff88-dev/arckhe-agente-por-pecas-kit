"""O CéREBRO: leva a conversa ao modelo e devolve o que ele decidiu.
Padrão: o Codex da sua assinatura do ChatGPT (comando `codex exec`), sem chave de API.
Para rodar 100% local com o Ollama: CEREBRO=local (o módulo à parte é o cerebro_local.py)."""
import json, os, subprocess, tempfile

if os.environ.get("CEREBRO") == "local":
    from cerebro_local import MODELO, pensar        # noqa: F401  (a mesma peça, outro cérebro)
else:
    MODELO = os.environ.get("MODELO", "gpt-6-luna")

    PROTOCOLO = ("Você é o cérebro de um agente. Você não executa nada: só decide o próximo passo.\n"
                 "Ferramentas que a caixa sabe executar:\n{cardapio}\n"
                 "Responda SOMENTE com um JSON numa linha, sem mais nada:\n"
                 '{{"ferramenta": "<nome>", "args": {{...}}}}  para a caixa executar uma ferramenta, ou\n'
                 '{{"resposta": "<texto>"}}  para responder ao dono.')

    def conversa(mensagens):
        quem = {"system": "INSTRUçÕES", "user": "DONO", "assistant": "VOCê", "tool": "A FERRAMENTA DEVOLVEU"}
        linhas = []
        for m in mensagens:
            texto = m.get("content") or json.dumps(m.get("tool_calls"), ensure_ascii=False)
            linhas.append(f"### {quem[m['role']]}\n{texto}")
        return "\n\n".join(linhas)

    def pensar(mensagens, ferramentas=None, modelo=None):
        prompt = conversa(mensagens)
        if ferramentas:
            cardapio = "\n".join(f"- {f['function']['name']}{list(f['function']['parameters']['properties'])}: "
                                 f"{f['function']['description']}" for f in ferramentas)
            prompt = PROTOCOLO.format(cardapio=cardapio) + "\n\n" + prompt
        with tempfile.TemporaryDirectory() as vazio:           # o Codex roda numa pasta vazia, sem mexer em nada
            saida = os.path.join(vazio, "resposta.txt")
            ambiente = {k: v for k, v in os.environ.items() if k != "OPENAI_API_KEY"}   # só a assinatura
            r = subprocess.run(["codex", "exec", "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only",
                            "--ignore-rules", "-m", modelo or MODELO, "-o", saida, "-"],
                           input=prompt, text=True, cwd=vazio, env=ambiente, capture_output=True, timeout=300)
            texto = open(saida).read().strip() if os.path.exists(saida) else ""
        if not texto:                                       # diz o motivo: login, modelo fora da assinatura, rede
            erro = (r.stderr.strip().splitlines() or ["sem detalhe"])[-1][:200]
            raise SystemExit(f"o Codex não respondeu: {erro}\n(confira: codex login status, e o nome do modelo em MODELO)")
        if not ferramentas:
            return {"role": "assistant", "content": texto}
        try:
            decisao = json.loads(texto[texto.index("{"):texto.rindex("}") + 1])
        except ValueError:
            return {"role": "assistant", "content": texto}  # respondeu sem JSON: vale como resposta
        if "ferramenta" in decisao:
            return {"role": "assistant", "content": "",
                    "tool_calls": [{"function": {"name": decisao["ferramenta"], "arguments": decisao.get("args", {})}}]}
        return {"role": "assistant", "content": decisao.get("resposta", texto)}
