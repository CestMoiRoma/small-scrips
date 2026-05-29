# Flowchart (Logigramme)

A flowchart is a graphical representation of a process or algorithm. It describes a sequence of steps, decisions, and flows using standardized symbols (ISO 5807).

---

## Core symbols

| Symbol | Shape | Role |
|--------|-------|------|
| **Terminal** | Oval / rounded rectangle | Marks the **start** or **end** of the process |
| **Process** | Rectangle | An action or operation to perform |
| **Decision** | Diamond | A condition with two exits: Yes / No |
| **Input / Output** | Parallelogram | Reading a value or displaying a result |
| **Subprocess** | Rectangle with side bars | Call to a predefined process (function, procedure) |
| **Connector** | Circle | Links two parts of the flowchart on the same page |
| **Off-page connector** | Pentagon | Links two parts across different pages |
| **Database** | Cylinder | Reading or writing persistent data |
| **Document** | Rectangle with wavy base | A produced document or report |
| **Flow** | Arrow | Direction of the process |

---

## Mandatory structure

Every flowchart must have:

- **A single entry point** — one Start terminal
- **At least one exit point** — one or more End terminals
- **A clear reading direction** — top → bottom, or left → right

---

## Decisions

A diamond always has **exactly two exits**. Each branch must be explicitly labelled.

| Branch | Common labels |
|--------|---------------|
| True | `Yes`, `True`, `≥ 0`, `Valid`, `OK` |
| False | `No`, `False`, `< 0`, `Invalid`, `KO` |

> Never leave a diamond exit unlabelled — the flow direction must always be unambiguous.

---

## Control structures

### Sequence

Processes chained one after another with no condition, top to bottom. The simplest structure.

### Condition (if / else)

A diamond splits the flow into two paths. The **Yes** branch executes one treatment, the **No** branch executes another (or nothing). Both paths rejoin afterwards.

### Loop (while — pre-test)

The condition is tested **before** the process executes. If `Yes`, the process runs and the flow returns to the decision. If `No`, the loop exits.

### Loop (do…while — post-test)

The process runs **at least once**, then the condition is tested. If `Yes`, the flow returns to the start of the process. If `No`, the loop exits.

---

## Basic rules

> A flowchart always has an explicit start and end represented by terminals.

> Arrows never cross. If unavoidable, use a connector symbol.

> Each diamond has exactly two exits — never one, never three.

> Infinite loops must be avoided unless intentional and clearly documented.
