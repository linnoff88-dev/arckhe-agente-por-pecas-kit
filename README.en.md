# agente-por-pecas-kit

[![Agent by pieces](guia/assets/banner-en.jpg)](https://linnoff88-dev.github.io/agente-por-pecas-kit/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

This is the kit for the free course **Agent by pieces**: a small AI agent in plain Python, where each piece is a file you open and read. It is for people who already use ChatGPT or Claude and want to see from the inside how an agent takes a request, does the task and checks the result. The brain is the Codex from your ChatGPT subscription, with no API key (or a model on your own computer, if you prefer). To use it, you need a terminal, Python 3 and Codex installed; the course teaches the rest, one lesson at a time.

## 📖 User guide

Full guide (landing + step by step): **https://linnoff88-dev.github.io/agente-por-pecas-kit/guia/en/**
Free course (in Portuguese): **https://linnoff88-dev.github.io/agente-por-pecas-v73/**

🎬 Video (in Portuguese): https://www.youtube.com/watch?v=pWXLBVyJd1Y

The kit for the course **Agent by pieces** (ARCKHé AI): an AI agent built piece by piece, where each piece is a file.

```
CHANNEL ──request──▶ BOX ──exact?──▶ RECIPE (no brain)
(terminal, chat,      │ no
 Telegram, folder)    ▼
                    BRAIN (Codex) ──asks──▶ TOOLS
                      │   ▲ memory and rules
                      ▼
                    CHECKER ──▶ success · try again · cancel
```

| Piece | File |
|---|---|
| Channel | `canal_terminal.py`, `canal_web.py` + `chat.html`, `canal_telegram.py`, `canal_pasta.py` |
| Box (the routine) | `caixa.py` |
| Brain | `cerebro.py` (Codex from the subscription) · `cerebro_local.py` (Ollama, separate module: `CEREBRO=local`) |
| Recipes (RPA) | `receitas.py` + `receitas/*.txt` |
| Tools | `ferramentas.py` |
| Memory | `memoria.json` (created when the agent remembers its first thing) |
| Rules | `regras.md` + the locks inside `ferramentas.py` |
| Checker and loop | `verificador.py` + the loop in `caixa.py` |

Each lesson of the course is a tag: `git checkout aula2` … `git checkout aula8`.

## The process, from start to finish

1. 🧠 Install Codex and log in with the subscription: `npm i -g @openai/codex && codex login`.
2. 🧠 Download the kit: `git clone https://github.com/linnoff88-dev/agente-por-pecas-kit && cd agente-por-pecas-kit`.
3. ⚙️ Lesson 2 (box and brain): `git checkout aula2 && python3 canal_terminal.py "your request"`.
4. ⚙️ Lesson 3 (chat): `git checkout aula3 && python3 canal_web.py` and open the address it shows.
5. 🧠 Lesson 4 (Telegram): create the bot with @BotFather, save `TELEGRAM_TOKEN=...` in `.env`, `python3 canal_telegram.py`.
6. ⚙️ Lesson 5 (folder): `git checkout aula5 && python3 canal_pasta.py` and drop `.txt` files into `entrada/`.
7. ⚙️ Lesson 6 (recipes and tools): `git checkout aula6`, exact requests go to `receitas/`.
8. ⚙️ Lesson 7 (memory and rules): `git checkout aula7`; on Telegram, `TELEGRAM_DONO=<your chat>` in `.env`.
9. ⚙️ Lesson 8 (checker and loop): `git checkout aula8 && python3 canal_terminal.py "request" --esperado "what has to show up"`.
10. ⚙️ Tests with no model: `python3 -m pytest -q testes/`.

The bot token lives only in `.env` (outside git). Codex runs in an empty folder, in read-only mode: the box is what touches files, through the tools.
