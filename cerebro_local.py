"""O CéREBRO LOCAL (módulo à parte): o mesmo papel do cerebro.py, com um modelo no seu computador (Ollama).
Use com CEREBRO=local. Precisa do Ollama instalado e do modelo baixado (ollama pull llama3.2)."""
import json, os, urllib.request

MODELO = os.environ.get("MODELO_LOCAL", "llama3.2")
URL = os.environ.get("OLLAMA_URL", "http://localhost:11434") + "/api/chat"


def pensar(mensagens, ferramentas=None, modelo=None):
    corpo = {"model": modelo or MODELO, "messages": mensagens, "stream": False, "think": False,
             "options": {"temperature": 0, "seed": 1}}
    if ferramentas:
        corpo["tools"] = ferramentas
    pedido = urllib.request.Request(URL, json.dumps(corpo).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(pedido, timeout=600) as r:
        return json.loads(r.read())["message"]
