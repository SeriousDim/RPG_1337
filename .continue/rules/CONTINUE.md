# CONTINUE.md — руководство по проекту

> Этот файл предназначен для Continue (и людей): кратко описывает архитектуру, ключевые модули и типовые рабочие операции.
> 
> Примечание: в репозитории не найден `requirements.txt/pyproject.toml`, поэтому разделы про зависимости и запуск помечены как **нуждается в проверке**.

## 1) Project Overview

### Назначение
Проект выглядит как прототип/библиотека для:
- описания **игровых сущностей** (игрок, предметы, броня, уровни, квесты) через Python `dataclass`
- генерации/подготовки **промптов** для LLM (папка `resources/prompts`)
- интеграции с LLM-провайдерами через **адаптеры** (`llm_adapters/*`)
- запуска **оценок качества ответов** (LLM-as-a-judge) через `deepeval` (скрипт `view/g_eval_test.py`), с сохранением результатов в `results/`

### Ключевые технологии
- Python (по артефактам видно Python 3.13, но **нуждается в проверке**)
- `dataclasses`
- `deepeval` (метрики GEval/AnswerRelevancy)
- `openai` SDK (для OpenAI-compatible endpoint)
- `requests` (для Gemini через HTTP)
- `python-dotenv` (загрузка `.env`)
- `pandas` (сохранение результатов в CSV)
- `langchain_core.prompts.ChatPromptTemplate` (заготовка для сборки промпта)

### Высокоуровневая архитектура
- **Domain model**: `model/` — игровые сущности как dataclass’ы (Player/Items/Armor/Quest/etc.)
- **Game data каталоги**: `model/objects/*` — «справочники» (списки мечей, ресурсов, брони, уровней)
- **Resources**: `resources/prompts/*.txt` — текстовые шаблоны промптов
- **Engine**: `engine/resource_loader.py` — безопасная загрузка ресурсов из `resources/`
- **Context/Prompt**: `context/*` — генерация контекста и промптов (частично пусто/заглушки)
- **LLM adapters**: `llm_adapters/*` — модели/клиенты, совместимые с интерфейсом `DeepEvalBaseLLM`
- **View (скрипты)**: `view/*` — runnable-модули для проверок/экспериментов (в т.ч. оценка судей)


## 2) Getting Started

### Prerequisites
- Python **3.11+** (рекомендуется), фактически в `.venv` встречается `cpython-313` (**нуждается в проверке**)
- Установленные зависимости (см. ниже)
- Переменные окружения (для LLM-запросов):
  - `PROXY_API_KEY` — используется в `view/g_eval_test.py`

### Установка (нуждается в проверке)
Так как файл зависимостей не найден, ниже — предполагаемый минимум (уточните по вашей среде):

```bash
pip install deepeval openai requests python-dotenv pandas langchain-core
```

Если у вас уже есть виртуальное окружение `.venv`, активируйте его и установите зависимости в него.

### Базовые примеры запуска
Показать содержимое промпта из `resources/`:

```bash
python -m view.context_test
```

Запустить эксперимент по «судьям» (deepeval), сохранить CSV в `results/results.csv`:

```bash
python -m view.g_eval_test
```

Важно: `view/g_eval_test.py` обращается к внешним API через ProxyAPI, без `PROXY_API_KEY` упадёт.

### Запуск тестов
Тестовый фреймворк как отдельный набор тестов не обнаружен (нет `tests/`, нет `pytest`-тестов). Скрипты в `view/` выполняют роль проверок.


## 3) Project Structure

### Директории
- `model/` — доменная модель игры
  - `model/player/` — Player, уровни, здоровье, статистика, броня
  - `model/items/` — базовые Item/Instrument/Weapon/Sword/Armor/Resource
  - `model/quest/` — структура квеста (Quest/QuestPart)
  - `model/objects/` — «каталоги» предопределённых объектов (мечи, ресурсы, броня, уровни)
- `resources/` — ресурсы (тексты промптов)
  - `resources/prompts/automata_v1.txt` — шаблон промпта для генерации квеста (YAML-формат)
