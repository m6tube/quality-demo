"""Модуль с функциями калькулятора."""

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание двух чисел."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление двух чисел."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b