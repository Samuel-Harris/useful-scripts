# useful-scripts

Useful scripts

## Table of Contents

- [useful-scripts](#useful-scripts)
  - [Table of Contents](#table-of-contents)
  - [Available Scripts](#available-scripts)
    - [md_docs_parser](#md_docs_parser)

## Available Scripts

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
