import pandas as pd
import yaml

# Input dataset file (change to CSV if you prefer)   hari ram
DATASET_FILE = "public_health_dataset_multilingual.xlsx"

# Output files
NLU_FILE = "data/nlu.yml"
DOMAIN_FILE = "domain.yml"

def convert_dataset():
    df = pd.read_excel(DATASET_FILE)

    nlu_data = {"version": "3.1", "nlu": []}
    domain_data = {
        "version": "3.1",
        "intents": ["ask_symptoms", "ask_prevention", "ask_vaccine"],
        "responses": {}
    }

    for _, row in df.iterrows():
        disease = row["Disease"]

        # English + Odia examples
        examples_sym = []
        if pd.notna(row["NLU_Examples_Symptoms_EN"]):
            examples_sym += row["NLU_Examples_Symptoms_EN"].split(" || ")
        if pd.notna(row["NLU_Examples_Symptoms_OD"]):
            examples_sym += row["NLU_Examples_Symptoms_OD"].split(" || ")

        examples_prev = []
        if pd.notna(row["NLU_Examples_Prevention_EN"]):
            examples_prev += row["NLU_Examples_Prevention_EN"].split(" || ")
        if pd.notna(row["NLU_Examples_Prevention_OD"]):
            examples_prev += row["NLU_Examples_Prevention_OD"].split(" || ")

        examples_vax = []
        if pd.notna(row["NLU_Examples_Vaccine_EN"]):
            examples_vax += row["NLU_Examples_Vaccine_EN"].split(" || ")
        if pd.notna(row["NLU_Examples_Vaccine_OD"]):
            examples_vax += row["NLU_Examples_Vaccine_OD"].split(" || ")

        # Add intents
        if examples_sym:
            nlu_data["nlu"].append({
                "intent": "ask_symptoms",
                "examples": "\n".join([f"- {ex}" for ex in examples_sym])
            })
            domain_data["responses"][f"utter_symptoms_{disease.lower().replace(' ', '_')}"] = [
                {"text": str(row["Symptoms_EN"])},
                {"text": str(row["Symptoms_OD"])}
            ]

        if examples_prev:
            nlu_data["nlu"].append({
                "intent": "ask_prevention",
                "examples": "\n".join([f"- {ex}" for ex in examples_prev])
            })
            domain_data["responses"][f"utter_prevention_{disease.lower().replace(' ', '_')}"] = [
                {"text": str(row["Prevention_EN"])},
                {"text": str(row["Prevention_OD"])}
            ]

        if examples_vax:
            nlu_data["nlu"].append({
                "intent": "ask_vaccine",
                "examples": "\n".join([f"- {ex}" for ex in examples_vax])
            })
            domain_data["responses"][f"utter_vaccine_{disease.lower().replace(' ', '_')}"] = [
                {"text": str(row["Vaccine_EN"])},
                {"text": str(row["Vaccine_OD"])}
            ]

    # Save files
    with open(NLU_FILE, "w", encoding="utf-8") as f:
        yaml.dump(nlu_data, f, allow_unicode=True, sort_keys=False)

    with open(DOMAIN_FILE, "w", encoding="utf-8") as f:
        yaml.dump(domain_data, f, allow_unicode=True, sort_keys=False)

    print("✅ Rasa NLU and Domain files generated successfully!")

if __name__ == "__main__":
    convert_dataset()

