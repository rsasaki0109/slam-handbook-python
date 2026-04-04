# Contributing

Thank you for your interest in contributing to SLAM Handbook Python!

## Getting Started

```bash
git clone https://github.com/rsasaki0109/slam-handbook-python.git
cd slam-handbook-python
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Code Style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting.

```bash
ruff check utils/ tests/
ruff format utils/ tests/
```

## Testing

```bash
pytest tests/ -v
```

All tests must pass before submitting a pull request.

## Notebooks

- Write comments and explanations in Japanese
- Ensure notebooks run on Google Colab without additional setup
- Install dependencies in the first cell using `!pip install`
- Avoid hardcoded local file paths

## Pull Requests

- One logical change per PR
- Include a description of what changed and why
- Make sure CI passes (lint + tests)

## Issues

Please use the provided issue templates:
- **Bug Report**: for errors in notebooks or utility modules
- **Feature Request**: for new topics or improvements
