"""
===============================================================================
Project        : Sanchayam
Module         : Logger
Description    : Centralized Logging System

Creates application logs.

===============================================================================
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from core.constants import (
    LOG_FILE_NAME,
    LOG_LEVEL,
)
from core.paths import PathManager


class LoggerManager:
    """
    Centralized logger for the application.
    """

    _logger = None

    @classmethod
    def get_logger(cls) -> logging.Logger:
        """
        Returns a singleton logger instance.
        """

        if cls._logger is not None:
            return cls._logger

        paths = PathManager()

        log_file: Path = paths.log_path / LOG_FILE_NAME

        logger = logging.getLogger("Sanchayam")

        logger.setLevel(getattr(logging, LOG_LEVEL.upper()))

        if not logger.handlers:

            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)-8s | %(module)s | %(message)s",
                datefmt="%d-%m-%Y %H:%M:%S",
            )

            file_handler = RotatingFileHandler(
                log_file,
                maxBytes=5 * 1024 * 1024,
                backupCount=5,
                encoding="utf-8",
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        cls._logger = logger

        return logger