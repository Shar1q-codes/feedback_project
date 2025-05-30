from django.db import models

class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ('feedback', 'Feedback'),
        ('complaint', 'Complaint'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
