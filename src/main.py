"""
===============================================================================
Sanchayam
Entry Point
===============================================================================
"""

from core.paths import PathManager


def main() -> None:
    """
    Application Entry Point
    """

    paths = PathManager()

    print("=========================================")
    print("Sanchayam")
    print("Personal Life Management System")
    print("=========================================")
    print()

    print("Application Root :", paths.application_root)
    print("Database Folder  :", paths.database_path)
    print("Logs Folder      :", paths.log_path)
    print("Exports Folder   :", paths.export_path)
    print("Backup Folder    :", paths.backup_path)

    print()
    print("Initialization Successful")


if __name__ == "__main__":
    main()