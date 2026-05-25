#!/usr/bin/env python3
"""
Ollama Bulk Puller — download multiple models in one shot.

Usage:
    python3 ollama_bulk_pull.py llama3.2 mistral gemma3          # pass models as args
    python3 ollama_bulk_pull.py --file models.txt                 # read from a text file
    python3 ollama_bulk_pull.py --file models.txt llama3.2        # both at once
    python3 ollama_bulk_pull.py --list                            # show already-installed models

models.txt format — one model per line, # comments and blank lines ignored:
    llama3.2
    mistral:7b
    # codellama  ← skipped
    gemma3:12b
"""

import sys
import time
from pathlib import Path

import ollama

# ── ANSI helpers ──────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
DIM    = "\033[2m"
RESET  = "\033[0m"
CLEAR  = "\033[2K\r"

def bar(done: int, total: int, width: int = 30) -> str:
    if total <= 0:
        return " " * width
    filled = int(width * done / total)
    return "█" * filled + "░" * (width - filled)

def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"

# ── Core logic ────────────────────────────────────────────────────────────────

def list_installed() -> None:
    models = ollama.list().models
    if not models:
        print("No models installed yet.")
        return
    print(f"\n  {'Model':<35} {'Size':>10}  Modified")
    print(f"  {'─'*35}  {'─'*10}  {'─'*20}")
    for m in sorted(models, key=lambda x: x.model):
        size = human(m.size) if m.size else "—"
        mod  = m.modified_at.strftime("%Y-%m-%d %H:%M") if m.modified_at else "—"
        print(f"  {m.model:<35} {size:>10}  {mod}")
    print()


def pull_model(name: str) -> bool:
    """Pull one model, streaming progress. Returns True on success."""
    print(f"\n  {CYAN}↓ Pulling {name}{RESET}")
    try:
        last_status = ""
        for chunk in ollama.pull(name, stream=True):
            status    = chunk.get("status") or ""
            completed = chunk.get("completed") or 0
            total     = chunk.get("total") or 0

            if total:
                pct  = completed / total * 100
                b    = bar(completed, total)
                line = (f"  {b} {pct:5.1f}%  "
                        f"{human(completed):>10} / {human(total):<10}  "
                        f"{DIM}{status}{RESET}")
            else:
                line = f"  {DIM}{status}{RESET}"

            if status != last_status or total:
                print(f"{CLEAR}{line}", end="", flush=True)
                last_status = status

        print(f"{CLEAR}  {GREEN}✔  {name} — done{RESET}")
        return True

    except ollama.ResponseError as e:
        print(f"{CLEAR}  {RED}✘  {name} — {e.error}{RESET}")
        return False
    except Exception as e:
        print(f"{CLEAR}  {RED}✘  {name} — {e}{RESET}")
        return False


def load_file(path: Path) -> list[str]:
    models = []
    for raw in path.read_text().splitlines():
        line = raw.split("#")[0].strip()
        if line:
            models.append(line)
    return models


def main() -> None:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    if "--list" in args:
        list_installed()
        sys.exit(0)

    models: list[str] = []

    # --file <path>
    if "--file" in args:
        idx = args.index("--file")
        try:
            file_path = Path(args[idx + 1])
        except IndexError:
            print(f"{RED}--file requires a path argument{RESET}")
            sys.exit(1)
        if not file_path.exists():
            print(f"{RED}File not found: {file_path}{RESET}")
            sys.exit(1)
        models += load_file(file_path)
        args = args[:idx] + args[idx + 2:]   # remove --file <path> from remaining

    # remaining positional args are model names
    models += [a for a in args if not a.startswith("--")]

    if not models:
        print(f"{YELLOW}No models specified. Pass names as args or use --file.{RESET}")
        sys.exit(1)

    # deduplicate while preserving order
    seen: set[str] = set()
    unique = [m for m in models if not (m in seen or seen.add(m))]

    print(f"\n  {CYAN}Ollama Bulk Pull — {len(unique)} model(s){RESET}")
    print(f"  {'─'*46}")
    for m in unique:
        print(f"  • {m}")

    t_start = time.time()
    results = {m: pull_model(m) for m in unique}
    elapsed = time.time() - t_start

    # ── Summary ───────────────────────────────────────────────────────────────
    ok   = [m for m, s in results.items() if s]
    fail = [m for m, s in results.items() if not s]

    print(f"\n  {'─'*46}")
    print(f"  Done in {elapsed:.1f}s  —  "
          f"{GREEN}{len(ok)} succeeded{RESET}  "
          f"{(RED + str(len(fail)) + ' failed' + RESET) if fail else ''}")

    if fail:
        print(f"\n  {RED}Failed:{RESET}")
        for m in fail:
            print(f"    ✘ {m}")
        print()
        sys.exit(1)
    print()


if __name__ == "__main__":
    main()
