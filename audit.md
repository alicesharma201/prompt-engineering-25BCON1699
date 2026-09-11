# Documentation Audit

This audit follows the Session 5 instruction to verify AI-generated documentation against the real repository before publishing.

## Repository Checked

- Repository: `prompt-engineering-25BCON1699`
- Branch checked: `main`
- Files present:
  - `README.md`
  - `Session5/factorial.py`
  - `Session5/fibonacci.py`
  - `Session5/struct.c`

## README Claim Check

| README claim | Evidence checked | Result |
| --- | --- | --- |
| The project contains small programming practice examples for Prompt Engineering coursework. | Repository name, Session 5 folder, and source files are consistent with coursework practice examples. | Verified |
| `Session5/factorial.py` calculates the factorial of `5` using a loop. | File sets `n = 5`, loops from `1` to `n`, multiplies into `fact`, and prints the result. | Verified |
| `Session5/fibonacci.py` prints the first `10` Fibonacci numbers. | File sets `n = 10` and prints ten values starting from `0`. | Verified |
| `Session5/struct.c` demonstrates a C `struct` named `Student`. | File defines `struct Student` with `name`, `roll`, and `marks`, assigns sample values, and prints them. | Verified |
| Python files can be run with `python3`. | Both Python commands were run successfully. | Verified |
| C file can be compiled with `gcc` and run as an executable. | `gcc Session5/struct.c -o /tmp/session5_struct_audit` compiled successfully, and the executable ran successfully. | Verified |
| Python 3 and GCC/C compiler are the required dependencies. | Python scripts use only built-in language features; C program uses standard headers `stdio.h` and `string.h`. | Verified |
| No extra Python packages are required. | No imports or package files are present for the Python scripts. | Verified |
| Created and maintained by `Alice Sharma [25BCON1699]`. | Git user is `alicesharma201`; repository name includes `25BCON1699`; screenshot evidence shows Alice Sharma as contributor. | Mostly verified |

## Run Verification

Commands tested:

```bash
python3 Session5/factorial.py
python3 Session5/fibonacci.py
gcc Session5/struct.c -o /tmp/session5_struct_audit
/tmp/session5_struct_audit
```

Observed outputs:

```text
Factorial of 5 = 120
Fibonacci series: 0 1 1 2 3 5 8 13 21 34
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

These commits match the Session 5 expectation that project history should show clear savepoints.

## Commit Message Comparison

| Commit | My message | AI message | Which is clearer, and why? |
| --- | --- | --- | --- |
| 1 | `feat: add factorial program` | `feat: add factorial calculator` | The AI message is slightly clearer because "calculator" tells the reader the program calculates a result, not just that a file was added. |
| 2 | `feat: add fibonacci series program` | `feat: add fibonacci series program` | Both are equally clear because they identify the feature and describe the program accurately. |
| 3 | `feat: add struct program` | `feat: add student info struct program` | The AI message is clearer because it explains what the struct program is about: student information. |

## Issues Found

- No false dependency claims were found.
- No missing files are referenced by the README.
- No license is claimed in the README, and no `LICENSE` file is present. This is acceptable because the README does not say the project has a license.
- The author claim is mostly supported, but the README does not include a direct contact method. This is not required by the assignment.

## Final Audit Result

The README is accurate for the current repository. The documented filenames, descriptions, run commands, and dependency requirements were checked against the real files and verified.
