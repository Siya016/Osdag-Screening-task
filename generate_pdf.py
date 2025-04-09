# # generate_pdf.py
# import subprocess
# import os
#
#
# class PDFGenerator:
#     @staticmethod
#     def generate_pdf(latex_content, output_dir="."):
#         try:
#             # Create output directory if it doesn't exist
#             os.makedirs(output_dir, exist_ok=True)
#
#             # Write the LaTeX content to a temporary file
#             tex_file = os.path.join(output_dir, "output.tex")
#             with open(tex_file, "w", encoding="utf-8") as f:
#                 f.write(latex_content)
#
#             # Run pdflatex twice to ensure proper generation of references
#             for _ in range(2):
#                 process = subprocess.run(
#                     ["pdflatex", "-interaction=nonstopmode", tex_file],
#                     cwd=output_dir,
#                     capture_output=True,
#                     text=True
#                 )
#
#                 if process.returncode != 0:
#                     raise Exception(f"PDFLaTeX Error: {process.stderr}")
#
#             # Check if PDF was created
#             pdf_path = os.path.join(output_dir, "output.pdf")
#             if os.path.exists(pdf_path):
#                 return True, pdf_path
#             else:
#                 raise Exception("PDF file was not created")
#
#         except Exception as e:
#             return False, str(e)


# import subprocess
# import os
#
#
# class PDFGenerator:
#     @staticmethod
#     def generate_pdf(latex_content, output_dir="."):
#         try:
#             # Ensure output directory exists
#             os.makedirs(output_dir, exist_ok=True)
#
#             # Write LaTeX content to file
#             tex_file = os.path.join(output_dir, "output.tex")
#             with open(tex_file, "w", encoding="utf-8") as f:
#                 f.write(latex_content)
#
#             # Run pdflatex twice (standard for references)
#             for _ in range(2):
#                 process = subprocess.run(
#                     ["pdflatex", "-interaction=nonstopmode", tex_file],
#                     cwd=output_dir,
#                     capture_output=True,
#                     text=True
#                 )
#
#                 if process.returncode != 0:
#                     error_message = f"""
# PDFLaTeX Error:
# --------------------
# STDOUT:
# {process.stdout}
#
# STDERR:
# {process.stderr}
# --------------------
# Please ensure all required LaTeX packages are installed (e.g., parskip, ltxcmds).
# Open MiKTeX Console and set 'Always install packages on-the-fly' to avoid this error.
#                     """.strip()
#                     raise Exception(error_message)
#
#             # Check for output.pdf
#             pdf_path = os.path.join(output_dir, "output.pdf")
#             if os.path.exists(pdf_path):
#                 return True, pdf_path
#             else:
#                 raise Exception("PDF file was not created.")
#
#         except Exception as e:
#             return False, str(e)

#

# import subprocess
# import os
#
# class PDFGenerator:
#     @staticmethod
#     def generate_pdf(latex_content, output_dir="."):
#         try:
#             # Ensure output directory exists
#             os.makedirs(output_dir, exist_ok=True)
#
#             # Write LaTeX content to file
#             tex_file = os.path.join(output_dir, "output.tex")
#             with open(tex_file, "w", encoding="utf-8") as f:
#                 f.write(latex_content)
#
#             # Run pdflatex twice (standard for references, images, tables, etc.)
#             for i in range(2):
#                 process = subprocess.run(
#                     ["pdflatex", "-interaction=nonstopmode", "output.tex"],
#                     cwd=output_dir,
#                     capture_output=True,
#                     text=True
#                 )
#
#                 if process.returncode != 0:
#                     # Print full stdout and stderr for debugging
#                     print("\n========== PDFLaTeX STDOUT ==========\n")
#                     print(process.stdout)
#                     print("\n========== PDFLaTeX STDERR ==========\n")
#                     print(process.stderr)
#
#                     # Raise detailed error
#                     raise Exception("PDFLaTeX compilation failed. Check the output above for more info.")
#
#             # Verify output
#             pdf_path = os.path.join(output_dir, "output.pdf")
#             if os.path.exists(pdf_path):
#                 print(f"[✅] PDF successfully generated at: {pdf_path}")
#                 return True, pdf_path
#             else:
#                 raise Exception("PDF file was not created.")
#
#         except Exception as e:
#             print("\n========== LaTeX Compilation Error ==========\n")
#             print(str(e))
#             return False, str(e)
#
#

