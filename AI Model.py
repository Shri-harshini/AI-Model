from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

data = [
    ("Translate English to French: How are you?", "Comment ça va?"),
    ("Summarize: The sun rises in the east and sets in the west.", "Sun rises east, sets west."),
    ("Paraphrase: He is very smart.", "He is highly intelligent.")
]

inputs = []
outputs = []

for text, target in data:
    input_ids = tokenizer(text, return_tensors="pt", padding=True, truncation=True).input_ids
    target_ids = tokenizer(target, return_tensors="pt", padding=True, truncation=True).input_ids
    inputs.append(input_ids)
    outputs.append(target_ids)

for i in range(len(inputs)):
    loss = model(input_ids=inputs[i], labels=outputs[i]).loss
    print(f"Sample {i+1} Loss:", loss.item())

def generate(text):
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=50)
    return tokenizer.decode(output[0], skip_special_tokens=True)

print(generate("Translate English to French: Good morning"))
print(generate("Paraphrase: She is very kind."))