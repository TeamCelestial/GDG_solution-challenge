# text_model.py - BERT for Text Moderation

from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf

# Load pre-trained BERT model and tokenizer
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def predict(text):
    inputs = tokenizer(text, return_tensors="tf")
    logits = model(inputs).logits
    predictions = tf.nn.softmax(logits, axis=-1)
    return predictions

# backend/models/text_model.py
def predict(text):
    return f"Fake prediction for: {text}"
