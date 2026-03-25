from preprocess import normalize_text
from extractor import extract_fields
import json
from tqdm import tqdm

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def save_output(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def process_pipeline(data):
    results = []

    for item in tqdm(data):
        raw = item["raw_text"]
        cleaned = normalize_text(raw)
        extracted = extract_fields(cleaned)

        result = {
            "raw_text": raw,
            "medicine_name": extracted["medicine_name"],
            "form": extracted["form"],
            "strength": extracted["strength"],
            "dosage": extracted["dosage"],
            "frequency": extracted["frequency"],
            "duration": extracted["duration"],
            "notes": extracted["notes"]
        }

        results.append(result)

    return results


if __name__ == "__main__":
    data = load_data("data/prescription_raw_text_only.json")

    print("Processing dataset...")
    results = process_pipeline(data)

    save_output(results, "output/result.json")

    print("Extraction complete. Saved to output/result.json")