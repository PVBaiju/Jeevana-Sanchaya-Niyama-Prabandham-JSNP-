"""
===============================================================================
Project        : Sanchayam
Module         : Configuration Manager

Loads YAML configuration files.

===============================================================================
"""

from pathlib import Path
import yaml

from core.constants import CONFIG_FOLDER


class ConfigManager:
    """
    Reads application configuration.
    """

    def __init__(self):

        self.config_file = CONFIG_FOLDER / "settings.yaml"

        self.user_config = CONFIG_FOLDER / "user_settings.yaml"

        self.settings = {}

        self.user_settings = {}

        self.load()

    # ------------------------------------------------------------------

    def load(self):

        if self.config_file.exists():

            with open(self.config_file, "r", encoding="utf-8") as file:

                self.settings = yaml.safe_load(file)

        if self.user_config.exists():

            with open(self.user_config, "r", encoding="utf-8") as file:

                self.user_settings = yaml.safe_load(file)

    # ------------------------------------------------------------------

    def get(self, section, key=None, default=None):

        data = self.settings.get(section, {})

        if key is None:
            return data

        return data.get(key, default)

    # ------------------------------------------------------------------

    def get_user(self, key, default=None):

        return self.user_settings.get(key, default)