import re


def filter_every_day(query):
    """
    [Тест, 10:00,13:00,15:00, Это-сообщение-прошу-повторить-мне]
    """
    if len(query) != 3:
        return 'Запрос неверен. Попробуй еще раз. \n\n' \
               'Пример: !кд Таблетка 10:00,13:00,15:00 Не-забудь-выпить-таблетку \n\n' \
               'Где: !кд - команда, Таблетка - название, 10:00,13:00,15:00 - время напоминания, ' \
               'Не-забудь-выпить-таблетку - сообщение, которое будет тебе выслано в нужное время. Заместо пробелов ' \
               'необходимо использовать "-".'

    for time in query[1].split(','):
        if not re.match(r'\d\d:\d\d', time):
            return 'Ошибка в записи времени. Время должно быть записано в формате 00:00,00:01, ' \
                   'через запятую и без пробелов.'


def filter_every_week(query):
    """
    Тест пн,ср,пт 10:30 Это-задание,-повторяем-,каждую-неделю-в-10:30
    """
    if len(query) != 4:
        return 'Запрос неверен. Попробуй еще раз. \n\n' \
               'Пример: !кн ЗвонокДругану пн,ср,пт 10:30 Позвони-другану-срочно \n\n' \
               'Где: !кн - команда, ЗвонокДругану - название, пн,ср,пт - дни недели напоминания, ' \
               '10:30 - время, Позвони-другану-срочно - сообщение, которое будет' \
               ' тебе выслано в нужное время. В сообщении заместо пробелов необходимо использовать "-".'

    days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    for day in query[1].split(','):
        if day not in days:
            return 'Ошибка в записи дней недели. Дни недели должны быть записаны в двухбуквенном формате ' \
                   'через запятую БЕЗ пробелов. Например: пн,ср,пт.'

    if not re.match(r'\d\d:\d\d', query[2]):
        return 'Ошибка в записи времени. Время должно быть записано в формате 00:00.'


def filter_every_month(query):
    """
    Месяц 1,5,8,26 9:30 Напоминаем-о-молочке
    """
    if len(query) != 4:
        return 'Запрос неверен. Попробуй еще раз. \n\n' \
               'Пример: !км СобратьДань 1,5,8,10 20:30 Собрать-дань-с-холопов \n\n' \
               'Где: !км - команда, СобратьДань - название, 1,5,8,10 - числа месяца напоминания, ' \
               '20:30 - время, Собрать-дань-с-холопов - сообщение, которое будет тебе' \
               ' выслано в нужное время. Заместо пробелов необходимо использовать "-".'

    for day in query[1].split(','):
        if not day.isdigit():
            return 'Ошибка записи чисел месяца. Числа должны быть записаны через запятую БЕЗ пробелов.'

    if not re.match(r'\d\d:\d\d', query[2]):
        return 'Ошибка в записи времени. Время должно быть записано в формате 00:00.'


def filter_every_year(query):
    """
    Год 24.01 09:00 Повторяем-каждый-год
    """

    if len(query) != 4:
        return 'Запрос неверен. Попробуй еще раз. \n\n' \
               'Пример: !кг ДеньРождениеДругана 24.01 20:30 Поздравить-друга \n\n' \
               'Где: !кг - команда, ДеньРождениеДругана - название, 24.01 - число и месяц напоминания, ' \
               '20:30 - время, Поздравить-друга - сообщение, которое будет тебе' \
               ' выслано в нужное время. Заместо пробелов необходимо использовать "-".'

    if not re.match(r'\d\d.\d\d', query[1]):
        return 'Ошибка в записи даты. Дата должна быть представлена в виде dd.mm, например: 24.01'

    if not re.match(r'\d\d:\d\d', query[2]):
        return 'Ошибка в записи времени. Время должно быть записано в формате 00:00.'


def filter_day(query):
    """
    ДеньРождение 01.02.2018-10:50 Сегодня-день-рождение
    """

    if len(query) != 3:
        return 'Запрос неверен. Попробуй еще раз. \n\n' \
               'Пример: !д ВажныйДень 01.02.2018-10:50 Напоминаю-о-важном-дне \n\n' \
               'Где: !д - команда, ВажныйДень - название, 01.02.2018-10:50 - дата и время напоминания, ' \
               'Напоминаю-о-важном-дне - сообщение, которое будет тебе' \
               ' выслано в нужное время. Заместо пробелов необходимо использовать "-".'

    if not (re.match(r'\d\d.\d\d.\d\d\d\d-\d\d:\d\d', query[1])
            or query[1][:7].lower() == 'сегодня' or query[1][:6].lower() == 'завтра'):

        return 'Ошибка записи даты и времени. Время и дата должны быть записаны в виде 01.02.2018-10:50'
