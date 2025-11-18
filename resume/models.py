from django.db import models

class ResumeFile(models.Model):
    
    file = models.FileField(upload_to="resumes/", blank=True, null=True)

    def __str__(self):
        return "Uploaded Resume"