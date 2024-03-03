import torch
from transformers import BertForSequenceClassification, BertTokenizer

# Load a trained model and vocabulary that you have fine-tuned
model = BertForSequenceClassification.from_pretrained(
    "models/two",
)
tokenizer = BertTokenizer.from_pretrained(
    "models/two",
)

topics = {
    0: "Analyst Update",
    1: "Fed | Central Banks",
    2: "Company | Product News",
    3: "Treasuries | Corporate Debt",
    4: "Dividend",
    5: "Earnings",
    6: "Energy | Oil",
    7: "Financials",
    8: "Currencies",
    9: "General News | Opinion",
    10: "Gold | Metals | Materials",
    11: "IPO",
    12: "Legal | Regulation",
    13: "M&A | Investments",
    14: "Macro",
    15: "Markets",
    16: "Politics",
    17: "Personnel Change",
    18: "Stock Commentary",
    19: "Stock Movement"
}


# Load a trained model and vocabulary that you have fine-tuned
def predict_label(text):
    tokens = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        return_tensors="pt",
        padding='max_length',
    )
    output = model(**tokens)
    probabilities = torch.nn.functional.softmax(output.logits, dim=-1)
    label = torch.argmax(probabilities).item()
    return topics.get(label, "-")

