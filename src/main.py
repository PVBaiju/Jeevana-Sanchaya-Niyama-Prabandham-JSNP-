"""
===============================================================================
Project        : Sanchayam
Project Code   : JSNP
File           : main.py
Description    : Application Entry Point
===============================================================================
"""

import sys

from app.application import SanchayamApplication


def main() -> int:
    """
    Application Entry Point.
    """

    application = SanchayamApplication()

    return application.run()


if __name__ == "__main__":
    sys.exit(main())