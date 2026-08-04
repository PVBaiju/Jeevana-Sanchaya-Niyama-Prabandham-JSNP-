"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : database.py
Description    : Database Engine
===============================================================================
"""

from pathlib import Path

from sqlalchemy import create_engine

# -------------------------------------------------------------------------

ROOT_PATH = Path(__file__).resolve().parents[2]

DATABASE_FOLDER = ROOT_PATH / "database"

DATABASE_FOLDER.mkdir(parents=True, exist_ok=True)

DATABASE_FILE = DATABASE_FOLDER / "sanchayam.db"

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

# -------------------------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)
