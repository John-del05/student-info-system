import json
from pathlib import Path

def ensure_data_file(file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    if not Path(file_path).exists():
        with open(file_path, 'w') as f:
            json.dump([], f)

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
