import numpy as np


def game_core_v3(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    count = 0
    low, high = 1, 100  # Начальные границы
    predict = (low + high) // 2  # Начальное предсказание

    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1  # Увеличиваем нижнюю границу
        else:
            high = predict - 1  # Уменьшаем верхнюю границу
        
        predict = (low + high) // 2  # Обновляем предсказание   
            
    
    return count


if __name__ == '__main__':
    print(game_core_v3(1))