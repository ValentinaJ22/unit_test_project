# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils.timezone import make_aware
from mixer.backend.django import mixer
from datetime import datetime
import pytest

@pytest.mark.django_db
class TestModels:

     def test_course_is_available(self):
          # Definimos un objeto tipo datetime a partir de una fecha en string
          start_date = make_aware(datetime.strptime("2020-01-01", "%Y-%m-%d"))
          end_date = make_aware(datetime.strptime("2020-12-12", "%Y-%m-%d"))

          # Simulamos un objeto de tipo Course
          course = mixer.blend('courses.Course', start_date=start_date, end_date=end_date)

          # Validamos que el test sea correcto
          assert course.is_available is False

     def test_course_is_available(self):
          # Definimos un objeto tipo datetime a partir de una fecha en string
          start_date = make_aware(datetime.strptime("2025-01-01", "%Y-%m-%d"))
          end_date = make_aware(datetime.strptime("2025-12-12", "%Y-%m-%d"))

          # Simulamos un objeto de tipo Course
          course = mixer.blend('courses.Course', start_date=start_date, end_date=end_date)

          # Validamos que el test sea correcto
          assert course.is_available is True
