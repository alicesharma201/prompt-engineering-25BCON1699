# Documentation Audit

This audit follows the Session 5 instruction to verify AI-generated documentation against the real repository before publishing.

## Repository Checked

- Repository: `prompt-engineering-25BCON1699`
- Branch checked: `main`
- Files present:
  - `README.md`
  - `Session5/audit.md`
  - `Session5/even_odd.py`
  - `Session5/factorial.py`
  - `Session5/fibonacci.py`
  - `Session5/largest.py`
  - `Session5/palindrome.py`
  - `Session5/struct.c`

## README Claim Check

| README claim | Evidence checked | Result |
| --- | --- | --- |
| The project contains small programming practice examples for Prompt Engineering coursework. | Repository name, Session 5 folder, and source files are consistent with coursework practice examples. | Verified |
| `Session5/factorial.py` calculates the factorial of `5` using a loop. | File sets `n = 5`, loops from `1` to `n`, multiplies into `fact`, and prints the result. | Verified |
| `Session5/fibonacci.py` prints the first `10` Fibonacci numbers. | File sets `n = 10` and prints ten values starting from `0`. | Verified |
| `Session5/even_odd.py` checks whether `10` is even or odd. | File sets `n = 10`, checks `n % 2 == 0`, and prints `Even`. | Verified |
| `Session5/largest.py` finds the largest value among `10`, `25`, and `15`. | File sets `a = 10`, `b = 25`, `c = 15`, uses `max(a, b, c)`, and prints `Largest number = 25`. | Verified |
| `Session5/palindrome.py` checks whether `madam` is a palindrome. | File sets `text = "madam"`, compares it with `text[::-1]`, and prints `Palindrome`. | Verified |
| `Session5/struct.c` demonstrates a C `struct` named `Student`. | File defines `struct Student` with `name`, `roll`, and `marks`, assigns sample values, and prints them. | Verified |
| `Session5/audit.md` audits the README and commit messages. | File contains README claim checks, run verification, commit history, and commit message comparison. | Verified |
| Python files can be run with `python3`. | All five Python commands documented in the README were run successfully. | Verified |
| C file can be compiled with `gcc` and run as an executable. | `gcc Session5/struct.c -o /tmp/session5_struct_audit` compiled successfully, and the executable ran successfully. | Verified |
| Python 3 and GCC/C compiler are the required dependencies. | Python scripts use only built-in language features; C program uses standard headers `stdio.h` and `string.h`. | Verified |
| No extra Python packages are required. | No imports or package files are present for the Python scripts. | Verified |
| Created and maintained by `Alice Sharma [25BCON1699]`. | Git user is `alicesharma201`; repository name includes `25BCON1699`; screenshot evidence shows Alice Sharma as contributor. | Mostly verified |

## Run Verification

Commands tested:

```bash
python3 Session5/factorial.py
python3 Session5/fibonacci.py
python3 Session5/even_odd.py
python3 Session5/largest.py
python3 Session5/palindrome.py
gcc Session5/struct.c -o /tmp/session5_struct_audit
/tmp/session5_struct_audit
```

Observed outputs:

```text
Factorial of 5 = 120
Fibonacci series: 0 1 1 2 3 5 8 13 21 34
Even
Largest number = 25
Palindrome
Name: Alice
Roll: 101
Marks: 87.5
```

## Commit History Check

The repository has meaningful commit history:

- `Initial commit`
- `feat: add factorial program`
- `feat: add fibonacci series program`
- `feat: add struct program`
- `docs: add comments to factorial program`
- `docs: add readme`
- `docs: add audit`
- `feat: add even or odd program`
- `feat: largest of three numbers program`
- `feat: check palindrome program`

These commits match the Session 5 expectation that project history should show clear savepoints.

## Commit Message Comparison

| Commit | My message | AI message | Which is clearer, and why? |
| --- | --- | --- | --- |
| 1 | `Initial commit` | `chore: initialize project repository` | The AI message is clearer because it follows the `type: summary` format and says the repository was initialized. |
| 2 | `feat: add factorial program` | `feat: add factorial calculator` | The AI message is slightly clearer because "calculator" tells the reader the program calculates a result, not just that a file was added. |
| 3 | `feat: add fibonacci series program` | `feat: add fibonacci series program` | Both are equally clear because they identify the feature and describe the program accurately. |
| 4 | `feat: add struct program` | `feat: add student info struct program` | The AI message is clearer because it explains what the struct program is about: student information. |
| 5 | `docs: add comments to factorial program` | `docs: comment factorial logic` | The AI message is clearer because it is shorter and directly says the factorial logic was commented. |
| 6 | `docs: add readme` | `docs: add project README` | The AI message is clearer because it specifies that the README documents the project. |
| 7 | `docs: add audit` | `docs: add documentation audit` | The AI message is clearer because it explains what kind of audit was added. |
| 8 | `feat: add even or odd program` | `feat: add even odd checker` | The AI message is clearer because "checker" describes the program's purpose more directly. |
| 9 | `feat: largest of three numbers program` | `feat: add largest number finder` | The AI message is clearer because it follows the same imperative style as the other feature commits. |
| 10 | `feat: check palindrome program` | `feat: add palindrome checker` | The AI message is clearer because it uses an imperative verb and names the program purpose cleanly. |

## Issues Found

- No false dependency claims were found.
- The README previously referenced `audit.md`, but the file has been moved to `Session5/audit.md`. The README has been updated to use the correct path.
- No license is claimed in the README, and no `LICENSE` file is present. This is acceptable because the README does not say the project has a license.
- The author claim is mostly supported, but the README does not include a direct contact method. This is not required by the assignment.

## Final Audit Result

The README is accurate for the current repository. The documented filenames, descriptions, run commands, and dependency requirements were checked against the real files and verified.
