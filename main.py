# import sys
# import os
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
#                              QCheckBox, QPushButton, QScrollArea, QMessageBox)
# from PyQt5.QtCore import Qt
# import subprocess
# from latex_parser import LatexParser
# from generate_pdf import PDFGenerator
#
#
# class LatexSelectorApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.parser = LatexParser()
#         self.components = []
#         self.checkboxes = []
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('LaTeX Component Selector')
#         self.setGeometry(100, 100, 800, 600)
#
#         # Create central widget and layout
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout(central_widget)
#
#         # Create scroll area for components
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll_content = QWidget()
#         self.scroll_layout = QVBoxLayout(scroll_content)
#
#         # Load and parse the TEX file
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         tex_file = os.path.join(current_dir, "FOSSEE_SUMMER_FELLOWSHIP_SAMPLE_TEX (1).tex")
#         self.components = self.parser.parse_file(tex_file)
#
#         # Create checkboxes for components
#         for component in self.components:
#             prefix = "    " * (component['level'] - 1)
#             checkbox = QCheckBox(f"{prefix}{component['type']}: {component['title']}")
#             self.checkboxes.append((checkbox, component))
#             self.scroll_layout.addWidget(checkbox)
#
#         # Add stretch to push checkboxes to the top
#         self.scroll_layout.addStretch()
#
#         # Set up scroll area
#         scroll.setWidget(scroll_content)
#         layout.addWidget(scroll)
#
#         # Add Generate PDF button
#         generate_btn = QPushButton('Generate PDF')
#         generate_btn.clicked.connect(self.generate_pdf)
#         layout.addWidget(generate_btn)
#
#     def generate_pdf(self):
#         # Get selected components
#         selected_components = [
#             component['title'] for checkbox, component in self.checkboxes
#             if checkbox.isChecked()
#         ]
#
#         if not selected_components:
#             QMessageBox.warning(self, 'Warning', 'Please select at least one component!')
#             return
#
#         # Generate LaTeX content
#         latex_content = self.parser.generate_latex(selected_components)
#
#         # Generate PDF
#         success, result = PDFGenerator.generate_pdf(latex_content)
#
#         if success:
#             msg = QMessageBox.information(
#                 self,
#                 'Success',
#                 'PDF generated successfully! Would you like to open it?',
#                 QMessageBox.Yes | QMessageBox.No
#             )
#
#             if msg == QMessageBox.Yes:
#                 # Open PDF with default viewer
#                 if sys.platform == 'win32':
#                     os.startfile(result)
#                 else:
#                     subprocess.run(['xdg-open', result])
#         else:
#             QMessageBox.critical(self, 'Error', f'Failed to generate PDF: {result}')
#
#
# def main():
#     app = QApplication(sys.argv)
#     ex = LatexSelectorApp()
#     ex.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QCheckBox, QPushButton, QScrollArea, QMessageBox)
from PyQt5.QtCore import Qt
import subprocess
from latex_parser import LatexParser
from generate_pdf import PDFGenerator


class LatexSelectorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.parser = LatexParser()
        self.components = []
        self.checkboxes = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LaTeX Component Selector')
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create scroll area for components
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)

        # Load and parse the TEX file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        tex_file = os.path.join(current_dir, "FOSSEE_SUMMER_FELLOWSHIP_SAMPLE_TEX (1).tex")
        self.components = self.parser.parse_file(tex_file)

        # Create checkboxes for components
        for component in self.components:
            prefix = "    " * (component['level'] - 1)
            checkbox = QCheckBox(f"{prefix}{component['type']}: {component['title']}")
            self.checkboxes.append((checkbox, component))
            self.scroll_layout.addWidget(checkbox)

        self.scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)

        # Add Generate PDF button
        generate_btn = QPushButton('Generate PDF')
        generate_btn.clicked.connect(self.generate_pdf)
        layout.addWidget(generate_btn)

    def generate_pdf(self):
        # Get selected components
        selected_components = [
            component['title'] for checkbox, component in self.checkboxes
            if checkbox.isChecked()
        ]

        if not selected_components:
            QMessageBox.warning(self, 'Warning', 'Please select at least one component!')
            return

        # Generate LaTeX content
        latex_content = self.parser.generate_latex(selected_components)

        # Generate PDF
        success, result = PDFGenerator.generate_pdf(latex_content)

        if success:
            msg = QMessageBox.information(
                self,
                'Success',
                'PDF generated successfully! Would you like to open it?',
                QMessageBox.Yes | QMessageBox.No
            )

            if msg == QMessageBox.Yes:
                self.open_pdf(result)
        else:
            QMessageBox.critical(self, 'Error', f'Failed to generate PDF:\n\n{result}')

    def open_pdf(self, path):
        try:
            if sys.platform.startswith('win'):
                os.startfile(path)
            elif sys.platform.startswith('darwin'):
                subprocess.run(['open', path])
            else:
                subprocess.run(['xdg-open', path])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not open PDF: {str(e)}")


def main():
    app = QApplication(sys.argv)
    window = LatexSelectorApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
