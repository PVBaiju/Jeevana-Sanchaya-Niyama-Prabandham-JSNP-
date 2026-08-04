"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
Author         : Baiju Nair
Description    : Application Constants

This module contains all application-wide constant values.
No hardcoded values should be used anywhere else in the application.

Copyright (c) 2026
===============================================================================
"""

from pathlib import Path

# =============================================================================
# APPLICATION INFORMATION
# =============================================================================

APP_NAME: str = "Sanchayam"

PROJECT_CODE: str = "JSNP"

APP_FULL_NAME: str = "Sanchayam - Personal Life Management System"

VERSION: str = "0.1.0"

VERSION_NAME: str = "Alpha"

AUTHOR: str = "Baiju Nair"

COMPANY: str = "VisionBoard"

COPYRIGHT: str = "© 2026 VisionBoard"

# =============================================================================
# WINDOW SETTINGS
# =============================================================================

WINDOW_WIDTH: int = 1400

WINDOW_HEIGHT: int = 850

MIN_WINDOW_WIDTH: int = 1200

MIN_WINDOW_HEIGHT: int = 700

# =============================================================================
# DATE & TIME
# =============================================================================

DATE_FORMAT: str = "%d-%m-%Y"

TIME_FORMAT: str = "%H:%M"

DATETIME_FORMAT: str = "%d-%m-%Y %H:%M:%S"

# =============================================================================
# DATABASE
# =============================================================================

DATABASE_NAME: str = "sanchayam.db"

DATABASE_VERSION: int = 1

# =============================================================================
# LOGGING
# =============================================================================

LOG_FILE_NAME: str = "sanchayam.log"

LOG_LEVEL: str = "INFO"

# =============================================================================
# REPORTS
# =============================================================================

REPORT_FOLDER: str = "exports"

BACKUP_FOLDER: str = "backups"

# =============================================================================
# APPLICATION DIRECTORIES
# =============================================================================

ROOT_FOLDER = Path(__file__).resolve().parents[2]

SRC_FOLDER = ROOT_FOLDER / "src"

DATABASE_FOLDER = ROOT_FOLDER / "database"

LOG_FOLDER = ROOT_FOLDER / "logs"

EXPORT_FOLDER = ROOT_FOLDER / "exports"

BACKUP_FOLDER_PATH = ROOT_FOLDER / "backups"

ASSETS_FOLDER = ROOT_FOLDER / "assets"

DOCS_FOLDER = ROOT_FOLDER / "docs"

TEST_FOLDER = ROOT_FOLDER / "tests"

CONFIG_FOLDER = SRC_FOLDER / "config"

RESOURCE_FOLDER = SRC_FOLDER / "resources"

# =============================================================================
# DEFAULT UI
# =============================================================================

DEFAULT_THEME: str = "Light"

DEFAULT_FONT: str = "Segoe UI"

DEFAULT_FONT_SIZE: int = 10

# =============================================================================
# APPLICATION STATUS
# =============================================================================

STATUS_READY = "Ready"

STATUS_LOADING = "Loading..."

STATUS_ERROR = "Error"

STATUS_SUCCESS = "Success"

STATUS_WARNING = "Warning"

# =============================================================================
# FUTURE FEATURES (Reserved)
# =============================================================================

ENABLE_AI = False

ENABLE_VOICE_ASSISTANT = False

ENABLE_CLOUD_SYNC = False

ENABLE_MULTI_USER = False

ENABLE_FARM_MODULE = False