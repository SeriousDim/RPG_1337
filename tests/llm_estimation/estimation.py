import json
from pathlib import Path
from deepeval.models import DeepEvalBaseLLM, GPTModel, AnthropicModel, OpenRouterModel
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

import yaml


def read_quest(path):
    path = Path(path)
    with path.open("r", encoding="utf-8") as file:
        quest = yaml.safe_load(file)

    if quest is None:
        return {}
    if not isinstance(quest, dict):
        raise ValueError(f"Expected a YAML mapping in {path}, got {type(quest).__name__}")

    return quest


def read_model_quests_paths(path, root_path="./results/generated"):
    root = Path(root_path) / path
    if not root.exists():
        return []

    quests = []
    for content_path in sorted(root.rglob("content.yaml")):
        if content_path.is_file():
            quests.append(content_path)

    return quests


def save_estmations(g_evals, quest_name, dir_to_save, root_path="./results/estimation"):
    data = {
        'quest': quest_name,
        'estimator': dir_to_save,
        'metrics': {
            g.name: {
                'score': g.score,
                'reason': g.reason,
                'name': g.name,
                'criteria': g.criteria,
                'steps': g.evaluation_steps
            } for g in g_evals
        }
    }

    output_path = Path(root_path) / dir_to_save / f"{quest_name}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def create_g_eval(judge_model, criteria_tuple):
    return GEval(
        name=criteria_tuple[0],
        criteria=f"{criteria_tuple[1]}. {criteria_tuple[2]}",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model=judge_model,
        top_logprobs=5
    )


def create_test_case(input, output):
    return LLMTestCase(
        input=input,
        actual_output=output
    )


def evaluate(g_eval, test_case_factory):
    test_case = test_case_factory()
    g_eval.measure(test_case)


def prepare_dialogs(quest):
    def _format_dialogs(dialogs) -> list[str]:
        lines = []
        for dialog in dialogs or []:
            speaker = dialog.get("speaker", "")
            remark = dialog.get("remark", "")
            lines.append(f"- {speaker}: {remark}")
        return lines

    quest_content = quest.get("quest", {})
    parts = quest_content.get("parts", {})
    resource_to_deliver = parts.get("resource_to_deliver", {})
    enemy_to_face = parts.get("enemy_to_face", {})
    destination = parts.get("destination", {})

    result = [
        "Диалоги для части с получением задания на доставку:",
        *_format_dialogs(resource_to_deliver.get("dialogs", [])),
        "",
        "Диалоги для части со встречей с противником:",
        *_format_dialogs(enemy_to_face.get("dialogs", [])),
        "",
        "Диалоги для части с доставкой персонажу (завершение квеста):",
        *_format_dialogs(destination.get("dialogs", [])),
    ]

    return "\n".join(result)

