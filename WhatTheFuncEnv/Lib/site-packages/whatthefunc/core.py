from openai import OpenAI
import os
from dotenv import load_dotenv

class WTF:
    """
    A class to define the WhatTheFunc functions.
    """
    def __init__(self, key: str | None = None):
        api_key = key or load_dotenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("No API Key found. Pass it in class or set OPENAI_API_KEY in environment")
        self.client = OpenAI(api_key=api_key)
        

    def wtfunc(self, text):
        if self.client is None:
            raise ValueError("API Key is not found or incorrect. Make sure to insert your API key into the class object first.")
        response = self.client.responses.create(
            model="gpt-5-mini",
            input="Here is the snippet of code that I want to know more about," + text
            + ". Explain what it does and its purpose for a beginner programmer in Layman's terms."
            + "Also make sure it is tied to its correct Python library if it does belong to any."
            + "Do not include follow up questions in your output, as it will be difficult to follow up for the purpose of this code."
        )
        return response.output_text or ""


