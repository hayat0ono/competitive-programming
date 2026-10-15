<h1 align="center">Competitive Programming</h1>

<p align="center">
  Competitive programming & algorithm practice by hayat0ono
</p>

## 🧩 About

Solutions, practice notes, and reusable snippets for competitive programming and algorithm practice, written in Python and C++. Problems are organized by platform, including [AtCoder](https://atcoder.jp/users/hayat0ono0628) and [LeetCode](https://leetcode.com/hayat0ono0628).

## 📁 Repository Structure

- `src/atcoder/<category>/<hundred>/<contest-number>/`: AtCoder solutions grouped by hundreds (e.g., `src/atcoder/abc/600/628/`).
- `src/leetcode/<hundred>/<problem-number>/main.py` or `main.cpp`: LeetCode solutions grouped by hundreds (e.g., `src/leetcode/1000/1016/main.py`).
- `snippets/`: Python input examples and algorithms to copy into solutions as needed.
- `.tools/setup_contest.bat`: Creates AtCoder contest or LeetCode problem folders and solution templates.

## 🚀 Problem & Contest Setup

Run from the repository root in PowerShell on Windows.

```powershell
.\.tools\setup_contest.bat atcoder abc628      # Python (optional: py)
.\.tools\setup_contest.bat atcoder abc628 cpp  # C++
.\.tools\setup_contest.bat leetcode 1016 1017 1018
.\.tools\setup_contest.bat leetcode 1016 1017 1018 cpp
```

For AtCoder, use `abc`, `arc`, `agc`, or `ahc` followed by the contest number. Existing files are preserved.

LeetCode accepts one or more positive problem numbers. The optional final argument selects `py` (default) or `cpp`. Each problem gets an empty `main.py` or `main.cpp`; existing files are preserved.

## 💻 Run Locally

Install Python or a C++ compiler (g++ below), then run from the repository root.

```powershell
python src/atcoder/abc/400/425/a.py

g++ -std=c++17 -O2 src/atcoder/abc/400/425/a.cpp -o a.exe
if ($LASTEXITCODE -eq 0) { .\a.exe }
```

For LeetCode, implement the solution in the generated `main.py` or `main.cpp` and submit it through LeetCode. To test locally, add the necessary test cases and entry point.
