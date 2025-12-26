md_docs_parser - Convert Large Markdown Documentation into LLM-Parsible Directory Structure

DESCRIPTION
-----------
This script takes very long markdown documentation files (e.g., comprehensive library docs) and converts them into a structured directory hierarchy that's much more suitable for Large Language Models (LLMs) to parse and navigate.

The script processes markdown headers to create a logical directory structure:
- H1 headers (#) become directories
- H2 (##) and H3 (###) headers become individual markdown files within those directories
- Introductory content goes into introduction.md files
- Automatic generation of index.md files for navigation

This approach solves the common problem where LLMs struggle to effectively use massive single-file documentation due to context length limitations and difficulty in locating specific information.

USAGE
-----
uv run script.py <input_file> <output_directory>

ARGUMENTS
---------
input_file      Path to the input markdown file (can be very large)
output_directory Path where the structured documentation will be created

EXAMPLE
-------
uv run script.py pydantic_ai_docs.md ./pydantic_ai_structured_docs

OUTPUT STRUCTURE
---------------
After processing, you'll get a directory structure like:

output_directory/
├── index.md                    # Root table of contents linking to all main topics
├── topic1_directory/
│   ├── index.md               # Table of contents for this topic
│   ├── introduction.md        # Any intro text for this topic
│   ├── subtopic1.md          # Content from H2/H3 headers
│   └── subtopic2.md
└── topic2_directory/
    ├── index.md
    └── ...

LLM USAGE RECOMMENDATIONS
-------------------------
When providing the generated documentation to an LLM, use the prompt template from llm_docs_usage_prompt.md to help the LLM understand and effectively navigate the structure.

The structured approach allows LLMs to:
1. Quickly identify relevant high-level topics via the root index.md
2. Drill down into specific areas using topic-specific index.md files
3. Read only the relevant content files instead of processing massive single files
4. Maintain context about where information is located in the overall documentation

BENEFITS FOR LLM CONSUMPTION
---------------------------
- Eliminates context length issues with massive single files
- Enables precise information retrieval by topic/section
- Provides clear navigation paths through index.md files
- Maintains logical document organization
- Reduces token usage by allowing focused reading of relevant sections

DEPENDENCIES
-----------
- Python 3.14+
- Standard library only (pathlib, argparse, re, shutil, os)

CLEANUP
-------
The script automatically removes empty files and directories that may be created during processing.

NOTES
-----
- Input files can be extremely large (tested with 100k+ line documentation)
- All markdown formatting is preserved in the output files
- Filenames are automatically sanitized for filesystem compatibility
- The script will overwrite existing output directories
