"""
Задача №3. Топ аудио ВК
-----------------------

Файл: `audios.py`

Итак, люди найдены. Но с кем будет интереснее познакомиться в первую 
очередь? Олаф предложил узнать, кто какую музыку слушает - ведь если
совпадают музыкальные выкусы уже будет о чём поговорить!

У всех друзей нужно получить список их аудиозаписей и вывести в консоль 
5 самых популярных записей среди друзей введённого аккаунта.
"""

from friedns import get_credentials, get_friends_list


def get_audios_top(friends):
    pass  # TODO: для каждого друга из списка друзей сходить в ВК и получить список его записей.
          # Найти совпадения и вернуть список из названий пяти самых популярных аудио.


def output_audios_top_to_console(audios):
    pass  # TODO: вывести аудио-записи в консоль

if __name__ == '__main__':
    credentials = get_credentials()
    friends = get_friends_list(credentials)
    audios = get_audios_top(friends)
    output_audios_top_to_console(audios)
