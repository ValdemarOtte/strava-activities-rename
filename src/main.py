### Imports
# Standard library
from enum import Enum
from pathlib import Path

# Third-party libraries

# Local files
from utilits import read_yaml, write_yaml


class Types(Enum):
    RUN = "run"
    SVIMNING = "svimning"


def load_counts(file: Path) -> dict[Types, int]:
    data = read_yaml(file)
    return {Types(key): value for key, value in data["counts"].items()}


def update_count(file: Path, counts: dict[Types, int]) -> None:
    data = read_yaml(file)
    # Go from Enum to string value
    counts = {key.value: value for key, value in counts.items()}
    data["counts"] = counts
    write_yaml(file, data)


def main_(file: Path, data: dict) -> dict:
    counts = load_counts(file)
    counts[data["type"]] += 1
    data["title"] = f'{(data["type"].value).title()} #{counts[data["type"]]}'
    update_count(file, counts)
    return data





def main():
    file = Path("src\\config.yaml")
    elements = [
        {
            "type": Types.RUN,
            "title": "morgen løb",
            "time": date
        },
        {
            "type": Types.RUN,
            "title": "morgen løb"
        },
        {
            "type": Types.SVIMNING,
            "title": "morgen svømning"
        },
    ]

    # main
    for d in elements:

        data = main_(file, d)
        for key, value in data.items():
            print(f"{key:<5}: {value}")
        print()


if __name__ == "__main__":
    main()
