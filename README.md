# useful-scripts

Useful scripts

## Table of Contents

- [useful-scripts](#useful-scripts)
  - [Table of Contents](#table-of-contents)
  - [Available Scripts](#available-scripts)
    - [init_project](#init_project)
    - [md_docs_parser](#md_docs_parser)

## Available Scripts

### init_project

Interactive CLI tool for scaffolding new projects with opinionated defaults for Python development.

**Location**: `init_project/main.py`

**Usage**: `cd init_project && uv run main.py [project_directory]`

**Description**: Interactively scaffolds new projects with automated setup of common development tools like `uv`, `ruff`, `pyright`, `pre-commit`, and optionally `pytest`. Also supports GitHub CI workflows and AI assistant ignore files (`.cursorignore`, `.geminiignore`).

**Key Features**:

- Interactive prompts for all configuration options
- Python project setup with uv package manager
- Automatic installation of dev tools (ruff, pyright, pre-commit)
- Configurable Pyright type checking mode (off/basic/standard/strict)
- Optional pytest integration with starter test files
- GitHub Actions CI workflow generation
- AI assistant ignore file templates

For detailed usage instructions and examples, see [`init_project/README.md`](init_project/README.md).

---

### md_docs_parser

Convert large markdown documentation files into structured directory hierarchies optimized for LLM consumption.

**Location**: `md_docs_parser/main.py`

**Usage**: `uv run main.py <input_file> <output_directory>`

**Description**: This script takes very long markdown documentation files (e.g., comprehensive library docs) and converts them into a structured directory hierarchy that's much more suitable for Large Language Models (LLMs) to parse and navigate.

**Key Features**:

- Converts H1 headers (#) into directories
- Converts H2 (##) and H3 (###) headers into individual markdown files
- Generates index.md files for navigation
- Handles extremely large files (tested with 100k+ lines)
- Preserves all markdown formatting
- Automatic cleanup of empty files/directories

For detailed usage instructions and examples, see [`md_docs_parser/README.md`](md_docs_parser/README.md).