- `engine/` — утилиты инфраструктуры
  - `engine/resource_loader.py` — безопасная загрузка файлов из `resources/`
- `context/` — генерация контекста/промптов
  - `context/prompt_generator.py` — заготовка генератора (сейчас есть заглушки/ошибки, см. ниже)
  - `context/context_generator.py` — файл пустой (**нуждается в реализации/удалении**)
- `llm_adapters/` — адаптеры LLM под `deepeval`
  - `open_ai_competible_chat_llm.py` — OpenAI-compatible chat endpoint через `openai.OpenAI`
  - `gemini.py` — Gemini via HTTP POST
- `view/` — runnable-скрипты/эксперименты
  - `context_test.py` — печатает промпт
  - `g_eval_test.py` — прогон метрик `deepeval` разными judge-моделями
- `results/` — артефакты экспериментов
  - `results.csv` — результаты `g_eval_test.py`
  - `logprobs.md` — заметки о поддержке log_probs разными моделями

### Важные файлы и замечания
- `engine/resource_loader.py`
  - Использует safe-resolve, предотвращая выход из `resources/` через `..`.
  - Это критичный компонент для безопасной загрузки текстовых шаблонов.

- `context/prompt_generator.py` (нуждается в проверке/правках)
  - `find_prompt_template_by_name()` сейчас возвращает строку `"prompts/{prompt_name}.txt"` без f-string → фактически всегда пытается загрузить файл с буквальным `{prompt_name}`.
  - `generate_prompt()` сейчас игнорирует заполненный промпт и возвращает только системное сообщение.
  - `fill_context()` возвращает пустую строку.

- `view/g_eval_test.py`
  - Это не юнит-тест, а эксперимент/скрипт.
  - Требует `PROXY_API_KEY` и интернет.
  - Пишет CSV в `./results/results.csv`.

### Конфигурация
- `.gitignore` игнорирует `.env`, `.vscode`, кэши, `.deepeval`.
- Файлы `.vscode/*` есть, но чтение `.vscode/settings.json` запрещено политикой инструментов (security).


## 4) Development Workflow

### Стандарты кода
- Используются `dataclass` и простые типы; старайтесь сохранять модель максимально «плоской» и сериализуемой.
- Для новых сущностей:
  - добавляйте типы в `model/`
  - добавляйте справочники/таблицы в `model/objects/`, если это «фиксированный контент»

Рекомендуемые (но не зафиксированные в репо) инструменты:
- форматирование: `black`
- сортировка импортов: `isort`
- линтинг: `ruff`

(**нуждается в проверке/добавлении конфигов**)

### Подход к тестированию
- Сейчас основная проверка — запуск модулей `view/*`.
- Рекомендуется добавить `pytest` и покрыть:
  - `ResourceLoader._safe_resolve()` (в т.ч. атаки через `../`)
  - корректность каталогов объектов (`SWORDS`, `HELMETS`, …)
  - сериализацию Player/Items в формат, ожидаемый промптами

### Build/Deploy
- Явного пайплайна сборки/деплоя не обнаружено.
- Проект сейчас выглядит как локальный исследовательский/прототипный.

### Contribution guidelines
- Делайте изменения небольшими PR/коммитами.
- Для изменений промптов:
  - обновляйте файлы в `resources/prompts/`
  - фиксируйте ожидаемый формат (например YAML schema) рядом, либо в комментариях в шаблоне
- Для изменений, связанных с LLM и метриками:
  - сохраняйте результаты в `results/` только если это осознанная фиксация артефактов (иначе лучше `.gitignore`)


## 5) Key Concepts

### Термины домена
- **Rank** — уровень/ранг предмета (в `Item.rank`) и минимальные требования к инструменту для ресурсов.
- **Instrument/Weapon/Sword** — иерархия предметов:
  - `Item` → `Instrument` → `Weapon` → `Sword`
- **Armor** — предмет, который поглощает урон (`absorbed_damage`).
- **PlayerArmor** — агрегирует части брони и суммарный `current_armor_absorbed_damage`.
- **LevelGradation / LEVELS** — таблица XP до следующего уровня.
- **Quest / QuestPart** — квест как набор частей с диалогами и хуками жизненного цикла.

