# Token Calculator

**File:** [`token_calculator.py`](token_calculator.py)

Reads a Markdown file and tells you how many tokens it contains, with cost estimates for the most common AI models. Useful before sending a document to an API so you know what you're paying for.

---

## Requirements

```bash
pip install tiktoken
pip install anthropic  # optional — only needed for --anthropic
```

---

## Usage

```bash
python3 token_calculator.py <file.md> [--sections] [--anthropic]
```

### Flags

| Flag | Description |
|------|-------------|
| _(none)_ | Count tokens and show cost estimates |
| `--sections` | Also break down token count per Markdown heading |
| `--anthropic` | Use the Anthropic API for an exact Claude token count instead of the tiktoken approximation. Requires `ANTHROPIC_API_KEY` in your environment. Falls back to tiktoken if the API call fails. |

---

## Examples

**Basic count:**
```bash
python3 token_calculator.py my-notes.md
```
```
  📄  my-notes.md
  ──────────────────────────────────────────────
  Characters : 4,821
  Words      : 732
  Lines      : 98
  Tokens     : 1,104  [tiktoken cl100k (≈ Claude / GPT-4)]

  💰  Cost estimates (input tokens only)
  ──────────────────────────────────────────────
  Claude Haiku 4.5        $0.000883  ($0.8/M)
  Claude Sonnet 4.6       $0.003312  ($3.0/M)
  Claude Opus 4.7         $0.016560  ($15.0/M)
  GPT-4o                  $0.002760  ($2.5/M)
  GPT-4o mini             $0.000166  ($0.15/M)
```

**With section breakdown:**
```bash
python3 token_calculator.py my-notes.md --sections
```
```
  📑  Token breakdown by section
  ──────────────────────────────────────────────
  # Introduction                               142 tokens  12.9%  ███
    ## Background                              310 tokens  28.1%  ████████
    ## Details                                 498 tokens  45.1%  █████████████
  # Conclusion                                 154 tokens  13.9%  ████
```

**Exact count via Claude API:**
```bash
ANTHROPIC_API_KEY=sk-... python3 token_calculator.py my-notes.md --anthropic
```

---

## How it works

- **Default mode** uses [tiktoken](https://github.com/openai/tiktoken) with the `cl100k_base` encoding (the same tokenizer used by GPT-4). It's a good approximation for Claude too — usually within a few percent.
- **`--anthropic` mode** calls `client.messages.count_tokens()` from the Anthropic SDK, which gives the exact token count for Claude models.
- **`--sections`** splits the file on Markdown headings (`#` through `######`) and tokenizes each chunk separately. The bar next to each section is proportional to its share of the total.

---

## Notes

- Cost estimates are for **input tokens only** — output tokens are billed separately.
- Prices are hardcoded in the `MODELS` list at the top of the script; update them if rates change.
