from typing import Iterable, List, Tuple
import os

# A conservative set of bytes considered "text" (ASCII printable + common whitespace)
_TEXT_BYTES = bytes(range(32, 127)) + b"\n\r\t\f\v"


def is_text_file(path: str, blocksize: int = 8192, nontext_threshold: float = 0.30) -> bool:
    """Return True if *path* looks like a text file.

    Heuristic used:
    - Non-existent or directories -> False
    - Empty files -> True
    - If the sample contains a NUL byte -> False (very likely binary)
    - Count control characters (bytes < 32) excluding common whitespace; if their
      fraction exceeds *nontext_threshold* the file is treated as binary.

    This approach is pragmatic and matches common editor heuristics for distinguishing
    text vs binary files.
    """
    if not os.path.exists(path) or os.path.isdir(path):
        return False

    try:
        with open(path, "rb") as f:
            sample = f.read(blocksize)
    except Exception:
        return False

    if not sample:
        return True

    if b"\x00" in sample:
        return False

    # Count bytes that are control characters (0-31) except common whitespace
    ctrl_count = 0
    for b in sample:
        if b < 32 and b not in (9, 10, 13):
            ctrl_count += 1

    ratio = ctrl_count / len(sample)
    return ratio <= nontext_threshold


def filter_text_files(paths: Iterable[str]) -> Tuple[List[str], List[str]]:
    """Given an iterable of paths, return (accepted, rejected).

    - accepted: list of paths that are likely text files
    - rejected: list of paths that are not text files or could not be opened
    """
    accepted: List[str] = []
    rejected: List[str] = []

    for p in paths:
        if is_text_file(p):
            accepted.append(p)
        else:
            rejected.append(p)

    return accepted, rejected
