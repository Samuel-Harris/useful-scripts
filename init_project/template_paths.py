from pathlib import Path

TEMPLATE_DIR_PATH = Path(__file__).parent / "templates"

HELLO_WORLD_PY_PATH = TEMPLATE_DIR_PATH / "hello_world.py"
PYRIGHTCONFIG_JSON_PATH = TEMPLATE_DIR_PATH / "pyrightconfig.json"
TEST_MAIN_PY_PATH = TEMPLATE_DIR_PATH / "test_main.py"

PRE_COMMIT_CONFIG_PATH = TEMPLATE_DIR_PATH / "pre-commit-config.yaml"
CI_YAML_PATH = TEMPLATE_DIR_PATH / "ci.yaml"

CURSORIGNORE_PATH = TEMPLATE_DIR_PATH / "ignore" / "cursorignore.tpl"
GEMINIIGNORE_PATH = TEMPLATE_DIR_PATH / "ignore" / "geminiignore.tpl"
