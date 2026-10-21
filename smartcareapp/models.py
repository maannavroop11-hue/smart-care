from django.db import models

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ("general", "General Enquiry"),
        ("services", "Healthcare Services"),
        ("appointment", "Appointment Enquiry"),
        ("feedback", "Feedback"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default="general"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"