import json
from pathlib import Path

MEMORY_DIR = Path("memory")
MEMORY_DIR.mkdir(exist_ok=True)

ALPHA_LIBRARY = MEMORY_DIR / "alpha_library.json"
REJECTED = MEMORY_DIR / "rejected_alphas.json"
PATTERNS = MEMORY_DIR / "discovered_patterns.json"
REGIMES = MEMORY_DIR / "regime_memory.json"
JOURNAL = MEMORY_DIR / "research_journal.json"


def load_json(path):
    if not path.exists():
        return []

    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def _deduplicate(data, key="expression"):
    seen = set()
    unique = []

    for item in data:
        val = item.get(key)
        if val not in seen:
            seen.add(val)
            unique.append(item)

    return unique


def save_alpha(alpha):
    data = load_json(ALPHA_LIBRARY)
    data.append(alpha)

    data = _deduplicate(data)

    save_json(ALPHA_LIBRARY, data)


def save_rejected(alpha):
    data = load_json(REJECTED)
    data.append(alpha)
    save_json(REJECTED, data)


def save_pattern(pattern):
    data = load_json(PATTERNS)
    data.append(pattern)
    save_json(PATTERNS, data)


def log_research(entry):
    data = load_json(JOURNAL)
    data.append(entry)
    save_json(JOURNAL, data)