def estimate_book_capacity(
    daily_volume,
    participation=0.05
):

    return (
        daily_volume.mean()
        *
        participation
    )