class QuestValidationError(Exception):
    """Ошибка валидации квеста с человекочитаемым сообщением."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

