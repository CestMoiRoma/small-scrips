# 🐍 Small Scripts

A growing collection of Python scripts I write whenever I need a quick tool.
Nothing fancy — each script solves one problem and does it well.
I'm sharing them as a loose library in case they're useful to anyone else.

---

## 📦 Scripts

| Folder | Description |
|--------|-------------|
| [`token-calculator/`](token-calculator/) | Count tokens in a Markdown file and estimate API costs |
| [`apple-tts2mp3/`](apple-tts2mp3/) | Convert text to MP3 using the macOS `say` command |
| [`get-macos-pos/`](get-macos-pos/) | Get your Mac's GPS coordinates and reverse-geocode them offline |
| [`ollama-bulk-pull/`](ollama-bulk-pull/) | Bulk-download Ollama models with a live progress bar |

Each folder contains the script, a `requirements.txt`, and its own `wiki.md`.

```
token-calculator/
├── token_calculator.py
├── requirements.txt
└── wiki.md

apple-tts2mp3/
├── apple-TTS2MP3.py
├── requirements.txt
└── wiki.md

get-macos-pos/
├── Get-MacOS-Pos.py
├── requirements.txt
└── wiki.md

ollama-bulk-pull/
├── ollama_bulk_pull.py
├── requirements.txt
└── wiki.md
```

---

## 📖 Wiki

Each script has a `wiki.md` in its folder. The [`wiki/`](wiki/) folder contains an [index](wiki/index.md) that links to all of them.

| Script | Docs |
|--------|------|
| Token Calculator | [wiki.md](token-calculator/wiki.md) |
| Apple TTS → MP3 | [wiki.md](apple-tts2mp3/wiki.md) |
| Get macOS Position | [wiki.md](get-macos-pos/wiki.md) |
| Ollama Bulk Pull | [wiki.md](ollama-bulk-pull/wiki.md) |

---

## 🚀 Quick start

```bash
cd <script-folder>
pip install -r requirements.txt
python3 <script>.py --help
```

---

## 🤝 Contributing

Want to add a script? Just open a PR!

**1. Script**
- One script = one problem, keep it focused
- Put everything in its own folder: `your-script/your_script.py` + `requirements.txt`
- Must have a `--help` flag or a module docstring explaining usage
- If your script needs environment variables, add a `.env.example` with each variable listed and a short comment explaining what it's for. Never commit a real `.env`.

**2. Wiki**
- Add a `wiki.md` inside your script folder (see any existing one as a template)
- It should cover: what the script does, requirements, all flags with a table, usage examples, and a brief "how it works" section
- Add a row for your script to [`wiki/index.md`](wiki/index.md)

**3. README**
- Add a row to the Scripts table at the top of this file
- Add a row to the Wiki table

That's it. No tests required, no framework needed.
