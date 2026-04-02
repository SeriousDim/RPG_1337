import os
from openai import OpenAI
from deepeval.models.base_model import DeepEvalBaseLLM

class OpenAICompatibleChatLLM(DeepEvalBaseLLM):
    def __init__(self, model: str, base_url: str, api_key: str):
        self.model = model
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.name = model

    def load_model(self):
        return self.client

    def generate(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message.content

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return self.model
