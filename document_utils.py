import re
import logging

def save_outline(outline, filename):
    with open(filename, 'w') as f:
        f.write(outline)
    logging.info(f"Outline saved to {filename}")

def parse_outline(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        sections = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
        logging.info(f"Parsed {len(sections)} sections from outline")
        return sections
    except FileNotFoundError:
        logging.error(f"Outline file {filename} not found")
        return []

def compile_document(title, sections):
    document = f"# {title}\n\n"
    for section in sections:
        document += section + "\n\n"
    logging.info(f"Compiled document with {len(sections)} sections")
    return document

def save_document(document, filename):
    with open(filename, 'w') as f:
        f.write(document)
    logging.info(f"Document saved to {filename}")