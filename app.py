from typing import Optional
import streamlit as st
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import os


# Function: Clean + Truncate Text
def clean_and_truncate(text:str, max_chars:int=20000)->str:
    cleaned=" ".join(text.strip().split())
    if len(cleaned)>max_chars:
        cleaned=cleaned[:max_chars] + "..."
    return cleaned

class Summarizer:
    
    def __init__(self,model_name:str="sshleifer/distilbart-cnn-12-6"):
        self.model_name=model_name
        self.pipeline = pipeline("summarization", model=model_name)  # type: ignore[arg-type]
    
    def summarize(self,text:str, max_length:int=150,min_length:int=40,do_sample:bool=False)->str:
        result=self.pipeline(text,max_length=max_length,min_length=min_length,do_sample=do_sample)
        return result[0].get("summary_text","")


