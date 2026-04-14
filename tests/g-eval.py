from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams
from deepeval.models import DeepEvalBaseLLM, GPTModel, AnthropicModel, OpenRouterModel
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
import pandas as pd

from llm.deepeval.create_model import create_deepeval_model
from llm.deepeval.gemini import GeminiViaHttpLLM
from llm.deepeval.open_ai_competible_chat_llm import OpenAICompatibleChatLLM

import os

from llm.providers import PROVIDERS
from prompt.generator.prompt_generator import prompt_from_file

provider = PROVIDERS['router_ai']
gpt_judge = create_deepeval_model("gpt-5.2", provider)

criterions = {
    "relevancy": AnswerRelevancyMetric(
        model=gpt_judge,
        top_logprobs=5
    )
}
g_eval_criterions = {
    "relevancy": GEval(
        name="Релевантность",
        criteria="Диалоги должны быть напрямую связаны с заданным игровым контекстом, целью квеста \
            и входными данными. Все упомянутые персонажи, предметы, локации и действия должны \
                соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
    "consistency": GEval(
        name="Релевантность",
        criteria="Текст должен быть напрямую связан с заданным игровым контекстом, целью квеста и входными данными. Все упомянутые персонажи, предметы, локации и действия должны соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
    "coherence": GEval(
        name="Релевантность",
        criteria="Текст должен быть напрямую связан с заданным игровым контекстом, целью квеста и входными данными. Все упомянутые персонажи, предметы, локации и действия должны соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
    "naturalness": GEval(
        name="Релевантность",
        criteria="Текст должен быть напрямую связан с заданным игровым контекстом, целью квеста и входными данными. Все упомянутые персонажи, предметы, локации и действия должны соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
    "non_redundancy": GEval(
        name="Релевантность",
        criteria="Текст должен быть напрямую связан с заданным игровым контекстом, целью квеста и входными данными. Все упомянутые персонажи, предметы, локации и действия должны соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
    "safety": GEval(
        name="Релевантность",
        criteria="Текст должен быть напрямую связан с заданным игровым контекстом, целью квеста и входными данными. Все упомянутые персонажи, предметы, локации и действия должны соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
    "reward": GEval(
        name="Релевантность",
        criteria="Текст должен быть напрямую связан с заданным игровым контекстом, целью квеста и входными данными. Все упомянутые персонажи, предметы, локации и действия должны соответствовать теме и намерению задачи",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=gpt_judge,
        top_logprobs=5
    ),
}

with open("./results/prompts/lvl_1/automata_v1_delivery_v2.txt", "r") as file:
    input = file.read()

with open("./results/generated/gpt-5.2-automata_v1-delivery_v2/content.yaml", "r") as file:
    output = file.read()

test_case = LLMTestCase(
    input=input,
    actual_output=output
)


