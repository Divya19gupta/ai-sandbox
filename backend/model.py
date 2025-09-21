from transformers import pipeline

model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

print(model("I love using transformers library!"))
print(model("This is the worst movie I have ever seen."))