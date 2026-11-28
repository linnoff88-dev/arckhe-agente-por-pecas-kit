# agente-por-pecas-kit

[![Agente por peças](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/agente-por-pecas-kit/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Este é o kit do curso grátis **Agente por peças**: um agente de IA pequeno, em Python puro, em que cada peça é um arquivo que você abre e lê. Serve para quem já usa o ChatGPT ou o Claude e quer ver por dentro como um agente recebe um pedido, faz a tarefa e confere o resultado. O cérebro é o Codex da sua assinatura do ChatGPT, sem chave de API (ou um modelo no seu computador, se você preferir). Para usar, você precisa de um terminal, do Python 3 e do Codex instalado; o curso ensina o resto, uma aula por vez.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://linnoff88-dev.github.io/agente-por-pecas-kit/guia/**
Curso grátis: **https://linnoff88-dev.github.io/agente-por-pecas-v73/**

🎬 Vídeo: https://www.youtube.com/watch?v=pWXLBVyJd1Y

O kit do curso **Agente por peças** (ARCKHé AI): um agente de IA montado peça por peça, onde cada peça é um arquivo.

```
CANAL ──pedido──▶ CAIXA ──é exato?──▶ RECEITA (sem cérebro)
(terminal, chat,    │ não
 Telegram, pasta)   ▼
                  CéREBRO (Codex) ──pede──▶ FERRAMENTAS
                    │   ▲ memória e regras
                    ▼
                  VERIFICADOR ──▶ sucesso · tentar de novo · cancelar
```

| Peça | Arquivo |
|---|---|
| Canal | `canal_terminal.py`, `canal_web.py` + `chat.html`, `canal_telegram.py`, `canal_pasta.py` |
| Caixa (a rotina) | `caixa.py` |
| Cérebro | `cerebro.py` (Codex da assinatura) · `cerebro_local.py` (Ollama, módulo à parte: `CEREBRO=local`) |
| Receitas (RPA) | `receitas.py` + `receitas/*.txt` |
| Ferramentas | `ferramentas.py` |
| Memória | `memoria.json` (nasce quando o agente lembra a primeira coisa) |
| Regras | `regras.md` + as travas dentro de `ferramentas.py` |
| Verificador e loop | `verificador.py` + o laço em `caixa.py` |

Cada aula do curso é uma tag: `git checkout aula2` … `git checkout aula8`.

## O processo, do início ao fim

1. 🧠 Instalar o Codex e entrar com a assinatura: `npm i -g @openai/codex && codex login`.
2. 🧠 Baixar o kit: `git clone https://github.com/linnoff88-dev/agente-por-pecas-kit && cd agente-por-pecas-kit`.
3. ⚙️ Aula 2 (caixa e cérebro): `git checkout aula2 && python3 canal_terminal.py "seu pedido"`.
4. ⚙️ Aula 3 (chat): `git checkout aula3 && python3 canal_web.py` e abrir o endereço que aparece.
5. 🧠 Aula 4 (Telegram): criar o bot no @BotFather, gravar `TELEGRAM_TOKEN=...` no `.env`, `python3 canal_telegram.py`.
6. ⚙️ Aula 5 (pasta): `git checkout aula5 && python3 canal_pasta.py` e deixar arquivos `.txt` em `entrada/`.
7. ⚙️ Aula 6 (receitas e ferramentas): `git checkout aula6`, pedidos exatos vão para `receitas/`.
8. ⚙️ Aula 7 (memória e regras): `git checkout aula7`; no Telegram, `TELEGRAM_DONO=<seu chat>` no `.env`.
9. ⚙️ Aula 8 (verificador e loop): `git checkout aula8 && python3 canal_terminal.py "pedido" --esperado "o que tem de aparecer"`.
10. ⚙️ Testes sem modelo: `python3 -m pytest -q testes/`.

O token do bot fica só no `.env` (fora do git). O Codex roda numa pasta vazia, em modo só leitura: quem mexe em arquivo é a caixa, pelas ferramentas.
