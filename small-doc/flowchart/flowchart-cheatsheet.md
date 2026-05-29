# Flowchart — Quick Cheat Sheet

---

## Symbols (ISO 5807)

| Symbol | Shape | Use |
|--------|-------|-----|
| Terminal | Oval / rounded rectangle | Start or End of the process |
| Process | Rectangle | Action, calculation, assignment |
| Decision | Diamond | Condition (2 exits: Yes / No) |
| Input / Output | Parallelogram | Read or display a value |
| Subprocess | Rectangle (side bars) | Function or procedure call |
| Connector | Circle | Cross-reference on the same page |
| Off-page connector | Pentagon | Cross-reference on another page |
| Database | Cylinder | Read / write persistent data |
| Document | Rectangle (wavy base) | Report, print, file |
| Flow | Arrow | Direction of the process |

---

## Control structures

| Structure | Description |
|-----------|-------------|
| **Sequence** | Blocks chained top to bottom, no condition |
| **Condition (if/else)** | Diamond → Yes branch and No branch, rejoining after |
| **While loop** | Condition tested **before** the process — may never execute |
| **Do…while loop** | Process runs **before** the condition — executes at least once |

---

## Common decision labels

| Context | True branch | False branch |
|---------|-------------|--------------|
| Closed question | `Yes` | `No` |
| Boolean condition | `True` | `False` |
| Numeric comparison | `≥ 0`, `> threshold` | `< 0`, `≤ threshold` |
| Validation | `Valid` / `OK` | `Invalid` / `KO` |
| Existence | `Exists` | `Does not exist` |
| State | `Active` | `Inactive` |

---

## Drawing rules

| Rule | Detail |
|------|--------|
| Reading direction | Top → bottom or left → right — consistent throughout |
| Entry point | Exactly one Start terminal |
| Exit point | One or more End terminals |
| Diamond exits | Exactly 2 — never more |
| Arrow crossings | Forbidden — use a connector symbol |
| Flow labels | Required on both exits of every diamond |
| Process name | Action verb: `Validate order`, `Calculate tax` |
| Decision phrasing | Closed question: `Stock sufficient?`, `User logged in?` |

---

## Mermaid — quick syntax

| Syntax | Output |
|--------|--------|
| `flowchart TD` | Top → bottom diagram |
| `flowchart LR` | Left → right diagram |
| `A([Start])` | Terminal (oval) |
| `A[Process]` | Rectangle |
| `A{Decision}` | Diamond |
| `A[\Input/Output/]` | Parallelogram |
| `A[[Subprocess]]` | Rectangle with side bars |
| `A[(Database)]` | Cylinder |
| `A --> B` | Plain arrow |
| `A -->|Yes| B` | Arrow with label |
