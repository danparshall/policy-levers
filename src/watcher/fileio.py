"""Atomic file writes shared by the state store and the digest writer.

A cron run killed mid-write must never leave a half-written file behind: write to
a temp file in the same directory, then `os.replace` it over the target, which is
atomic on POSIX for same-filesystem renames.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path


def atomic_write_text(path: str | Path, text: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=p.parent, prefix=f".{p.name}-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as tf:
            tf.write(text)
        os.replace(tmp_name, p)
    except BaseException:
        # Leave the target untouched; don't litter the directory with the temp file.
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
