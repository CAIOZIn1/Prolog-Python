import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QTextEdit

class RecommenderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.pref_label = QLabel("Selecione suas preferências:", self)
        layout.addWidget(self.pref_label)

        self.pref_combobox = QComboBox(self)
        self.pref_combobox.addItems(["Backend", "Frontend", "Mobile", "Data Science"])
        layout.addWidget(self.pref_combobox)

        self.result_label = QLabel("Recomendações:", self)
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit(self)
        layout.addWidget(self.result_text)

        self.recommend_button = QPushButton("Recomendar", self)
        self.recommend_button.clicked.connect(self.get_recommendations)
        layout.addWidget(self.recommend_button)

        self.setLayout(layout)
        self.setWindowTitle('Recomendador de Tecnologias')
        self.show()

    def get_recommendations(self):
        preference = self.pref_combobox.currentText()
        recommendations = self.query_prolog(preference)
        self.result_text.setText("\n".join(recommendations))

    def query_prolog(self, preference):
        if preference == "Backend":
            return ["Python", "Java", "Node.js"]
        elif preference == "Frontend":
            return ["JavaScript", "React", "Angular"]
        elif preference == "Mobile":
            return ["Flutter", "React Native", "Swift"]
        elif preference == "Data Science":
            return ["Python", "R", "Julia"]
        else:
            return []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecommenderApp()
    sys.exit(app.exec_())
