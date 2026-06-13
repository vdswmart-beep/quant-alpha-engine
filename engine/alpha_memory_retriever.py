import json
from pathlib import Path

MEMORY = Path(
    "memory/alpha_library.json"
)

def retrieve_best_alphas(
    top_n=20
):

    if not MEMORY.exists():

        return []

    data = json.loads(
        MEMORY.read_text()
    )

    data = sorted(
        data,
        key=lambda x:
        x["rb_score"],
        reverse=True
    )

    return data[:top_n]