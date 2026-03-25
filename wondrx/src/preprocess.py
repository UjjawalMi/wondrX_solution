import re

ABBREVIATIONS = {
    "tab": "tablet",
    "cap": "capsule",
    "inj": "injection",
    "syp": "syrup",
    "syr": "syrup",
    "susp": "suspension",

    "od": "once daily",
    "bd": "twice daily",
    "tds": "three times daily",
    "qid": "four times daily",
    "hs": "at bedtime",
    "sos": "if needed",
    "prn": "if needed",

    "af": "after food",
    "a/f": "after food",
    "pc": "after food",
    "bf": "before food",
    "ac": "before food",
}

def normalize_text(text):
    text = text.lower()

    text = re.sub(r"[^\w\s/\-]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    expanded_words = []

    for word in words:
        if word in ABBREVIATIONS:
            expanded_words.append(ABBREVIATIONS[word])
        else:
            expanded_words.append(word)

    text = " ".join(expanded_words)

    text = re.sub(r"x(\d+)d", r"for \1 days", text)
    text = re.sub(r"(\d+)d", r"\1 days", text)
    text = re.sub(r"(\d+)wk", r"\1 week", text)
    text = re.sub(r"(\d+)weeks", r"\1 week", text)

    return text