"""
Global constants for the Sphinx extension and proc_examples.py

These are here to form a quasi-configuration file, rather than have constants
strewn across different modules.
"""
from typing import Final
from pathlib import Path

PACKAGED_ENV_NAME: Final = Path("environment.yaml")
"""
Name of the Conda environment file in zipped download files and Colab folders.
"""

OPENFF_DOCS_ROOT = Path(__file__).parent.parent.parent.parent
"""Path to the root of the openff-docs repo."""
UNIVERSAL_ENV_PATH: Final = OPENFF_DOCS_ROOT / "devtools/conda-envs/examples_env.yml"
"""
Path to the default environment file for notebooks that don't package their own.
"""
IGNORED_FILES: Final = [
    ".gitignore",
    "Thumbs.db",
    ".DS_Store",
    "thumbnail.png",
    "__pycache__",
]
"""File names to exclude from zipped download files and Colab folders."""
GITHUB_REPOS: Final = [
    "openforcefield/openff-toolkit",
    "openforcefield/openff-interchange",
]
"""
GitHub repos to download example notebooks from.

Should be given as ``username/repo-name``.
"""

DO_NOT_SEARCH = [
    "deprecated",
    "external",  # TODO: Do we really want to skip these?
]
"""Directory names to not descend into when searching for notebooks."""

SRC_IPYNB_ROOT: Final[Path] = OPENFF_DOCS_ROOT / "build/notebook-src"
"""Path to download notebooks to and cache unmodified notebooks in"""
EXEC_IPYNB_ROOT: Final[Path] = OPENFF_DOCS_ROOT / "source/notebooks"
"""Path to store executed notebooks in, ready for HTML rendering"""
COLAB_IPYNB_ROOT: Final[Path] = OPENFF_DOCS_ROOT / "source/_static/colab"
"""Path to store notebooks and their required files for Colab"""
ZIPPED_IPYNB_ROOT: Final[Path] = OPENFF_DOCS_ROOT / "source/_static/examples"
"""Path to store zips of notebooks and their required files"""
