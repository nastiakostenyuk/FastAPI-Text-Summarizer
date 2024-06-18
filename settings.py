from fastapi import FastAPI
from transformers import pipeline


app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
