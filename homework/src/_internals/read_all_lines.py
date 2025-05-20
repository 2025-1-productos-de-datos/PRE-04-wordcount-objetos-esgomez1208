import os


class ReadAllLinesMixin:

    def read_all_lines(self):

        lines = []
        for filename in os.listdir(self.input_folder):
            filepath = os.path.join(self.input_folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                lines.extend(f.readlines())

        self.lines = lines
