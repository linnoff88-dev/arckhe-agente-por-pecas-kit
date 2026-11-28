# agente-por-pecas-kit

[![Agente por piezas](guia/assets/banner-es.jpg)](https://linnoff88-dev.github.io/agente-por-pecas-kit/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Este es el kit del curso gratuito **Agente por piezas** (en portugués): un agente de IA pequeño, en Python puro, en el que cada pieza es un archivo que abres y lees. Sirve para quien ya usa ChatGPT o Claude y quiere ver por dentro cómo un agente recibe un pedido, hace la tarea y comprueba el resultado. El cerebro es el Codex de tu suscripción de ChatGPT, sin clave de API (o un modelo en tu computadora, si lo prefieres). Para usarlo necesitas una terminal, Python 3 y el Codex instalado; el curso enseña el resto, una clase a la vez.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://linnoff88-dev.github.io/agente-por-pecas-kit/guia/es/**
Curso gratuito (en portugués): **https://linnoff88-dev.github.io/agente-por-pecas-v73/**

🎬 Video (en portugués): https://www.youtube.com/watch?v=pWXLBVyJd1Y

El kit del curso **Agente por piezas** (ARCKHé AI): un agente de IA armado pieza por pieza, donde cada pieza es un archivo.

```
CANAL ──pedido──▶ CAJA ──¿es exacto?──▶ RECETA (sin cerebro)
(terminal, chat,    │ no
 Telegram, carpeta) ▼
                  CEREBRO (Codex) ──pide──▶ HERRAMIENTAS
                    │   ▲ memoria y reglas
                    ▼
                  VERIFICADOR ──▶ éxito · intentar de nuevo · cancelar
```

| Pieza | Archivo |
|---|---|
| Canal | `canal_terminal.py`, `canal_web.py` + `chat.html`, `canal_telegram.py`, `canal_pasta.py` |
| Caja (la rutina) | `caixa.py` |
| Cerebro | `cerebro.py` (Codex de la suscripción) · `cerebro_local.py` (Ollama, módulo aparte: `CEREBRO=local`) |
| Recetas (RPA) | `receitas.py` + `receitas/*.txt` |
| Herramientas | `ferramentas.py` |
| Memoria | `memoria.json` (nace cuando el agente recuerda la primera cosa) |
| Reglas | `regras.md` + los bloqueos dentro de `ferramentas.py` |
| Verificador y bucle | `verificador.py` + el bucle en `caixa.py` |

Cada clase del curso es un tag: `git checkout aula2` … `git checkout aula8`.

## El proceso, de principio a fin

1. 🧠 Instalar el Codex e iniciar sesión con la suscripción: `npm i -g @openai/codex && codex login`.
2. 🧠 Descargar el kit: `git clone https://github.com/linnoff88-dev/agente-por-pecas-kit && cd agente-por-pecas-kit`.
3. ⚙️ Clase 2 (caja y cerebro): `git checkout aula2 && python3 canal_terminal.py "tu pedido"`.
4. ⚙️ Clase 3 (chat): `git checkout aula3 && python3 canal_web.py` y abrir la dirección que aparece.
5. 🧠 Clase 4 (Telegram): crear el bot en @BotFather, guardar `TELEGRAM_TOKEN=...` en el `.env`, `python3 canal_telegram.py`.
6. ⚙️ Clase 5 (carpeta): `git checkout aula5 && python3 canal_pasta.py` y dejar archivos `.txt` en `entrada/`.
7. ⚙️ Clase 6 (recetas y herramientas): `git checkout aula6`, los pedidos exactos van a `receitas/` (las recetas del kit están en portugués).
8. ⚙️ Clase 7 (memoria y reglas): `git checkout aula7`; en Telegram, `TELEGRAM_DONO=<tu chat>` en el `.env`.
9. ⚙️ Clase 8 (verificador y bucle): `git checkout aula8 && python3 canal_terminal.py "pedido" --esperado "lo que tiene que aparecer"`.
10. ⚙️ Pruebas sin modelo: `python3 -m pytest -q testes/`.

El token del bot queda solo en el `.env` (fuera de git). El Codex se ejecuta en una carpeta vacía, en modo solo lectura: quien toca los archivos es la caja, mediante las herramientas.
