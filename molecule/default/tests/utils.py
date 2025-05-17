# molecule/default/tests/utils.py
from pathlib import Path

import yaml


def load_yaml(relative_path, default=None):
    try:
        full_path = (Path(__file__).resolve().parent / relative_path).resolve()
        with open(full_path, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return default or {}


def load_role_vars():
    return load_yaml("../vars/all.yml")
