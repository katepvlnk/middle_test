import re


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_words(text):
    words = re.split(r'[ ,;:]+', text.strip())
    words = [w for w in words if w]
    return len(words)


def count_sentences(text):
    sentences = re.split(r'\.{3}|[.!?]', text.strip())
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)
