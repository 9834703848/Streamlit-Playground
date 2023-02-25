import streamlit as st
import pandas as pd
import numpy as np

import requests
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
    "inputs": "I will win this",
    "parameters": {"candidate_labels": ["postive", "negative1", "faq"]},
})
st.write(output)