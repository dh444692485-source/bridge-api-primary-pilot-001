def normalize_counts(values):
    """Summarize a list of nonnegative built-in integers."""
    if type(values) is not list:
        raise TypeError("values must be a list")
    for value in values:
        if type(value) is not int:
            raise TypeError("values must contain built-in integers")
    if any(value < 0 for value in values):
        raise ValueError("values must be nonnegative")
    return {
        "count": len(values),
        "total": sum(values),
        "maximum": max(values, default=0),
    }