#
# import subprocess
# import os
# import re
#
# class PDFGenerator:
#     @staticmethod
#     def replace_images_with_paths(tex_content):
#         # Replace \includegraphics with a framed box showing the path
#         pattern = r'\\includegraphics(?:\[[^\]]*\])?\{([^\}]+)\}'
#         return re.sub(pattern, r'\\fbox{\\parbox{4cm}{\\tiny\\texttt{\1}}}', tex_content)
#
#     @staticmethod
#     def generate_pdf(latex_content, output_dir="."):
#         try:
#             # Ensure output directory exists
#             os.makedirs(output_dir, exist_ok=True)
#
#             # Replace image commands with path as text
#             modified_content = PDFGenerator.replace_images_with_paths(latex_content)
#
#             # Write modified LaTeX content to file
#             tex_file = os.path.join(output_dir, "output.tex")
#             with open(tex_file, "w", encoding="utf-8") as f:
#                 f.write(modified_content)
#
#             # Run pdflatex twice (for references etc.)
#             for i in range(2):
#                 process = subprocess.run(
#                     ["pdflatex", "-interaction=nonstopmode", "output.tex"],
#                     cwd=output_dir,
#                     capture_output=True,
#                     text=True
#                 )
#
#                 if process.returncode != 0:
#                     print("\n========== PDFLaTeX STDOUT ==========\n")
#                     print(process.stdout)
#                     print("\n========== PDFLaTeX STDERR ==========\n")
#                     print(process.stderr)
#                     raise Exception("PDFLaTeX compilation failed. Check the output above for more info.")
#
#             # Verify output
#             pdf_path = os.path.join(output_dir, "output.pdf")
#             if os.path.exists(pdf_path):
#                 print(f"[✅] PDF successfully generated at: {pdf_path}")
#                 return True, pdf_path
#             else:
#                 raise Exception("PDF file was not created.")
#
#         except Exception as e:
#             print("\n========== LaTeX Compilation Error ==========\n")
#             print(str(e))
#             return False, str(e)

#
#


# import subprocess
# import os
# import re
#
# class PDFGenerator:
#     @staticmethod
#     def replace_images_with_paths(tex_content):
#         # Replace \includegraphics with a framed box showing the path
#         pattern = r'\\includegraphics(?:\[[^\]]*\])?\{([^\}]+)\}'
#         return re.sub(pattern, r'\\fbox{\\parbox{4cm}{\\tiny\\texttt{\1}}}', tex_content)
#
#     @staticmethod
#     def generate_pdf(latex_content, output_dir="."):
#         try:
#             # Ensure output directory exists
#             os.makedirs(output_dir, exist_ok=True)
#
#             # Replace image commands with path as text
#             modified_content = PDFGenerator.replace_images_with_paths(latex_content)
#
#             # Write modified LaTeX content to file
#             tex_file = os.path.join(output_dir, "output.tex")
#             with open(tex_file, "w", encoding="utf-8") as f:
#                 f.write(modified_content)
#
#             # Run pdflatex twice (for TOC/references)
#             for i in range(2):
#                 print(f"[{i+1}/2] Running pdflatex...")
#                 process = subprocess.run(
#                     "pdflatex -interaction=nonstopmode output.tex",
#                     cwd=output_dir,
#                     capture_output=True,
#                     text=True,
#                     shell=True  # Required on Windows
#                 )
#
#                 if process.returncode != 0:
#                     print("\n========== PDFLaTeX STDOUT ==========\n")
#                     print(process.stdout)
#                     print("\n========== PDFLaTeX STDERR ==========\n")
#                     print(process.stderr)
#                     raise Exception("PDFLaTeX compilation failed. Check the output above for more info.")
#
#             # Check if the PDF was created
#             pdf_path = os.path.join(output_dir, "output.pdf")
#             if os.path.exists(pdf_path):
#                 print(f"[✅] PDF successfully generated at: {pdf_path}")
#                 return True, pdf_path
#             else:
#                 raise Exception("PDF file was not created.")
#
#         except Exception as e:
#             print("\n========== LaTeX Compilation Error ==========\n")
#             print(str(e))
#             return False, str(e)


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


