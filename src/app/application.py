"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : application.py
Description    : Application Bootstrap

Initializes the core components of the application.

===============================================================================
"""

from core.paths import PathManager
from core.logger import LoggerManager
from config.config_manager import ConfigManager


class SanchayamApplication:
    """
    Main Application Bootstrap Class.
    """

    def __init__(self) -> None:

        self.paths = None
        self.logger = None
        self.config = None

    # ---------------------------------------------------------------------

    def initialize(self) -> None:
        """
        Initialize application components.
        """

        # Initialize folders
        self.paths = PathManager()

        # Initialize logger
        self.logger = LoggerManager.get_logger()

        self.logger.info("=" * 70)
        self.logger.info("Starting Sanchayam...")
        self.logger.info("=" * 70)

        # Load configuration
        self.config = ConfigManager()

        self.logger.info("Configuration Loaded Successfully")

    # ---------------------------------------------------------------------

    def show_startup_information(self) -> None:
        """
        Display startup information.
        """

        print("\n" + "=" * 70)
        print("Sanchayam")
        print("Personal Life Management System")
        print("=" * 70)

        print(f"Application Root : {self.paths.application_root}")
        print(f"Database Folder  : {self.paths.database_path}")
        print(f"Logs Folder      : {self.paths.log_path}")
        print(f"Exports Folder   : {self.paths.export_path}")
        print(f"Backup Folder    : {self.paths.backup_path}")

        print()

        print(f"Application Name : {self.config.get('application', 'name')}")
        print(f"Version          : {self.config.get('application', 'version')}")
        print(f"Database         : {self.config.get('database', 'type')}")
        print(f"Theme            : {self.config.get('ui', 'theme')}")

    # ---------------------------------------------------------------------

    def run(self) -> int:
        """
        Start the application.
        """

        self.initialize()

        self.show_startup_information()

        self.logger.info("Application Initialized Successfully")

        print("\nApplication Started Successfully.")

        return 0