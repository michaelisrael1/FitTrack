from PyQt6.QtWidgets import QApplication
from logic import *


def main() -> None:
    """
    Main function to run the FitTrack application.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
