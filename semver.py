"""Minimal semver parse & compare (major.minor.patch). Standard library only."""


def parse(v):
    core = v.lstrip("v").split("-")[0].split("+")[0]
    parts = [int(x) for x in core.split(".")]
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts[:3])


def compare(a, b):
    pa, pb = parse(a), parse(b)
    return (pa > pb) - (pa < pb)
