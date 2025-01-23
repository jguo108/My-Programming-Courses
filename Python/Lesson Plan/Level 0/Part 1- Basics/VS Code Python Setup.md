# VS Code Python Setup

### Reference

https://www.youtube.com/watch?v=9o4gDQvVkLU

https://www.youtube.com/watch?v=GZbeL5AcTgw

### Basic Setup

- Install Python and VS Code
- Install ‘Python’ (by Microsoft) extension and ‘Code Runner’ extension
- Change output window from ‘Output’ to ‘Terminal’: Settings → Code Actions On Save → Add ‘code-runner.runInTerminal’: true

### Select Difference Python Version

1. Under the `View` menu select `Command Palette... F1` (or press F1 key).
2. Type `Python: Select Interpreter`.
3. Choose which Python version to use by default [1].

### Venv

- Open the project folder in VS Code
- Type in ‘*python -m venv .venv*’