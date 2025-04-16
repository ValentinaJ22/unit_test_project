# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils.timezone import make_aware
from mixer.backend.django import mixer
from datetime import datetime
from courses.models import Course, Student
import pytest
import mock
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

     def test_calculate_approval_percentage(self):
          student = Student()

          # Datos de entrada válidos
          score_correct = 4.0
          scale_correct_5 = 5
          scale_correct_10 = 10

          # Datos incorrectos o no numéricos
          score_string = '3'
          score_zero = 0
          scale_zero = 0
          scale_string = '1 - 10'

          # Pruebas con entradas válidas
          assert student.approval_percentage(score_correct, scale_correct_5) == 80
          assert student.approval_percentage(score_correct, scale_correct_10) == 40
          assert student.approval_percentage(score_string, scale_correct_5) == "La nota debe ser un número"
          assert student.approval_percentage(score_zero, scale_correct_5) == 0
          assert student.approval_percentage(score_correct, scale_string) == "La escala debe ser un número"
          assert student.approval_percentage(score_correct, scale_zero) == "La escala no puede ser cero"

     def test_student_registration(self): 
          #Creamos un mock de tipo course para usar su método is_available como verdadero 
          course_available = mock.Mock(Course) 
          #Creamos un mock de tipo course para usar su método is_available como falso 
          course_not_available = mock.Mock(Course) #definimos que el metodo is_available del mock course_available retorne un valor verdadero 
          course_available.is_available = True 
          #definimos que el metodo is_available del mock course_not_available retorne un valor falso 
          course_not_available.is_available = False #creamos el objeto student 
          student = Student() 
          #verificamos la respuesta 
          assert student.student_registration(course_available) == "Estudiante puede matricularse" 
          assert student.student_registration(course_not_available) == "Estudiante no se puede matricular"

     def test_approved_course(self):
          # Creamos un mock de tipo Student para usar su propiedad approval_percentage como aprobado
          student_approval = mock.Mock(Student)
          # Creamos un mock de tipo Student para usar su propiedad approval_percentage como no aprobado
          student_not_approval = mock.Mock(Student)
          
          # Definimos que el atributo approval_percentage del mock aprobado tenga un valor numérico >= 90
          student_approval.approval_percentage = 95  
          # Definimos que el atributo approval_percentage del mock no aprobado tenga un valor menor a 90
          student_not_approval.approval_percentage = 80  
          
          # Creamos el objeto real student
          student = Student()
          
          # Verificamos la respuesta: ajustamos las cadenas de comparación para que coincidan
          assert student.approved_course(student_approval) == "El estudiante aprobo el curso"
          assert student.approved_course(student_not_approval) == "El estudiante no aprobo el curso"
