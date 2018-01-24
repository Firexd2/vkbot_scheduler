from django.test import TestCase
from .tools import *


class TestQueryAnalyzeres(TestCase):

    def test_analyzer_every_day(self):
        query = '!каждыйдень Тест 10:00,13:00,15:00 Это-сообщение-прошу-повторить-мне 4'
        query_analyzer_every_day(query, 123)

        r = ScheduleEveryDay.objects.get(id=1)

        self.assertEqual(r.uid, 123)
        self.assertEqual(r.name, 'Тест')
        self.assertEqual(r.message, 'Это сообщение прошу повторить мне')

        all_times = r.times.all()
        self.assertTrue(len(all_times) == 3)

        self.assertEqual(all_times[0].time, '10:00')
        self.assertEqual(all_times[1].time, '13:00')
        self.assertEqual(all_times[2].time, '15:00')

        self.assertEqual(all_times[0].repeat_count, 4)
        self.assertEqual(all_times[1].repeat_count, 4)
        self.assertEqual(all_times[2].repeat_count, 4)

    def test_analyzer_every_week(self):
        query = '!каждуюнеделю Тест пн,ср,пт Это-задание,-повторяем-,каждую-неделю'
        query_analyzer_every_week(query, 123)

        r = ScheduleEveryWeek.objects.get(id=1)

        self.assertEqual(r.uid, 123)
        self.assertEqual(r.name, 'Тест')

        week_day = r.week_day.split(',')
        self.assertEqual(week_day[0], 'пн')
        self.assertEqual(week_day[1], 'ср')
        self.assertEqual(week_day[2], 'пт')

        self.assertEqual(r.message, 'Это задание, повторяем ,каждую неделю')

    def test_analyzer_every_year(self):
        query = '!каждыйгод Год 24.01 Повторяем-каждый-год'
        query_analyzer_every_year(query, 123)

        r = ScheduleEveryYear.objects.get(id=1)

        self.assertEqual(r.uid, 123)
        self.assertEqual(r.name, 'Год')
        self.assertEqual(r.message, 'Повторяем каждый год')
        self.assertEqual(r.day, '24.01')

    def test_analyzer_day(self):
        query = '!день ДеньРождение 01.02.2018-10:30 Сегодня-день-рождение'
        query_analyzer_day(query, 123)

        r = ScheduleDay.objects.get(id=1)

        self.assertEqual(r.uid, 123)
        self.assertEqual(r.name, 'ДеньРождение')

        tz = timezone('Europe/Moscow')
        self.assertEqual(r.day, datetime.datetime(2018, 2, 1, 10, 30, tzinfo=tz))
        self.assertEqual(r.message, 'Сегодня день рождение')
