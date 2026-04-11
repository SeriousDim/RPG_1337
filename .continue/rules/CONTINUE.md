# CONTINUE.md — project guide

> This file is meant for Continue and for humans: it explains the architecture, the main modules, and the common ways to work in this repository.
>
> Note: there is no `requirements.txt` or `pyproject.toml` in the repo, so dependency and run instructions below are marked as **needs verification** where appropriate.

## 1) Project Overview

### Purpose
This codebase looks like a prototype/library for:
- defining **game entities** with Python `dataclass`-style models: player, items, armor, locations, enemies, quests
- generating and filling **LLM prompts** from game state and catalog data
- calling LLMs through both **LangChain** and **DeepEval** adapters
- parsing model output into YAML + metadata artifacts
- validating generated quests with rule-based checks

### Key technologies
- Python 3.x (compiled artifacts suggest 3.13, but **needs verification**)
- `dataclasses` and `attrs`
- `PyYAML`
- `python-dotenv`
- `langchain-core` and provider integrations
- `deepeval`
- `openai`
- `requests`
- `pandas`

### High-level architecture
- **Domain model**: `model/` contains players, items, quests, mobs, and locations.
- **Game catalogs / world data**: `model/objects/` and `model/game/context/` define fixed lists of characters, enemies, armor, resources, and locations.
- **Prompt layer**: `resources/prompts/` stores prompt templates; `prompt/generator/` loads them; `generation/context/` assembles template variables.
- **LLM adapters**: `llm/langchain/` and `llm/deepeval/` build model clients for different providers.
- **Generation pipeline**: `experiment/` ties prompt creation, model invocation, parsing, and result saving together.
- **Validation**: `validation/formal/` contains rule objects that check schema and entity consistency in generated quests.
- **Artifacts**: `results/` stores generated YAML, metadata, and evaluation CSVs.


## 2) Getting Started

### Prerequisites
- Python **3.11+** is a safe assumption; compiled files in `.venv` suggest Python 3.13 (**needs verification**)
- `pip` + a virtual environment (`.venv` or similar)
- Internet access for LLM calls
- `PROXY_API_KEY` in the environment for ProxyAPI-based providers and evaluation scripts

### Installation
No lockfile or dependency manifest was found, so install the likely minimum manually (**verify against your environment**):
- `attrs`
- `PyYAML`
- `python-dotenv`
- `langchain-core`
- `langchain-openai`
- `langchain-anthropic`
- `langchain-google-genai`
- `langchain-openrouter`
- `deepeval`
- `openai`
- `requests`
- `pandas`

Typical setup:
1. create/activate a virtual environment
2. install the packages above
3. export `PROXY_API_KEY`
4. run the scripts you need

### Basic usage examples
- Load a prompt template by name through `prompt/generator/prompt_generator.py`
- Build a game state and generate prompt context through `generation/context/quest_context_generator.py`
- Run the single quest generation flow from `experiment/single_generation.py`
- Run the judge evaluation script in `tests/g_eval_test.py` to produce a CSV under `results/`

### Running tests
There is no formal pytest suite or test runner configuration detected.
Current verification is mostly done by:
- executing the scripts in `tests/`
- checking the YAML output in `results/generated/` or `results/`
- applying rule-based validation from `validation/formal/`


## 3) Project Structure

### Main directories
- `core/` — infrastructure helpers
  - `resource_loader.py` — safe loading of files from `resources/`
  - `find.py` — helper for resolving items/armor by name
  - `level_utils.py`, `yaml/` — supporting utilities
- `generation/` — prompt context assembly
  - `const.py` — template keys such as `player`, `game`, `quest_type`, `quest_format`
  - `context/quest_context_generator.py` — generates prompt variables from `GameState`
  - `objects/` — generators for player and world context
- `prompt/` — prompt loading and parsing
  - `generator/prompt_generator.py` — loads prompt templates into `ChatPromptTemplate`
  - `parser/result.py` — `LlmResult` model and save/load helpers
  - `parser/result_parser.py` — converts LLM messages into a savable result
- `llm/` — LLM provider adapters
  - `providers.py` — environment-backed provider registry
  - `langchain/` — LangChain model builders
  - `deepeval/` — DeepEval-compatible model builders and wrappers