### Промпты
- `automata_v1.txt` задаёт генерацию **ровно одного квеста** типа `{quest_type}` в YAML-формате `{quest_format}`.
- В промпте есть строгие требования: не упоминать сущности, которых нет в игре.

### Оценка ответов (deepeval)
- `GEval` используется для метрики «Correctness».
- `AnswerRelevancyMetric` — релевантность ответа.
- Judge-модели в `view/g_eval_test.py` включают:
  - GPT через ProxyAPI OpenAI endpoint
  - Claude через ProxyAPI Anthropic endpoint
  - Gemini через HTTP adapter
  - DeepSeek через OpenRouter


## 6) Common Tasks

### 6.1 Добавить новый предмет (например новое оружие)
1. Добавьте dataclass (если нужен новый тип) в `model/items/`.
2. Добавьте экземпляры в соответствующий справочник в `model/objects/objects.py`.
3. Убедитесь, что промпты/контекст знают, как сериализовать и перечислять эти сущности.

### 6.2 Добавить/изменить промпт
1. Создайте/отредактируйте файл в `resources/prompts/<name>.txt`.
2. Проверьте загрузку через:

```bash
python -m view.context_test
```

3. Если промпт параметризуется (`{player}`, `{game}` …), убедитесь, что генерация контекста реально их подставляет (**сейчас `fill_context()` заглушка**).

### 6.3 Запустить оценку judge-моделей и получить CSV
1. Создайте `.env` (он игнорируется git’ом) и добавьте:

```env
PROXY_API_KEY=...
```

2. Запустите:

```bash
python -m view.g_eval_test
```

3. Результат: `results/results.csv`.

### 6.4 Загрузить ресурс безопасно
Используйте `ResourceLoader.load_text("prompts/...")`. Не используйте прямой `open()` для ресурсов, если важна защита от path traversal.


## 7) Troubleshooting

### `FileNotFoundError` при загрузке промпта
- Проверьте путь относительно `resources/`.
- Пример корректного вызова:
  - `ResourceLoader.load_text("prompts/automata_v1.txt")`

### `ValueError: Недопустимый путь`
- `ResourceLoader` блокирует пути, выходящие за `resources/`.
- Убедитесь, что вы не передаёте `../` или абсолютные пути.

### Ошибка `KeyError: 'PROXY_API_KEY'`
- В `view/g_eval_test.py` переменная читается как `os.environ["PROXY_API_KEY"]`.
- Добавьте переменную в окружение или `.env` (и убедитесь, что `python-dotenv` установлен).

### Сетевые ошибки / 401 / 403 / timeouts при `g_eval_test.py`
- Проверьте ключ, base_url’ы ProxyAPI и доступность сети.
- Для Gemini HTTP адаптера: проверьте, что endpoint ожидает заголовок `x-goog-api-key`.

### Пустой/неожиданный промпт из `context/prompt_generator.py`
- На текущий момент это ожидаемо: `fill_context()` возвращает пустую строку, а `generate_prompt()` не вставляет заполненный промпт.
- Нужна реализация (см. раздел “нуждается в проверке”).


## 8) References

- DeepEval: https://docs.confident-ai.com/ (проверьте актуальный URL для `deepeval`)
- OpenAI Python SDK: https://github.com/openai/openai-python
- LangChain Core prompts: https://python.langchain.com/docs/modules/model_io/prompts/
- ProxyAPI (используется в коде): **нуждается в ссылке/проверке**


---

## TODO / Needs verification (быстрый чеклист)
- [ ] Добавить `requirements.txt` или `pyproject.toml` с зафиксированными зависимостями.
- [ ] Реализовать `context/context_generator.py` или удалить, если не нужен.
- [ ] Починить `context/prompt_generator.py` (f-string для имени промпта + реальная подстановка контекста).
- [ ] Добавить минимальные автоматические тесты (`pytest`).
- [ ] Документировать формат `{game}` и `{quest_format}` (где хранится схема YAML квеста).
