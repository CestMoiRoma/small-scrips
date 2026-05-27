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

---

## 📝 Small Doc

Quick references — no fluff, straight to the point.
All pages live in [`small-doc/`](small-doc/) — see the [index](small-doc/index.md) for the full list.

**Windows CMD**

| Topic | Page |
|-------|------|
| CMD Cheat Sheet | [cmd-cheatsheet.md](small-doc/windows-cmd/cmd-cheatsheet.md) |
| CMD Basics | [cmd-basics.md](small-doc/windows-cmd/cmd-basics.md) |
| CMD Advanced | [cmd-advanced.md](small-doc/windows-cmd/cmd-advanced.md) |
| CMD Flags Reference | [cmd-flags.md](small-doc/windows-cmd/cmd-flags.md) |

**PowerShell**

| Topic | Page |
|-------|------|
| PowerShell Cheat Sheet | [powershell-cheatsheet.md](small-doc/powershell/powershell-cheatsheet.md) |
| PowerShell Basics | [powershell-basics.md](small-doc/powershell/powershell-basics.md) |
| PowerShell Advanced | [powershell-advanced.md](small-doc/powershell/powershell-advanced.md) |
| PowerShell Flags Reference | [powershell-flags.md](small-doc/powershell/powershell-flags.md) |

**Chocolatey**

| Topic | Page |
|-------|------|
| Chocolatey Cheat Sheet | [chocolatey-cheatsheet.md](small-doc/chocolatey/chocolatey-cheatsheet.md) |
| Chocolatey Basics | [chocolatey-basics.md](small-doc/chocolatey/chocolatey-basics.md) |
| Chocolatey Advanced | [chocolatey-advanced.md](small-doc/chocolatey/chocolatey-advanced.md) |
| Chocolatey Flags Reference | [chocolatey-flags.md](small-doc/chocolatey/chocolatey-flags.md) |

**Homebrew**

| Topic | Page |
|-------|------|
| Homebrew Cheat Sheet | [homebrew-cheatsheet.md](small-doc/homebrew/homebrew-cheatsheet.md) |
| Homebrew Basics | [homebrew-basics.md](small-doc/homebrew/homebrew-basics.md) |
| Homebrew Advanced | [homebrew-advanced.md](small-doc/homebrew/homebrew-advanced.md) |
| Homebrew Flags Reference | [homebrew-flags.md](small-doc/homebrew/homebrew-flags.md) |

**Python & pip**

| Topic | Page |
|-------|------|
| Python Cheat Sheet | [python-cheatsheet.md](small-doc/python/python-cheatsheet.md) |
| Python Basics | [python-basics.md](small-doc/python/python-basics.md) |
| Python Advanced | [python-advanced.md](small-doc/python/python-advanced.md) |
| Python & pip Flags | [python-flags.md](small-doc/python/python-flags.md) |

**Docker**

| Topic | Page |
|-------|------|
| Docker Cheat Sheet | [docker-cheatsheet.md](small-doc/docker/docker-cheatsheet.md) |
| Docker Basics | [docker-basics.md](small-doc/docker/docker-basics.md) |
| Docker Advanced | [docker-advanced.md](small-doc/docker/docker-advanced.md) |
| Docker Flags Reference | [docker-flags.md](small-doc/docker/docker-flags.md) |

**Linux**

| Topic | Page |
|-------|------|
| Linux Cheat Sheet | [linux-cheatsheet.md](small-doc/linux/linux-cheatsheet.md) |
| Linux Basics | [linux-basics.md](small-doc/linux/linux-basics.md) |
| Linux Advanced | [linux-advanced.md](small-doc/linux/linux-advanced.md) |
| Linux Flags Reference | [linux-flags.md](small-doc/linux/linux-flags.md) |

**Git**

| Topic | Page |
|-------|------|
| Git Cheat Sheet | [git-cheatsheet.md](small-doc/git/git-cheatsheet.md) |
| Git Basics | [git-basics.md](small-doc/git/git-basics.md) |
| Git Advanced | [git-advanced.md](small-doc/git/git-advanced.md) |
| Git Flags Reference | [git-flags.md](small-doc/git/git-flags.md) |

**Conventional Commits**

| Topic | Page |
|-------|------|
| Conventional Commits Cheat Sheet | [conventional-commits-cheatsheet.md](small-doc/conventional-commits/conventional-commits-cheatsheet.md) |
| Conventional Commits | [conventional-commits.md](small-doc/conventional-commits/conventional-commits.md) |
