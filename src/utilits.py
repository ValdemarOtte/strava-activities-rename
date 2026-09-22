### Imports
# Standard library
from pathlib import Path

# Third-party libraries
import yaml

# Local files


def read_yaml(file: Path) -> dict:
    """
    Read an `.yaml`-file and return it's content.

    Parameters
    ----------
    file : Path
        Path to the file.

    Returns
    -------
    dict
        The `.yaml-file`'s content as a dict.

    """
    with Path.open(file, encoding="UTF-8") as f:
        return yaml.safe_load(f)


def write_yaml(file: Path, content: dict) -> None:
    """
    Read an `.yaml`-file and return it's content.

    Parameters
    ----------
    file : Path
        Path to the file.
    content : dict
        The content which will be writed to the file.

    """
    with open(file, "w") as f:
        yaml.safe_dump(content, f, sort_keys=False)
