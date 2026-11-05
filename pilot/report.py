"""Serialize normalized counts as compact, deterministic JSON."""

import json

if __package__:
    from .normalize import normalize_counts
else:
    from normalize import normalize_counts


def report_counts(values):
    """Return a JSON summary of nonnegative built-in integers."""
    return json.dumps(normalize_counts(values), sort_keys=True, separators=(",", ":"))
