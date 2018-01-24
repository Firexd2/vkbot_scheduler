import datetime
from vkbot_schedule.models import *


def send_message(uid, message):
    return 1


def schedule_every_day_task():
    """
    Эта функция будет выполняться каждые пять минут для проверки задания.
    Если текущее время больше, чем в время указанное в задании, и это время не 'подтверждено',
    то отсылаем сообщение пользователю о том, что надо выполнить задание.
    """
    now_time = datetime.datetime.now().time().strftime("%H:%M") # текущее время
    for item in ScheduleEveryDay.objects.all(): # цикл обхода всех заданий в базе
        for time in item.times.all(): # проверка времени в задании
            if now_time >= time.time and time.repeat_count: # если текущее время больше и повторения не закончились
                send_message(item.uid, item.message) # уведомляем об этом пользователя
                time.repeat_count -= 1
                time.save()
                break


def schedule_every_week_task():
    """
    Это задание будет выполнятся каждый день для проверки еженедельных команд
    """
    days_of_week = {'пн': 1, 'вт': 2, 'ср': 3, 'чт': 4, 'пт': 5, 'сб': 6, 'вс': 7}
    now_day = datetime.datetime.now().isoweekday() # получение номера текущего дня
    for item in ScheduleEveryWeek.objects.all():
        for day in item.week_day.split(','):
            if days_of_week[day] == now_day:
                send_message(item.uid, item.message)


def schedule_every_year_task():
    """
    Это задание будет выполнятся каждый день для проверки и выполнения ежегодного задания
    """
    now_day = datetime.datetime.now().strftime('%d.%m') # текущая дата
    for item in ScheduleEveryYear.objects.all():
        if item.day == now_day:
            send_message(item.uid, item.message)


def schedule_day_task():

    now_datetime = datetime.datetime.now()
    for item in ScheduleDay.objects.all():
        if item.day <= now_datetime:
            send_message(item.uid, item.message)
            item.delete()