- `model/` — domain models and catalogs
  - `model/player/` — `Player`, `PlayerArmor`, `PlayerLevel`, health, statistics
  - `model/items/` — `Item`, `Instrument`, `Weapon`, `Sword`, `Armor`, `Resource`
  - `model/mobs/` — `Character`, `Enemy`
  - `model/locations/` — location entities
  - `model/objects/` — fixed catalogs of items, characters, enemies, armors, locations
  - `model/game/` — DTO-like structures used for prompt context and game state
- `resources/` — prompt and schema assets
  - `prompts/automata_v1.txt`, `prompts/automata_v2.txt` — quest-generation prompts
  - `prompts/static_charatcers.txt` — static character prompt asset; filename looks misspelled, verify if intentional
  - `quest_yamls/delivery.yaml`, `quest_yamls/delivery_v2.yaml` — YAML format examples/schemas for delivery quests
- `experiment/` — end-to-end orchestration
  - `single_generation.py` — prompt + model + parsing + save flow
  - `many_generations.py`, `formal_validator.py` — batch and validation helpers
- `tests/` — runnable evaluation scripts rather than a classic unit-test suite
  - `g_eval_test.py` — DeepEval-based judge comparison over multiple models
  - `prompt_test.py`, `context_test.py`, `many_generation_test.py` — ad hoc verification scripts
- `validation/` — rule-based validation
  - `formal/` — quest schema, entity existence, and balance checks
  - `llm_based/` — currently empty in this checkout
- `results/` — generated artifacts and evaluation outputs

### Important files
- `core/resource_loader.py`
  - safe path resolution prevents traversal outside `resources/`
- `prompt/generator/prompt_generator.py`
  - loads `resources/prompts/<name>.txt` through `ResourceLoader`
- `generation/context/quest_context_generator.py`
  - maps prompt keys to context payloads from `GameState`
- `experiment/single_generation.py`
  - orchestrates `GameState` -> prompt -> model -> parsed result -> save
- `prompt/parser/result.py`
  - saves raw model output, metadata, and parsed YAML to disk
- `validation/formal/*.py`
  - checks required keys, entity existence, delivery-quest constraints, and rewards

### Configuration files
- `.gitignore` — ignores `.env`, `.vscode`, caches, `.deepeval`, and other local artifacts
- `.env` — expected locally for API keys; should not be committed
- `.continue/rules/CONTINUE.md` — this guide, auto-loaded by Continue for this project


## 4) Development Workflow

### Coding conventions
- Prefer small, serializable `dataclass`-style models.
- Keep game content in catalog modules rather than hardcoding it in prompts.
- Use exact names from the catalogs when validating or generating quests.
- Be careful with side effects at import time: several provider modules read environment variables when imported.

### Testing approach
Recommended layers:
1. **resource loading** — ensure prompt and YAML assets resolve safely
2. **prompt context generation** — verify the keys `{player}`, `{game}`, `{quest_type}`, `{quest_format}` are filled correctly
3. **LLM response parsing** — verify `LlmResult.extract_yaml_content()` handles fenced and unfenced YAML
4. **formal validation** — run the rule classes in `validation/formal/`

### Build / deployment
- No build pipeline, packaging config, or deployment automation was found.
- Treat the project as a local research/prototyping repository unless a later manifest or CI workflow is added.

### Contribution guidelines
- Keep changes aligned across the whole pipeline: catalogs, prompt templates, context generators, parsers, and validators.
- When adding a new entity, update both the source catalog and the validation rules that reference that catalog.
- Commit generated artifacts only when they are intended as examples or benchmarks.
- Prefer small focused changes over broad refactors.


## 5) Key Concepts

### Domain terminology
- **Rank** — item progression tier used by weapons, resources, and armor.
- **Item hierarchy** — `Item` → `Instrument` → `Weapon` → `Sword`.
- **Armor** — item with `absorbed_damage` used by `PlayerArmor`.
- **Resource** — harvestable item with `resource_type` and `min_instrument_rank`.
- **GameState** — combines the current `Player` and generated world context.
- **Quest** — currently modeled as a YAML-driven object with delivery/encounter/destination parts.
- **Validation** — formal rules that ensure the generated quest follows the expected schema and only references existing entities.

### Core abstractions
- **Prompt templates**: text files under `resources/prompts/` with placeholders like `{player}`, `{game}`, `{quest_type}`, `{quest_format}`.
- **Context generators**: functions/classes in `generation/context/` that fill the placeholders.
- **Result wrapper**: `prompt/parser/result.py:LlmResult` saves content and metadata side by side.
- **Provider registry**: `llm/providers.py` exposes provider credentials and base URLs.
- **Model adapters**: LangChain and DeepEval wrappers normalize different API providers behind a common interface.

