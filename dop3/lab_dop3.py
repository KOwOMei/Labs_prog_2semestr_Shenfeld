import re
from functools import reduce
from collections import OrderedDict

def sort_news(news): # Объявляем функцию по поиску нужных хороших новостей.
    """Функция сортирует набор новостей и выбирает самые положительные в порядке возрастания 'Силы Позитива'. Формат данных: news - наш словарь формата 'Сила_Позитива - Заголовок_Новости';
    На выходе получаем список новостей, выбранных во возрастанию 'Силы Позитива'. """
    mem = 0
    st = "0"
    all_rating = OrderedDict()
    all_rating[mem] = None
    for i in news:
        k = 1
        st_mem = all_rating[mem]
        while st.isdigit():
            st = str(i)[0:k]
            k += 1
        st = st[:-1]
        mem = reduce(lambda a,b: a if (a > b) else b, [int(st),mem])
        all_rating[mem] = re.sub(f"{mem} ", '', i) if (mem in all_rating.keys()) == False else st_mem
    all_rating.pop(0)
    return all_rating


with open(r"news.txt", "r", encoding="utf-8") as file: # Открываем наш файл через кодировку utf-8.
    news_base = list(file)

print("Starting to sort well-based news...")
sorted_news = sort_news(news_base)

if sorted_news != []:
    print("Here's your good news! \n")
    for i in sorted_news.keys():
        print(''.join(str(sorted_news[i])))
