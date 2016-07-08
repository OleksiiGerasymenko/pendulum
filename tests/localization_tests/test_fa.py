# -*- coding: utf-8 -*-

from pendulum import Pendulum

from .. import AbstractTestCase
from . import AbstractLocalizationTestCase



class FaTest(AbstractLocalizationTestCase, AbstractTestCase):

    locale = 'fa'

    def diff_for_humans(self):
        with self.wrap_with_test_now():
            d = Pendulum.now().sub(seconds=1)
            self.assertEqual('1 ثانیه پیش', d.diff_for_humans())

            d = Pendulum.now().sub(seconds=2)
            self.assertEqual('2 ثانیه پیش', d.diff_for_humans())

            d = Pendulum.now().sub(minutes=1)
            self.assertEqual('1 دقیقه پیش', d.diff_for_humans())

            d = Pendulum.now().sub(minutes=2)
            self.assertEqual('2 دقیقه پیش', d.diff_for_humans())

            d = Pendulum.now().sub(hours=1)
            self.assertEqual('1 ساعت پیش', d.diff_for_humans())

            d = Pendulum.now().sub(hours=2)
            self.assertEqual('2 ساعت پیش', d.diff_for_humans())

            d = Pendulum.now().sub(days=1)
            self.assertEqual('1 روز پیش', d.diff_for_humans())

            d = Pendulum.now().sub(days=2)
            self.assertEqual('2 روز پیش', d.diff_for_humans())

            d = Pendulum.now().sub(weeks=1)
            self.assertEqual('1 هفته پیش', d.diff_for_humans())

            d = Pendulum.now().sub(weeks=2)
            self.assertEqual('2 هفته پیش', d.diff_for_humans())

            d = Pendulum.now().sub(months=1)
            self.assertEqual('1 ماه پیش', d.diff_for_humans())

            d = Pendulum.now().sub(months=2)
            self.assertEqual('2 ماه پیش', d.diff_for_humans())

            d = Pendulum.now().sub(years=1)
            self.assertEqual('1 سال پیش', d.diff_for_humans())

            d = Pendulum.now().sub(years=2)
            self.assertEqual('2 سال پیش', d.diff_for_humans())

            d = Pendulum.now().add(seconds=1)
            self.assertEqual('1 ثانیه بعد', d.diff_for_humans())

            d = Pendulum.now().add(seconds=1)
            d2 = Pendulum.now()
            self.assertEqual('1 ثانیه پس از', d.diff_for_humans(d2))
            self.assertEqual('1 ثانیه پیش از', d2.diff_for_humans(d))

            self.assertEqual('1 ثانیه', d.diff_for_humans(d2, True))
            self.assertEqual('2 ثانیه', d2.diff_for_humans(d.add(seconds=1), True))
