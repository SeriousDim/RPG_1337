# Поддержка log_probs в разных моделях

Посмотреть значение поля `model_data.supports_log_propb` можно в конструкторе, найдя примерно такую строку:

```
self.model_data = ANTHROPIC_MODELS_DATA.get(model)
```

## ProxyAPI

| Модель | log_probs |
|---|---|
| gpt-5.2 | Надо прописывать параметр `model.model_data.supports_log_probs = True` |
| gpt-4-turbo | Да |
| claude-sonnet-4-6 | Не поддерживается |
| gemini-2.5-pro | Не поддерживается |
| gemini-2.0-flash | Поддерживается, нужно делать обработку |
| gemini-XXX | ? |
| deepseek/deepseek-v3.2 | Не поддерживается |
| OpenRouter модели | Зависит от модели (пока не нашел ни одну) |

| Модель | log_probs |
|---|---|
| YandexGPT | ? |
| GigaChat 2 | Не поддерживается  |
