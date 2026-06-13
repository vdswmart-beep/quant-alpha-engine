from research.memory import (
    load_memory
)


def is_novel(
    alpha_code
):

    library = load_memory(
        "alpha_library.json"
    )

    for alpha in library:

        if alpha["code"] == alpha_code:
            return False

    return True