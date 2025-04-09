# # latex_parser.py
# import re
#
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Extract sections and subsections with their content
#             section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section|\\end\{document\})'
#             subsection_pattern = r'\\subsection\{([^}]+)\}(.*?)(?=\\subsection|\\section|\\end\{document\})'
#
#             # Find all sections
#             sections = re.finditer(section_pattern, content, re.DOTALL)
#             for section in sections:
#                 section_title = section.group(1)
#                 section_content = section.group(2)
#
#                 # Store section information
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title,
#                     'content': section.group(0),
#                     'level': 1
#                 })
#
#                 # Find subsections within this section
#                 subsections = re.finditer(subsection_pattern, section_content, re.DOTALL)
#                 for subsection in subsections:
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': subsection.group(1),
#                         'content': subsection.group(0),
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_components):
#         # Basic LaTeX document structure
#         latex_content = [
#             r"\documentclass{article}",
#             r"\usepackage[T1]{fontenc}",
#             r"\usepackage[utf8]{inputenc}",
#             r"\usepackage{lmodern}",
#             r"\usepackage{textcomp}",
#             r"\usepackage{lastpage}",
#             r"\usepackage{parskip}",
#             r"\usepackage[top=5cm,hmargin=2cm,headheight=100pt,footskip=100pt,bottom=5cm]{geometry}",
#             r"\usepackage{amsmath}",
#             r"\usepackage{graphicx}",
#             r"\usepackage{needspace}",
#             r"\usepackage{color}",
#             r"\usepackage{longtable}",
#             r"\usepackage{tabularx}",
#             r"\usepackage{multirow}",
#             r"\usepackage[table]{xcolor}",
#             r"\usepackage{xcolor}",
#             r"\usepackage{fancyhdr}",
#             r"\begin{document}"
#         ]
#
#         # Add selected components
#         for component in self.components:
#             if component['title'] in selected_components:
#                 latex_content.append(component['content'])
#
#         latex_content.append(r"\end{document}")
#         return "\n".join(latex_content)


# latex_parser.py
# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix image paths: convert absolute paths to just filenames
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             # Extract sections and subsections with their content
#             section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section|\\end\{document\})'
#             subsection_pattern = r'\\subsection\{([^}]+)\}(.*?)(?=\\subsection|\\section|\\end\{document\})'
#
#             # Find all sections
#             sections = re.finditer(section_pattern, content, re.DOTALL)
#             for section in sections:
#                 section_title = section.group(1)
#                 section_content = section.group(2)
#
#                 # Store section information
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title,
#                     'content': section.group(0),
#                     'level': 1
#                 })
#
#                 # Find subsections within this section
#                 subsections = re.finditer(subsection_pattern, section_content, re.DOTALL)
#                 for subsection in subsections:
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': subsection.group(1),
#                         'content': subsection.group(0),
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_components):
#         # Basic LaTeX document structure with color fixes
#         latex_content = [
#             r"\documentclass{article}",
#             r"\usepackage[T1]{fontenc}",
#             r"\usepackage[utf8]{inputenc}",
#             r"\usepackage{lmodern}",
#             r"\usepackage{textcomp}",
#             r"\usepackage{lastpage}",
#             r"\usepackage{parskip}",
#             r"\usepackage[top=5cm,hmargin=2cm,headheight=100pt,footskip=100pt,bottom=5cm]{geometry}",
#             r"\usepackage{amsmath}",
#             r"\usepackage{graphicx}",
#             r"\usepackage{needspace}",
#             r"\usepackage{color}",
#             r"\usepackage{longtable}",
#             r"\usepackage{tabularx}",
#             r"\usepackage{multirow}",
#             r"\usepackage[table]{xcolor}",
#             r"\usepackage{xcolor}",
#             r"\definecolor{OsdagGreen}{RGB}{0, 128, 0}",
#             r"\definecolor{Red}{RGB}{255, 0, 0}",
#             r"\usepackage{fancyhdr}",
#             r"\begin{document}"
#         ]
#
#         # Add selected components
#         for component in self.components:
#             if component['title'] in selected_components:
#                 latex_content.append(component['content'])
#
#         latex_content.append(r"\end{document}")
#         return "\n".join(latex_content)


# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix image paths: convert absolute paths to just filenames
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             self.original_content = content  # Save for generate_latex()
#
#             # Extract sections and subsections with their content
#             section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section\{|\\end\{document\})'
#             subsection_pattern = r'\\subsection\{([^}]+)\}(.*?)(?=\\subsection\{|\\section\{|\\end\{document\})'
#
#             # Find all sections
#             sections = re.finditer(section_pattern, content, re.DOTALL)
#             for section in sections:
#                 section_title = section.group(1)
#                 section_content = section.group(0)
#
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title.strip(),
#                     'content': section_content,
#                     'level': 1
#                 })
#
#                 # Find subsections within this section
#                 subsections = re.finditer(subsection_pattern, section.group(2), re.DOTALL)
#                 for subsection in subsections:
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': subsection.group(1).strip(),
#                         'content': subsection.group(0),
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_components):
#         try:
#             # Extract preamble and postamble from the original content
#             preamble_match = re.search(r'^(.*?)\\begin\{document\}', self.original_content, re.DOTALL)
#             postamble_match = re.search(r'\\end\{document\}(.*)$', self.original_content, re.DOTALL)
#
#             preamble = preamble_match.group(1) if preamble_match else ''
#             postamble = postamble_match.group(1) if postamble_match else ''
#
#             # Begin building final LaTeX document
#             latex_content = [preamble + r'\begin{document}']
#
#             for component in self.components:
#                 if component['title'] in selected_components:
#                     latex_content.append(component['content'])
#
#             latex_content.append(r'\end{document}' + postamble)
#             return "\n".join(latex_content)
#
#         except Exception as e:
#             print(f"Error generating LaTeX: {str(e)}")
#             return ""



# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#         self.original_content = ""
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix image paths: convert absolute to relative
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             self.original_content = content
#
#             # Extract sections
#             section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section\{|\\end\{document\})'
#             subsection_pattern = r'\\subsection\{([^}]+)\}(.*?)(?=\\subsection\{|\\section\{|\\end\{document\})'
#
#             sections = re.finditer(section_pattern, content, re.DOTALL)
#             for section in sections:
#                 section_title = section.group(1).strip()
#                 section_content = section.group(0).strip()
#
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title,
#                     'content': section_content,
#                     'level': 1
#                 })
#
#                 # Extract subsections inside this section
#                 subsections = re.finditer(subsection_pattern, section.group(2), re.DOTALL)
#                 for subsection in subsections:
#                     subsection_title = subsection.group(1).strip()
#                     subsection_content = subsection.group(0).strip()
#
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': subsection_title,
#                         'content': subsection_content,
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"❌ Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_components):
#         try:
#             preamble_match = re.search(r'^(.*?)\\begin\{document\}', self.original_content, re.DOTALL)
#             postamble_match = re.search(r'\\end\{document\}(.*)$', self.original_content, re.DOTALL)
#
#             preamble = preamble_match.group(1) if preamble_match else ''
#             postamble = postamble_match.group(1) if postamble_match else ''
#
#             latex_content = [preamble + '\n\\begin{document}\n']
#
#             for component in self.components:
#                 if component['title'] in selected_components:
#                     latex_content.append(component['content'])
#
#             latex_content.append('\n\\end{document}' + postamble)
#             return "\n".join(latex_content)
#
#         except Exception as e:
#             print(f"❌ Error generating LaTeX: {str(e)}")
#             return ""


# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#         self.original_content = ""
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix image paths (Windows absolute to relative)
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             self.original_content = content
#
#             self.components.clear()
#
#             # Extract sections linearly
#             section_split = re.split(r'(\\section\{[^}]+\})', content)
#             for i in range(1, len(section_split), 2):  # Skip preamble
#                 section_header = section_split[i]
#                 section_body = section_split[i + 1] if i + 1 < len(section_split) else ''
#                 section_title = re.findall(r'\\section\{([^}]+)\}', section_header)[0]
#
#                 full_section = section_header + section_body
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title,
#                     'content': full_section.strip(),
#                     'level': 1
#                 })
#
#                 # Find subsections inside this section only once
#                 subsections = re.finditer(
#                     r'(\\subsection\{([^}]+)\}(.*?))(?=\\subsection\{|\\section\{|\\end\{document\})',
#                     section_body,
#                     re.DOTALL
#                 )
#                 for match in subsections:
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': match.group(2).strip(),
#                         'content': match.group(1).strip(),
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"❌ Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_components):
#         try:
#             preamble_match = re.search(r'^(.*?)\\begin\{document\}', self.original_content, re.DOTALL)
#             postamble_match = re.search(r'\\end\{document\}(.*)$', self.original_content, re.DOTALL)
#
#             preamble = preamble_match.group(1) if preamble_match else ''
#             postamble = postamble_match.group(1) if postamble_match else ''
#
#             latex_content = [preamble + '\n\\begin{document}\n']
#
#             for component in self.components:
#                 if component['title'] in selected_components:
#                     latex_content.append(component['content'])
#
#             latex_content.append('\n\\end{document}' + postamble)
#             return "\n".join(latex_content)
#
#         except Exception as e:
#             print(f"❌ Error generating LaTeX: {str(e)}")
#             return ""


# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#         self.original_content = ""
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix image paths (Windows absolute to relative)
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             self.original_content = content
#
#             self.components.clear()
#
#             # Extract sections linearly
#             section_split = re.split(r'(\\section\{[^}]+\})', content)
#             for i in range(1, len(section_split), 2):  # Skip preamble
#                 section_header = section_split[i]
#                 section_body = section_split[i + 1] if i + 1 < len(section_split) else ''
#                 section_title = re.findall(r'\\section\{([^}]+)\}', section_header)[0]
#
#                 full_section = section_header + section_body
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title,
#                     'content': full_section.strip(),
#                     'level': 1
#                 })
#
#                 # Find subsections inside this section only once
#                 subsections = re.finditer(
#                     r'(\\subsection\{([^}]+)\}(.*?))(?=\\subsection\{|\\section\{|\\end\{document\})',
#                     section_body,
#                     re.DOTALL
#                 )
#                 for match in subsections:
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': match.group(2).strip(),
#                         'content': match.group(1).strip(),
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"\u274c Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_components):
#         try:
#             preamble_match = re.search(r'^(.*?)\\begin\{document\}', self.original_content, re.DOTALL)
#             postamble_match = re.search(r'\\end\{document\}(.*)$', self.original_content, re.DOTALL)
#
#             preamble = preamble_match.group(1) if preamble_match else ''
#             postamble = postamble_match.group(1) if postamble_match else ''
#
#             latex_content = [preamble + '\n\\begin{document}\n']
#
#             # Track selected sections
#             selected_sections = {
#                 component['title']
#                 for component in self.components
#                 if component['title'] in selected_components and component['level'] == 1
#             }
#
#             for component in self.components:
#                 if component['title'] not in selected_components:
#                     continue
#
#                 # Skip subsection if it's already part of a selected section
#                 if component['level'] == 2:
#                     for parent in self.components:
#                         if parent['level'] == 1 and parent['title'] in selected_sections:
#                             if component['content'] in parent['content']:
#                                 break
#                     else:
#                         latex_content.append(component['content'])
#                 else:
#                     latex_content.append(component['content'])
#
#             latex_content.append('\n\\end{document}' + postamble)
#             return "\n".join(latex_content)
#
#         except Exception as e:
#             print(f"\u274c Error generating LaTeX: {str(e)}")
#             return ""



# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#         self.original_content = ""
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix image paths
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             self.original_content = content
#
#             section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section\{|\\end\{document\})'
#             subsection_pattern = r'\\subsection\{([^}]+)\}(.*?)(?=\\subsection\{|\\section\{|\\end\{document\})'
#
#             sections = re.finditer(section_pattern, content, re.DOTALL)
#
#             for section in sections:
#                 section_title = section.group(1).strip()
#                 section_body = section.group(2)
#
#                 # Add section without subsections
#                 body_without_subsections = re.sub(subsection_pattern, '', section_body, flags=re.DOTALL)
#                 section_content = f"\\section{{{section_title}}}{body_without_subsections}"
#
#                 self.components.append({
#                     'type': 'section',
#                     'title': section_title,
#                     'content': section_content,
#                     'level': 1
#                 })
#
#                 # Add subsections separately
#                 subsections = re.finditer(subsection_pattern, section_body, re.DOTALL)
#                 for subsection in subsections:
#                     subsection_title = subsection.group(1).strip()
#                     subsection_content = f"\\subsection{{{subsection_title}}}{subsection.group(2)}"
#
#                     self.components.append({
#                         'type': 'subsection',
#                         'title': subsection_title,
#                         'content': subsection_content,
#                         'level': 2
#                     })
#
#             return self.components
#
#         except Exception as e:
#             print(f"Error parsing LaTeX file: {str(e)}")
#             return []
#
#     def generate_latex(self, selected_titles):
#         try:
#             preamble_match = re.search(r'^(.*?)\\begin\{document\}', self.original_content, re.DOTALL)
#             postamble_match = re.search(r'\\end\{document\}(.*)$', self.original_content, re.DOTALL)
#
#             preamble = preamble_match.group(1) if preamble_match else ''
#             postamble = postamble_match.group(1) if postamble_match else ''
#
#             latex_content = [preamble + r'\begin{document}']
#
#             for component in self.components:
#                 if component['title'] in selected_titles:
#                     latex_content.append(component['content'])
#
#             latex_content.append(r'\end{document}' + postamble)
#             return "\n".join(latex_content)
#
#         except Exception as e:
#             print(f"Error generating LaTeX: {str(e)}")
#             return ""


# import re
#
# class LatexParser:
#     def __init__(self):
#         self.components = []
#
#     def parse_file(self, file_path):
#         try:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 content = file.read()
#
#             # Fix absolute paths in \includegraphics
#             content = re.sub(
#                 r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
#                 r'\\includegraphics[\1]{\2}',
#                 content
#             )
#
#             self.original_content = content
#
#             self.components = []
#             self._extract_components()
#
#             return self.components
#
#         except Exception as e:
#             print(f"[Error] Parsing LaTeX file: {str(e)}")
#             return []
#
#     def _extract_components(self):
#         section_pattern = r'(\\section\{([^}]+)\})(.*?)(?=(\\section|\\end\{document\}))'
#         matches = re.finditer(section_pattern, self.original_content, re.DOTALL)
#
#         for match in matches:
#             full_section = match.group(1) + match.group(3)
#             section_title = match.group(2).strip()
#
#             self.components.append({
#                 'type': 'section',
#                 'title': section_title,
#                 'content': full_section,
#                 'level': 1
#             })
#
#             # Now check for subsections within this section
#             subsection_pattern = r'(\\subsection\{([^}]+)\})(.*?)(?=(\\subsection|\\section|\\end\{document\}))'
#             subsection_matches = re.finditer(subsection_pattern, match.group(3), re.DOTALL)
#             for sm in subsection_matches:
#                 full_sub = sm.group(1) + sm.group(3)
#                 sub_title = sm.group(2).strip()
#
#                 self.components.append({
#                     'type': 'subsection',
#                     'title': sub_title,
#                     'content': full_sub,
#                     'level': 2
#                 })
#
#     def generate_latex(self, selected_titles):
#         try:
#             # Extract preamble and postamble
#             preamble = re.search(r'^(.*?)\\begin\{document\}', self.original_content, re.DOTALL).group(1)
#             postamble = re.search(r'\\end\{document\}(.*)$', self.original_content, re.DOTALL)
#             postamble = postamble.group(1) if postamble else ""
#
#             content_parts = []
#             for component in self.components:
#                 if component['title'] in selected_titles:
#                     content_parts.append(component['content'])
#
#             return preamble + r'\begin{document}' + "\n".join(content_parts) + r'\end{document}' + postamble
#
#         except Exception as e:
#             print(f"[Error] Generating LaTeX: {str(e)}")
#             return ""



import re

class LatexParser:
    def __init__(self):
        self.components = []
        self.full_content = ""

    def parse_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Fix image paths: convert absolute paths to just filenames
            content = re.sub(
                r'\\includegraphics\[([^\]]+)\]\{[A-Z]:[^\\}]+\\([^\\}]+)\}',
                r'\\includegraphics[\1]{\2}',
                content
            )

            self.full_content = content  # Save full content for generate_latex

            self.components = []

            # Find all section and subsection positions
            pattern = re.compile(
                r'(?P<type>\\section|\\subsection)\{(?P<title>[^\}]+)\}',
                re.DOTALL
            )

            matches = list(pattern.finditer(content))

            for i, match in enumerate(matches):
                component_type = match.group('type').lstrip('\\')
                title = match.group('title').strip()
                level = 1 if component_type == 'section' else 2
                start = match.start()

                self.components.append({
                    'type': component_type,
                    'title': title,
                    'level': level,
                    'start': start
                })

            return self.components

        except Exception as e:
            print(f"Error parsing LaTeX file: {str(e)}")
            return []

    def generate_latex(self, selected_titles):
        selected_set = set(selected_titles)

        blocks = []
        for i, comp in enumerate(self.components):
            if comp['title'] not in selected_set:
                continue

            start_idx = comp['start']
            end_idx = self.components[i + 1]['start'] if i + 1 < len(self.components) else len(self.full_content)
            blocks.append(self.full_content[start_idx:end_idx].strip())

        # Extract preamble and postamble
        preamble_match = re.search(r"(.*?\\begin\{document\})", self.full_content, re.DOTALL)
        postamble_match = re.search(r"(\\end\{document\}.*)", self.full_content, re.DOTALL)

        preamble = preamble_match.group(1) if preamble_match else r"\documentclass{article}\begin{document}"
        postamble = postamble_match.group(1) if postamble_match else r"\end{document}"

        joined_blocks = '\n\n'.join(blocks)
        return f"{preamble}\n\n{joined_blocks}\n\n{postamble}"

