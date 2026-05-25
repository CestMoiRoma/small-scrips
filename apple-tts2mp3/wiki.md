# Apple TTS → MP3

**File:** [`apple-TTS2MP3.py`](apple-TTS2MP3.py)

Converts any text to an MP3 file using macOS's built-in `say` command as the speech engine. No cloud, no API keys — everything runs locally using Apple's on-device voices.

---

## Requirements

- **macOS only** (uses the `say` command)
- [ffmpeg](https://ffmpeg.org/) for the AIFF → MP3 conversion step:
  ```bash
  brew install ffmpeg
  ```

---

## Usage

```bash
python3 apple-TTS2MP3.py <text> [options]
python3 apple-TTS2MP3.py -              # read text from stdin
```

### Arguments & flags

| Argument | Default | Description |
|----------|---------|-------------|
| `text` | _(required)_ | The text to synthesize. Use `-` to read from stdin. |
| `-r`, `--rate` | `175` | Speech rate in words per minute. |
| `-v`, `--voice` | system default | Apple voice to use (e.g. `Samantha`, `Daniel`, `Thomas`). |
| `-o`, `--output` | `output.mp3` | Output file path. The `.mp3` extension is added automatically if missing. |
| `--list-voices` | — | Print all installed voices and exit. |

---

## Examples

**Basic synthesis:**
```bash
python3 apple-TTS2MP3.py "Hello, world!"
# → output.mp3
```

**Custom voice and speed:**
```bash
python3 apple-TTS2MP3.py "Welcome back." -v Samantha -r 200 -o welcome.mp3
```

**Slower narration voice:**
```bash
python3 apple-TTS2MP3.py "Chapter one." -v Daniel -r 140 -o chapter1.mp3
```

**Read from a file via stdin:**
```bash
cat my-script.txt | python3 apple-TTS2MP3.py -
```

**See available voices:**
```bash
python3 apple-TTS2MP3.py --list-voices
```

---

## How it works

1. **`say` → AIFF** — macOS's `say` command synthesizes the text and writes a lossless AIFF audio file to a temp location.
2. **AIFF → MP3** — ffmpeg converts the AIFF to MP3 using the `libmp3lame` encoder at VBR quality 2 (~190 kbps). The temp AIFF is deleted afterwards.

The two-step process is necessary because `say` can only export AIFF natively; ffmpeg handles the final compression.

---

## Notes

- Available voices depend on what's installed on your Mac. Go to **System Settings → Accessibility → Spoken Content → System Voice → Manage Voices** to install more.
- Rate `175` wpm is roughly natural conversational speed. `120–140` is good for clear narration, `220+` for faster listening.
