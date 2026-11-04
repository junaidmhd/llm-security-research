from datasets import load_dataset

dataset = load_dataset(
    "TrustAIRLab/in-the-wild-jailbreak-prompts",
    "jailbreak_2023_12_25",
    split="train"
)

print(dataset)
print(dataset[0])
dataset.to_csv("jailbreak_dataset.csv", index=False)

print("Dataset saved successfully!")