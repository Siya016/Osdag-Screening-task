


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

