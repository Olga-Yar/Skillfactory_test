import numpy as np


def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше и ли меньше.
    Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return count


if __name__ == '__main__':
    print(random_predict())
    