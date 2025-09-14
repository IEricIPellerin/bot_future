# main.py — PySide6, 2 zones minimalistes (haut/bas)
# Dépendances : pip install PySide6

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFrame, QLabel
)

class fenetre_princpale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kucoin bot - Crypto trading")
        self.resize(900, 600)

        # --- Zone centrale + layout vertical ---
        central = QWidget(self)
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(8)

        # --- Zone du haut (placeholder pour le tableau de paires) ---
        self.frame_paires = QFrame(self, objectName="frame_paires")
        self.frame_paires.setFrameShape(QFrame.StyledPanel)
        self.frame_paires.setFrameShadow(QFrame.Raised)

        # Un petit label indicatif (à retirer plus tard)
        lbl_top = QLabel("Zone Paires (tableau à venir)", self.frame_paires)
        lbl_top.setAlignment(Qt.AlignCenter)

        # --- Zone du bas (placeholder pour les logs) ---
        self.frame_logs = QFrame(self, objectName="frame_logs")
        self.frame_logs.setFrameShape(QFrame.StyledPanel)
        self.frame_logs.setFrameShadow(QFrame.Raised)

        lbl_bot = QLabel("Zone Logs (console à venir)", self.frame_logs)
        lbl_bot.setAlignment(Qt.AlignCenter)

        # --- Ajout au layout + ratio d’espace ---
        root.addWidget(self.frame_paires)
        root.addWidget(self.frame_logs)
        root.setStretch(0, 3)  # haut: 3 parts
        root.setStretch(1, 2)  # bas : 2 parts

def main():
    # (optionnel) HighDPI avant la création de l'app
    try:
        QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )
    except Exception:
        pass

    app = QApplication(sys.argv)
    w = fenetre_princpale()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
