#!/usr/bin/env python3
"""
Token Calculator — counts tokens in a Markdown file.

Usage:
    python token_calculator.py <file.md>
    python token_calculator.py <file.md> --sections      # breakdown by heading
    python token_calculator.py <file.md> --anthropic     # exact count via Claude API
"""

import sys
import re
from pathlib import Path

# ── Cost table (USD per 1M input tokens, as of 2025) ─────────────────────────
MODELS = [
    ("Claude Haiku 4.5",   0.80),
    ("Claude Sonnet 4.6",  3.00),
    ("Claude Opus 4.7",   15.00),
    ("GPT-4o",             2.50),
    ("GPT-4o mini",        0.15),
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def count_tokens(text: str) -> int:
    """Count tokens using tiktoken (cl100k_base, the GPT-4 / Claude approximation)."""
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


def count_tokens_anthropic(text: str) -> int:
    """Exact token count via the Anthropic API (requires ANTHROPIC_API_KEY)."""
    import anthropic
    client = anthropic.Anthropic()
    resp = client.messages.count_tokens(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": text}],
    )
    return resp.input_tokens


def parse_sections(text: str) -> list[tuple[str, str]]:
    """Split markdown into (heading, content) pairs."""
    pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
    matches = list(pattern.finditer(text))

    if not matches:
        return [("(entire file)", text)]

    sections = []
    for i, m in enumerate(matches):
        heading = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        level = len(m.group(1))
        sections.append((level, heading, text[start:end]))

    return sections


def fmt(n: int) -> str:
    return f"{n:,}"

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    file_path      = Path(args[0])
    show_sections  = "--sections"  in args
    use_anthropic  = "--anthropic" in args

    if not file_path.exists():
        print(f"❌  File not found: {file_path}")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8")
    char_count = len(text)
    line_count = text.count("\n") + 1
    word_count = len(text.split())

    # ── Token count ───────────────────────────────────────────────────────────
    method_label = "tiktoken cl100k (≈ Claude / GPT-4)"
    if use_anthropic:
        try:
            token_count  = count_tokens_anthropic(text)
            method_label = "Anthropic API (exact for Claude)"
        except Exception as e:
            print(f"⚠️  Anthropic API failed ({e}), falling back to tiktoken.\n")
            token_count = count_tokens(text)
    else:
        token_count = count_tokens(text)

    # ── Output ────────────────────────────────────────────────────────────────
    print()
    print(f"  📄  {file_path.name}")
    print(f"  {'─' * 46}")
    print(f"  Characters : {fmt(char_count)}")
    print(f"  Words      : {fmt(word_count)}")
    print(f"  Lines      : {fmt(line_count)}")
    print(f"  Tokens     : {fmt(token_count)}  [{method_label}]")
    print()

    # ── Cost estimates ────────────────────────────────────────────────────────
    print("  💰  Cost estimates (input tokens only)")
    print(f"  {'─' * 46}")
    for name, usd_per_m in MODELS:
        cost = (token_count / 1_000_000) * usd_per_m
        print(f"  {name:<22}  ${cost:.6f}  (${usd_per_m}/M)")
    print()

    # ── Section breakdown ─────────────────────────────────────────────────────
    if show_sections:
        sections = parse_sections(text)
        print("  📑  Token breakdown by section")
        print(f"  {'─' * 46}")
        for level, heading, content in sections:
            indent  = "  " * (level - 1)
            prefix  = "#" * level
            label   = f"{indent}{prefix} {heading}"
            n       = count_tokens(content)
            bar_len = max(1, n * 30 // token_count)
            bar     = "█" * bar_len
            pct     = n * 100 / token_count if token_count else 0
            print(f"  {label[:38]:<38}  {fmt(n):>7} tokens  {pct:4.1f}%  {bar}")
        print()


if __name__ == "__main__":
    main()
