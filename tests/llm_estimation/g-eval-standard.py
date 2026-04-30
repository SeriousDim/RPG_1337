from pathlib import Path
import yaml

from llm.deepeval.create_model import create_deepeval_model
from llm.providers import PROVIDERS
from tests.llm_estimation.criteria import CRITERIA
from tests.llm_estimation.estimation import create_g_eval, create_test_case, evaluate, prepare_dialogs, read_model_quests_paths, read_quest, save_estmations


def evaluate_all_g_evals_for_quest(g_evals, model_dir, quest_name, quest_yaml, judge_model_name, input):
    formatted_quest = yaml.safe_dump(quest_yaml, sort_keys=False, allow_unicode=True, indent=2)
    for g_eval in g_evals:
        evaluate(g_eval, lambda: create_test_case(input, formatted_quest))
    
    save_estmations(g_evals, quest_name, f"{model_dir}/estimated_by_{judge_model_name}")


def evaluate_all_g_evals_for_dialogs(g_evals, model_dir, quest_name, quest_yaml, judge_model_name, input):
    dialogs_str = prepare_dialogs(quest_yaml)
    for g_eval in g_evals:
        evaluate(g_eval, lambda: create_test_case(input, dialogs_str))
    
    save_estmations(g_evals, quest_name + "_dialogs", f"{model_dir}/estimated_by_{judge_model_name}")


def evaluate_quest_with_model(g_evals, model_dir, quest_name, quest_yaml, judge_model_name, input):
    print(f"Evaluting whole quest")
    evaluate_all_g_evals_for_quest(g_evals, model_dir, quest_name, quest_yaml, judge_model_name, input)
    # print(f"Evaluting dialogs")
    # evaluate_all_g_evals_for_dialogs(g_evals, model_dir, quest_name, quest_yaml, judge_model_name, input)


provider = PROVIDERS['router_ai']
estimators = {
    'gpt': create_deepeval_model("openai/gpt-5.4-mini", provider),
    'deepseek': create_deepeval_model("deepseek/deepseek-v3.2", provider),
    'claude': create_deepeval_model("anthropic/claude-haiku-4.5", provider),
    'gemini': create_deepeval_model("google/gemini-3-flash-preview", provider),
}

enable_log_probs = False
for key in estimators.keys():
    estimators[key].model_data.supports_log_probs = enable_log_probs
    estimators[key].temperature = 0.0


input_path = Path("./results/prompts/lvl_1/automata_v2_delivery_v2.txt")
with input_path.open("r", encoding="utf-8") as file:
    input = file.read()

model_dirs = [
    'claude-haiku-4-5-automata_v2-delivery_v2',
    'gemini-3-flash-preview-automata_v2-delivery_v2',
    'deepseek/deepseek-v3.2-automata_v2-delivery_v2',
    'gpt-5.4-automata_v2-delivery_v2'
]

for model_dir in model_dirs:
    quests_paths = read_model_quests_paths(model_dir, root_path="./results/quests")

    #judge_model = estimators['deepseek']
    judge_model = estimators['gpt']
    g_evals = [
        create_g_eval(judge_model, c) for c in CRITERIA
    ]

    print(f"Evaluting directory: {model_dir}")
    for p in quests_paths:
        for idx in range(4, 10):
            quest_name = p.parent.name
            print(f"Evaluting: {quest_name}")
            quest_yaml = read_quest(p)
            evaluate_quest_with_model(g_evals, model_dir, f"{model_dir}/{quest_name}_{idx}", quest_yaml, judge_model.name, input)
