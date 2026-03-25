import re
from utils import correct_spelling

FORMS = ["tablet", "capsule", "injection", "syrup", "suspension"] # constants declaration

FREQUENCY_PATTERNS = [
    "once daily",
    "twice daily",
    "three times daily",
    "four times daily",
    "at bedtime",
    "if needed"
]

NOTES_PATTERNS = [
    "after food",
    "before food",
    "empty stomach",
    "at bedtime",
    "morning only",
    "with food",
    "with milk"
]



def extract_fields(text):  #main
    result = {
        "medicine_name": "",
        "form": "",
        "strength": "",
        "dosage": "",
        "frequency": "",
        "duration": "",
        "notes": ""
    }

    for form in FORMS:
        if form in text:
            result["form"] = form
            break

    strength_match = re.search(r"\d+\s?(mg|iu|ml)", text)
    if strength_match:
        result["strength"] = strength_match.group()

    dosage_match = re.search(r"\d+\s?(tablet|capsule|ml|ampoule|vial)s?", text)
    if dosage_match:
        result["dosage"] = dosage_match.group()

    if re.search(r"1-0-1|1-1-0|0-1-1", text):
        result["frequency"] = "twice daily"

    elif re.search(r"1-1-1", text):
        result["frequency"] = "three times daily"

    if not result["frequency"]:
        for freq in FREQUENCY_PATTERNS:
            if freq in text:
                result["frequency"] = freq
                break

    duration_match = re.search(r"(for )?\d+\s?(days|day|week|weeks)", text)
    if duration_match:
        result["duration"] = duration_match.group().replace("for ", "")

    for note in NOTES_PATTERNS:
        if note in text:
            result["notes"] = note
            break

    temp = text

    for value in result.values():
        if value:
            temp = temp.replace(value, "")

    temp = re.sub(r"\d+", "", temp)  # Remove numbers & extra spaces
    temp = re.sub(r"\s+", " ", temp).strip()

    tokens = temp.split()  # Token-based extraction

    medicine = ""
    for token in tokens:
        if len(token) > 3:  # avoid noise like 'mg', 'ml'
            medicine = token
            break

    # Spell correction
    medicine = correct_spelling(medicine)

    result["medicine_name"] = medicine

    return result