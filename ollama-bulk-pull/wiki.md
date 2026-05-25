# Ollama Bulk Pull

**File:** [`ollama_bulk_pull.py`](ollama_bulk_pull.py)

Downloads multiple Ollama models in one command, with a live progress bar for each. Useful when setting up a new machine or grabbing a batch of models you know you'll need.

---

## Requirements

- [Ollama](https://ollama.com) installed and running (`ollama serve`)
- Python package:
  ```bash
  pip install ollama
  ```

---

## Usage

```bash
python3 ollama_bulk_pull.py <model> [model ...]     # pass models directly
python3 ollama_bulk_pull.py --file models.txt       # read from a file
python3 ollama_bulk_pull.py --list                  # show installed models
```

### Flags

| Flag | Description |
|------|-------------|
| `<model> ...` | One or more model names as positional arguments. |
| `--file <path>` | Path to a text file with one model per line. Can be combined with positional args. |
| `--list` | Print all locally installed models with their size and last-modified date, then exit. |

---

## Examples

**Download a few models directly:**
```bash
python3 ollama_bulk_pull.py llama3.2 mistral gemma3:12b
```

**From a file:**
```bash
python3 ollama_bulk_pull.py --file models.txt
```

**Mix file + extra model:**
```bash
python3 ollama_bulk_pull.py --file models.txt codellama:13b
```

**See what's already installed:**
```bash
python3 ollama_bulk_pull.py --list
```
```
  Model                                     Size  Modified
  ───────────────────────────────────  ──────────  ────────────────────
  gemma4:31b                             18.5 GB  2026-05-19 13:41
  mistral-nemo:latest                     6.6 GB  2026-05-23 16:21
```

---

## models.txt format

One model name per line. Lines starting with `#` (after trimming) are treated as comments and skipped. Blank lines are ignored.

```
llama3.2
mistral:7b
# codellama  ← this line is skipped
gemma3:27b
```

---

## How it works

- Uses the [`ollama` Python library](https://github.com/ollama/ollama-python) which communicates with the local Ollama daemon over HTTP (`localhost:11434`).
- Each model is pulled sequentially (not in parallel) to avoid saturating your disk or connection.
- The progress display streams `completed` / `total` byte counts from the Ollama API and renders a live `█░░░` bar in-place using ANSI escape codes.
- Duplicate model names are silently deduplicated while preserving order.
- A summary at the end lists elapsed time, how many succeeded, and any that failed.

---

## Notes

- Model names follow Ollama's naming convention: `name` or `name:tag` (e.g. `llama3.2`, `mistral:7b`). Check [ollama.com/library](https://ollama.com/library) for available models and tags.
- If a model name doesn't exist in the Ollama registry, the pull will fail with a clear error and the script will continue with the next model.
- The Ollama daemon must be running before you start. Launch it with `ollama serve` or by opening the Ollama desktop app.
