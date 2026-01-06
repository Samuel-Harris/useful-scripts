import argparse
import subprocess
from jinja2 import Environment, FileSystemLoader
from enum import StrEnum
from pathlib import Path
from pydantic import BaseModel
from constants import DEFAULT_PYTHON_VERSION
from rich.console import Console
from rich.prompt import Confirm, Prompt
from template_paths import (
    CI_YAML_PATH,
    CURSORIGNORE_PATH,
    GEMINIIGNORE_PATH,
    HELLO_WORLD_PY_PATH,
    PRE_COMMIT_CONFIG_PATH,
    PYRIGHTCONFIG_JSON_PATH,
    TEMPLATE_DIR_PATH,
    TEST_MAIN_PY_PATH,
)

console = Console()


class PyrightMode(StrEnum):
    OFF = "off"
    BASIC = "basic"
    STANDARD = "standard"
    STRICT = "strict"


class Args(BaseModel):
    project_root: Path


def render_template(template_path: Path, **kwargs) -> str:
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR_PATH))
    relative_path = template_path.relative_to(TEMPLATE_DIR_PATH)
    template = env.get_template(str(relative_path))
    return template.render(**kwargs)


def write_file_if_not_exists(path: Path, content: str):
    if path.exists():
        console.print(f"[yellow]Skipping {path} as it already exists.[/yellow]")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    console.print(f"[green]Created {path}[/green]")


def parse_args() -> Args:
    parser = argparse.ArgumentParser(description="Initialize a new project.")
    parser.add_argument(
        "project_dir",
        nargs="?",
        default=".",
        help="Directory to initialize the project in (default: current directory)",
    )
    raw_args = parser.parse_args()

    project_root = Path(raw_args.project_dir).resolve()

    return Args(project_root=project_root)


def init_python(
    *,
    project_root: Path,
    python_version: str,
    pyright_mode: PyrightMode,
    use_pytest: bool,
):
    console.print("[blue]Initializing with uv...[/blue]")
    subprocess.run(
        [
            "uv",
            "init",
            "--name",
            project_root.name,
            "--python",
            python_version,
        ],
        cwd=project_root,
        check=True,
    )

    src_dir = project_root / "src" / "app"
    src_dir.mkdir(parents=True, exist_ok=True)
    write_file_if_not_exists(src_dir / "main.py", render_template(HELLO_WORLD_PY_PATH))
    write_file_if_not_exists(src_dir / "__init__.py", "")

    write_file_if_not_exists(
        project_root / "pyrightconfig.json",
        render_template(PYRIGHTCONFIG_JSON_PATH, type_checking_mode=pyright_mode.value),
    )

    dev_deps = ["ruff", "pyright", "pre-commit"]

    if use_pytest:
        dev_deps.append("pytest")

    console.print("[blue]Adding development dependencies with uv...[/blue]")
    subprocess.run(["uv", "add", "--dev"] + dev_deps, cwd=project_root, check=True)

    if use_pytest:
        test_dir = project_root / "src/test"
        test_dir.mkdir(parents=True, exist_ok=True)
        write_file_if_not_exists(test_dir / "__init__.py", "")
        write_file_if_not_exists(
            test_dir / "test_main.py", render_template(TEST_MAIN_PY_PATH)
        )


def init_precommit(
    *,
    project_root: Path,
    is_python_project: bool,
):
    pre_commit_config = render_template(
        PRE_COMMIT_CONFIG_PATH,
        is_python_project=is_python_project,
    )

    write_file_if_not_exists(
        project_root / ".pre-commit-config.yaml", pre_commit_config
    )


def init_ci(
    *,
    project_root: Path,
    python_version: str,
    use_pytest: bool,
):
    ci_content = render_template(
        CI_YAML_PATH,
        python_version=python_version,
        use_pytest=use_pytest,
    )

    workflows_dir = project_root / ".github" / "workflows"
    workflows_dir.mkdir(parents=True, exist_ok=True)
    write_file_if_not_exists(workflows_dir / "ci.yml", ci_content)


class PythonProjectConfig(BaseModel):
    python_version: str
    pyright_mode: PyrightMode
    use_pytest: bool


class ProjectConfig(BaseModel):
    project_root: Path
    create_project_root: bool = False
    python_config: PythonProjectConfig | None = None
    want_ci: bool = False
    want_cursorignore: bool = False
    want_geminiignore: bool = False

    class Config:
        arbitrary_types_allowed = True


def construct_project_config(project_root: Path) -> ProjectConfig | None:
    console.print(f"[bold blue]Initializing project in:[/bold blue] {project_root}")

    if not project_root.exists():
        create_project_root_dir = Confirm.ask(
            f"Directory {project_root} does not exist. Create it?"
        )

        if not create_project_root_dir:
            console.print("[red]Aborted.[/red]")
            return None
    else:
        create_project_root_dir = False

    is_python_project = Confirm.ask("Would you like to set up a Python project?")
    want_ci = Confirm.ask("Would you like a GitHub CI workflow?")

    python_config = None
    if is_python_project:
        python_version = Prompt.ask(
            "Which Python version?", default=DEFAULT_PYTHON_VERSION
        )

        mode_str = Prompt.ask(
            "Which type checking mode?",
            choices=[m.value for m in PyrightMode],
            default=PyrightMode.STRICT.value,
        )
        pyright_mode = PyrightMode(mode_str)

        use_pytest = Confirm.ask("Would you like to use pytest?")

        python_config = PythonProjectConfig(
            python_version=python_version,
            pyright_mode=pyright_mode,
            use_pytest=use_pytest,
        )

    want_cursorignore = Confirm.ask("Would you like a .cursorignore file?")
    want_geminiignore = Confirm.ask("Would you like a .geminiignore file?")

    return ProjectConfig(
        project_root=project_root,
        create_project_root=create_project_root_dir,
        python_config=python_config,
        want_ci=want_ci,
        want_cursorignore=want_cursorignore,
        want_geminiignore=want_geminiignore,
    )


def init_project(config: ProjectConfig):
    if config.create_project_root:
        config.project_root.mkdir(parents=True)

    if config.python_config is not None:
        init_python(
            project_root=config.project_root,
            python_version=config.python_config.python_version,
            pyright_mode=config.python_config.pyright_mode,
            use_pytest=config.python_config.use_pytest,
        )

    init_precommit(
        project_root=config.project_root,
        is_python_project=config.python_config is not None,
    )

    if config.want_ci and config.python_config is not None:
        init_ci(
            project_root=config.project_root,
            python_version=config.python_config.python_version,
            use_pytest=config.python_config.use_pytest,
        )

    if config.want_cursorignore:
        write_file_if_not_exists(
            config.project_root / ".cursorignore",
            render_template(CURSORIGNORE_PATH),
        )

    if config.want_geminiignore:
        write_file_if_not_exists(
            config.project_root / ".geminiignore",
            render_template(GEMINIIGNORE_PATH),
        )


def main():
    args = parse_args()
    config = construct_project_config(args.project_root)
    if config is None:
        return
    init_project(config)


if __name__ == "__main__":
    main()
