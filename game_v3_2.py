import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Задаем мин и макс границу предсказания.
    Далее в зависимости от больше или меньшего значения увеличиваем/уменьшаем границы.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    low, high = 1, 100  
    predict = (low + high) // 2  

    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1  # Увеличиваем нижнюю границу
        else:
            high = predict - 1  # Уменьшаем верхнюю границу
        
        predict = (low + high) // 2    
            
    
    return count


if __name__ == '__main__':
    print(game_core_v3(1))