# 📄 Osdag LaTeX GUI – Section-Based PDF Generator

This is a **Python GUI application** built using **PyQt5** that helps users create **customized LaTeX reports** by selecting specific sections/subsections from a preloaded `.tex` file.

- Parses a predefined LaTeX `.tex` file
- Displays all `\section` and `\subsection` components
- Lets users select the sections/subsections to include
- Generates a new `.tex` file containing only the selected components
- Allows users to compile the new file into a PDF (e.g., using Overleaf or `pdflatex`)




---

✅ Built with **PyQt5** for an interactive GUI  
✅ Parses predefined `.tex` file (no upload required)  
✅ Lists all `\section` and `\subsection` headings  
✅ Supports selective content export  
✅ Generates a valid `.tex` file  
✅ Compatible with **Overleaf**


---

## 📦 Requirements

- **Python 3.8+**
- **MiKTeX** (with pdflatex in system PATH)
- Optional: PyQt5 for GUI (installed automatically below)

---

## 🛠️ Setup Instructions
```
 1. Clone the repo


git clone https://github.com/your-username/osdag-latex-gui.git

cd osdag-latex-gui

2. Install Python dependencies

pip install PyQt5
3. Install MiKTeX (if not installed)

Download and install from https://miktex.org/download

During setup, enable automatic package installation.

Ensure pdflatex is available in your system path:

pdflatex --version
📚 Required LaTeX Packages

Some LaTeX documents may require extra packages. You can install them using MiKTeX’s CLI:


mpm --install parskip
mpm --install kvoptions
mpm --install ltxcmds
mpm --install kvsetkeys
mpm --install geometry
mpm --install needspace
mpm --install multirow
mpm --install colortbl
mpm --install fancyhdr


🧠 How It Works
main.py: Launches the PyQt5 GUI.

latex_parser.py: Parses the .tex file for \section and \subsection tags.

generate_pdf.py: Generates a new .tex file and compiles it with pdflatex to produce a PDF.

📂 Folder Structure


📁 osdag-latex-gui/
├── main.py                # GUI logic
├── latex_parser.py        # Parses LaTeX into sections
├── generate_pdf.py        # PDF generation & LaTeX compilation
├── FOSSEE_SUMMER_...tex   # Sample LaTeX file


🧪 Example Usage
Run main.py:

python main.py
Select a .tex file (example provided).

A new `.tex` file is generated via `generate_pdf.py`
 User can compile the output `.tex` using Overleaf or MiKTeX to produce a clean, customized PDF
