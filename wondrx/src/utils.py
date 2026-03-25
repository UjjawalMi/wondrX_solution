from rapidfuzz import process

MEDICINE_DB = [
    "metformin", "amitriptyline", "ciprofloxacin", "aspirin",
    "atorvastatin", "ramipril", "losartan", "ibuprofen",
    "paracetamol", "omeprazole", "pantoprazole",
    "doxycycline", "azithromycin", "cetirizine",
    "levocetirizine", "prednisolone", "tramadol"
]

def correct_spelling(word):
    match, score, _ = process.extractOne(word, MEDICINE_DB)
    return match if score > 80 else word