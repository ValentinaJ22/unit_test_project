# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    
    @property
    def is_available(self):
        date = timezone.now()
        if self.start_date <= date and date <= self.end_date:
            return True
        else:
            return False
        

class Student:
    def approval_percentage(self, score, scale):
        # Validar que 'score' sea numérico.
        if not isinstance(score, (int, float)):
            return "La nota debe ser un número"
        # Validar que 'scale' sea numérico.
        if not isinstance(scale, (int, float)):
            return "La escala debe ser un número"
        # Verificar si la escala es cero para evitar división por cero.
        if scale == 0:
            return "La escala no puede ser cero"
        try:
            result = (score * 100) / scale
            return result
        except Exception as error:
            return f"Error: {error}"
        
    def student_registration(self, course): 
        if course.is_available: 
            return "Estudiante puede matricularse" 
        else:
            return "Estudiante no se puede matricular"

    def approved_course(self, student): 
        if student.approval_percentage >= 90: 
            return "El estudiante aprobo el curso" 
        else: 
            return "El estudiante no aprobo el curso"