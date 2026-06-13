from engine.mythos_validator import (
    run_mythos_validation
)


def validate_alpha(
    returns
):

    report = run_mythos_validation(
        returns
    )

    if report is None:

        return None

    if report["rb_score"] < 70:

        return None

    if report["pbo"] > 0.20:

        return None

    return report