### Design patterns used
- Catalog/data-table pattern for fixed world content
- Adapter pattern for LLM provider integrations
- Template + context filling for prompt generation
- Rule-based validation for schema/entity integrity


## 6) Common Tasks

### 6.1 Add a new item, character, enemy, or location
1. Add or update the relevant dataclass/model if needed.
2. Add the instance to the appropriate catalog module in `model/objects/`.
3. Update any generator or prompt context code that serializes the catalog.
4. Update validation rules so the new entity is considered valid.
5. If the entity should appear in prompts, add it to the prompt-facing game context.

### 6.2 Add or edit a prompt
1. Edit or create a file in `resources/prompts/<name>.txt`.
2. Load it through `prompt/generator/prompt_generator.py` or the existing smoke-test scripts.
3. Confirm all placeholders have matching context keys.
4. If the prompt format changes, update the YAML examples in `resources/quest_yamls/` and the formal validators.

### 6.3 Generate a quest end-to-end
1. Create or update the prompt template.
2. Build the game state through `model/game/state/game_state.py`.
3. Use `experiment/single_generation.py` as the orchestration entry point.
4. Save the parsed result under `results/generated/`.
5. Validate the generated YAML with the formal validators.

### 6.4 Add a new provider or model
1. Add the provider credentials to `llm/providers.py`.
2. Implement or extend the LangChain adapter in `llm/langchain/model_handlers.py`.
3. Implement or extend the DeepEval adapter in `llm/deepeval/model_handlers.py` if judge support is needed.
4. Check base URL formatting and authentication headers.
5. Verify the model works in both prompt generation and evaluation flows if applicable.

### 6.5 Load a resource safely
Use `core.resource_loader.ResourceLoader.load_text(...)` instead of plain `open()` when reading prompt or schema files. This prevents path traversal outside `resources/`.


## 7) Troubleshooting

### `KeyError: 'PROXY_API_KEY'`
- `llm/providers.py` and `tests/g_eval_test.py` read this variable directly from the environment.
- Export the variable before importing those modules or running the scripts.
- If you use `.env`, ensure `python-dotenv` is installed and loaded early enough.

### `FileNotFoundError` when loading prompts or schemas
- Check the path relative to `resources/`.
- Confirm the filename spelling, especially for assets like `static_charatcers.txt`.
- Remember that `ResourceLoader` deliberately blocks `..` traversal.

### Generated YAML fails to parse
- Make sure the model returns valid YAML, ideally fenced with ```yaml.
- Check `prompt/parser/result.py:LlmResult.extract_yaml_content()` and the prompt instructions.
- Verify that the schema file under `resources/quest_yamls/` matches the prompt.

### Validation fails because of unknown entities
- Validation checks exact names against the catalogs.
- Update `model/objects/` if you added a new item, enemy, or character.
- Verify there are no typos or mismatched aliases in the generated YAML.

### LLM requests fail with 401/403/404/timeouts
- Check `PROXY_API_KEY` and the provider base URL.
- Confirm the model name is valid for the provider.
- Review the adapter base URL formatting in `llm/langchain/model_handlers.py` and `llm/deepeval/model_handlers.py` if the endpoint looks wrong.

### Prompt generation looks empty or incomplete
- Inspect `generation/context/quest_context_generator.py` to ensure all required keys are populated.
- Verify the prompt template file exists in `resources/prompts/`.
- Confirm the prompt parser is not stripping useful content unexpectedly.


## 8) References

- DeepEval docs: https://docs.confident-ai.com/
- OpenAI Python SDK: https://github.com/openai/openai-python
- LangChain prompt docs: https://python.langchain.com/docs/concepts/prompt_templates/
- PyYAML: https://pyyaml.org/
- requests: https://requests.readthedocs.io/
- ProxyAPI: **needs verification**

---

## TODO / Needs verification
- [ ] Add `requirements.txt` or `pyproject.toml` with pinned dependencies.
- [ ] Add a formal `pytest` suite.
- [ ] Verify whether `resources/prompts/static_charatcers.txt` is intentionally misspelled.
- [ ] Review the `llm/*` base URL formatting for each provider.
- [ ] Decide whether `validation/llm_based/` should remain empty or be implemented.
- [ ] Document the exact YAML schema for each quest type.
