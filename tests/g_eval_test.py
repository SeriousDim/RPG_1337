from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams
from deepeval.models import DeepEvalBaseLLM, GPTModel, AnthropicModel, OpenRouterModel
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
import pandas as pd

from llm.deepeval.gemini import GeminiViaHttpLLM
from llm.deepeval.open_ai_competible_chat_llm import OpenAICompatibleChatLLM

from dotenv import load_dotenv
load_dotenv()

import os
PROXY_API_KEY = os.environ["PROXY_API_KEY"]

gpt_judge = GPTModel(
    model="gpt-5.2",
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
    
)
gpt_judge.model_data.supports_log_probs = True

gpt_4_judge = GPTModel(
    model="gpt-4-turbo",
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1"
)

claude_judge = AnthropicModel(
    model="claude-sonnet-4-6",
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/anthropic"
)

gemini_judge = GeminiViaHttpLLM(
    model="gemini-2.5-pro",
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/google"
)

deepseek_judge = OpenRouterModel(
    model="deepseek/deepseek-v3.2",
    api_key=PROXY_API_KEY,
    base_url="https://api.proxyapi.ru/openrouter/v1"
)

def create_correctness_g_eval(judge_model):
    return GEval(
        name="Correctness",
        criteria="Determine whether the actual output is factually correct based on the expected output.",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=judge_model,
        top_logprobs=5
    )

def create_relevancy_metric(judge_model):
    return AnswerRelevancyMetric(
        threshold=0.7,
        include_reason=True,
        model=judge_model
    )

def eval_judge_model(test_case, judge_model: DeepEvalBaseLLM):
    correctness = create_correctness_g_eval(judge_model)
    relevancy = create_relevancy_metric(judge_model)
    
    correctness.measure(test_case)
    relevancy.measure(test_case)
    
    return {
        "model": judge_model.name,
        "correctness": correctness,
        "relevancy": relevancy
    }

test_case = LLMTestCase(
    input="The dog chased the cat up the tree, who ran up the tree?",
    actual_output="It depends, some might consider the cat, while others might argue the dog."
)

judges = [gpt_judge, claude_judge, gemini_judge, deepseek_judge]

results = []
for judge in judges:
    if judge is not None:
        results.append(eval_judge_model(test_case, judge))

def to_pandas(results):
    rows = map(lambda r: {
        "model": r["model"], 
        "correctness (score)": r["correctness"].score, 
        "correctness (reason)": r["correctness"].reason, 
        "relevancy (score)": r["relevancy"].score, 
        "relevancy (reason)": r["relevancy"].reason, 
        }, results)
    return pd.DataFrame(rows)

to_pandas(results).to_csv("./results/results.csv")
