from __future__ import annotations

import logging
from logging import Logger
from pathlib import Path


LOG_ROOT = Path(__file__).resolve().parent.parent / "logs"
LOG_ROOT.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(LOG_ROOT / "pcos.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger
