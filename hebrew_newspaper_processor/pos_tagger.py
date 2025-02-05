import os
import stanza

class POSTagger:
    def __init__(self):
        self.nlp = stanza.Pipeline('he', processors='tokenize,pos')

    def tag_text(self, text):
        """Tag text with POS information."""
        doc = self.nlp(text)
        tagged_lines = []
        for sent in doc.sentences:
            for word in sent.words:
                pos = "PPOS" if word.upos == "PRON" else word.upos
                tagged_lines.append(f"{word.text} --> {pos}")
        return '\n'.join(tagged_lines)

    def process_file(self, input_path, output_dir='pos_tagged'):
        """Process text file and save POS tagged version."""
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f'{output_dir}/{base_name}_pos.txt'

        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        tagged_text = self.tag_text(text)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(tagged_text)

        return output_path
