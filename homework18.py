import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("homework.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def divide(a, b):
    logger.debug("Виклик divide(a=%s, b-%s)", a, b)

    try:
        result = a / b
    except ZeroDivisionError:
        logger.error("Помилка: ділення на нуль (a=%s, b=%s)", a, b)

        return None

    logger.info("Результат ділення %s / %s = %s", a, b, result)

divide(10, 2)
divide(10, 0)