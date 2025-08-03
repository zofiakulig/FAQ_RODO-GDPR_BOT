from django.db import models

class FAQ(models.Model):
    LANG_CHOICES = [
        ('pl', 'Polski'),
        ('en', 'English'),
    ]

    question = models.CharField(max_length=300)
    answer = models.TextField()
    language = models.CharField(max_length=2, choices=LANG_CHOICES, default='pl')

    def __str__(self):
        return f"[{self.language.upper()}] {self.question}"
