import random


WINDOWS = [
    5,
    10,
    20,
    50,
    100,
    200
]


def mutate_alpha(
    expression
):
    """
    Mutation simple :

    remplace une fenêtre
    par une autre.
    """

    numbers = []

    current = ""

    for c in expression:

        if c.isdigit():

            current += c

        else:

            if current:

                numbers.append(current)

                current = ""

    if current:

        numbers.append(current)

    if len(numbers) == 0:

        return expression

    target = random.choice(
        numbers
    )

    new_window = str(
        random.choice(
            WINDOWS
        )
    )

    return expression.replace(
        target,
        new_window,
        1
    )