from django.db import models

class ResumeFile(models.Model):
    """
    Optional manual upload (যদি চাই future এ ready-made PDF upload করতে)
    """
    file = models.FileField(upload_to="resumes/", blank=True, null=True)

    def __str__(self):
        return "Uploaded Resume"