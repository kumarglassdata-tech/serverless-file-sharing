# Contributing

## Getting Started
1. Fork the repo and create a feature branch
2. Make your changes with clear commit messages
3. Add or update tests as appropriate
4. Open a pull request against `main`

## Commit Message Style
Use the imperative mood: "add", "fix", "update", not "added" or "adds".

## Code Style
- Python 3.12+
- 4-space indentation
- Keep Lambda handlers short — extract helpers for logic

## Running Tests
```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```
