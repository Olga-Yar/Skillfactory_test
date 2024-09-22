import numpy as np


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
if __name__ == '__main__':
    print(score_game())
    