"""Format normalized counts as a single line."""

if __package__:
    from .normalize import normalize_counts
else:
    from normalize import normalize_counts


def display_counts(values):
    """Return a readable summary of nonnegative built-in integers."""
    counts = normalize_counts(values)
    return (
        f"count={counts['count']}; total={counts['total']}; "
        f"maximum={counts['maximum']}"
    )
