


import yaml
from main import Types, load_counts, update_count, main_



def test_main():
    # Given an activitet


    counts = {
        Types.RUN: 0
    }
    data = {
        "type": Types.RUN,
        "title": "morgen løb"
    }
    
    # When we call for rewirting the title
    
    counts[data["type"]] += 1
    data["title"] = f'{(data["type"].value).title()} #{counts[data["type"]]}'

    # Then it should be "Type #number"
    assert data["title"] == "Run #1"


def test_load_counts(tmp_path):
    # Given the following `.yaml` content and it is wirted to an `yaml`-file.
    yaml_content = {
        "counts": {
            "run": 55,
            "svimning": 12
        },
        "data": "Må ikke slettes"
    }
    file = tmp_path / "config.yaml"
    file.write_text(yaml.safe_dump(yaml_content))
    # When we 
    counts = load_counts(file)
    # Then number of keys should be two
    assert len(counts) == 2
    # Then the count for `Types.RUN` and `Types.SVIMNING` should respectively be 55 and 12
    assert counts[Types.RUN] == 55
    assert counts[Types.SVIMNING] == 12


def test_update_count(tmp_path):
    # Given the following `.yaml` content and it is wirted to an `yaml`-file.
    yaml_content = {
        "counts": {
            "run": 55,
            "svimning": 12
        },
        "data": "Må ikke slettes"
    }
    file = tmp_path / "config.yaml"
    file.write_text(yaml.safe_dump(yaml_content))
    # Given 
    counts = {Types.RUN: 55, Types.SVIMNING: 13}
    # When we update the 
    update_count(file, counts)
    # Then
    counts = load_counts(file)
    assert counts[Types.RUN] == 55
    assert counts[Types.SVIMNING] == 13


def test_main_(tmp_path):
    # Given the following `.yaml` content and it is writed to an `yaml`-file.
    yaml_content = {
        "counts": {
            "run": 55,
            "svimning": 12
        },
        "data": "Må ikke slettes"
    }
    file = tmp_path / "config.yaml"
    file.write_text(yaml.safe_dump(yaml_content))
    data = {"type": Types.RUN, "title": "morgen løb"}
    # When
    data = main_(file, data)
    # Then
    assert data["title"] == "Run #56"

