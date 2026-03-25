# Prescription NLP Extraction Pipeline

Problem Statement: Extract structured prescription information from raw, noisy medical text.

Objective: Convert unstructured prescription text into structured JSON with fields:

medicine_name
form
strength
dosage
frequency
duration
notes

Approach:

1. Preprocessing (Lowercasing, Punctuation removal, Abbreviation expansion (OD → once daily, BD → twice daily), Duration normalization (x5d → 5 days))

2. Rule-Based Extraction: Regex patterns for strenth, frequency, etc.

3. Post-processing: RapidFuzz and cleaning the different tokens.

Tech Stack: Python, Regex, RapidFuzz, tqdm.


Evaluation: 

Input:
"Tab. Amitriptyline 25 mg 1 tablet OD for 5 days at bedtime"

Output:
{
medicine_name: amitriptyline
form: tablet
strength: 25 mg
dosage: 1 tablet
frequency: once daily
duration: 5 days
notes: at bedtime
}

## Failure Cases: I also want to highlight that misspellings or any ambiguous frequency

To Run: 

pip install -r requirements.txt
python src/main.py

Output: 

Results saved in: output/result.json