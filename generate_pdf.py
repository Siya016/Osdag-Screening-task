


import subprocess
import os
import re

class PDFGenerator:
    @staticmethod
    def replace_images_with_paths(tex_content):
        # Optionally replace \includegraphics with text representation (if needed)
        pattern = r'\\includegraphics(?:\[[^\]]*\])?\{([^\}]+)\}'
        return re.sub(pattern, r'\\fbox{\\parbox{4cm}{\\tiny\\texttt{\1}}}', tex_content)

    @staticmethod
    def generate_pdf(latex_content, output_dir="."):
        try:
            os.makedirs(output_dir, exist_ok=True)

            # Write the raw LaTeX content directly to output.tex
            tex_file = os.path.join(output_dir, "output.tex")
            with open(tex_file, "w", encoding="utf-8") as f:
                f.write(latex_content)

            # Compile it using pdflatex
            for i in range(2):
                print(f"[{i+1}/2] Running pdflatex...")
                process = subprocess.run(
                    "pdflatex -interaction=nonstopmode output.tex",
                    cwd=output_dir,
                    capture_output=True,
                    text=True,
                    shell=True
                )

                if process.returncode != 0:
                    print("\n========== STDOUT ==========\n", process.stdout)
                    print("\n========== STDERR ==========\n", process.stderr)
                    raise Exception("PDFLaTeX failed")

            pdf_path = os.path.join(output_dir, "output.pdf")
            if os.path.exists(pdf_path):
                print(f"[✅] PDF generated at: {pdf_path}")
                return True, pdf_path
            else:
                raise Exception("PDF not created")

        except Exception as e:
            print("\n========== LaTeX Error ==========\n", str(e))
            return False, str(e)


