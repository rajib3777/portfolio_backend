from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Optional: send email to you
        send_mail(
            subject=f"New contact: {instance.subject}",
            message=instance.message,
            from_email=instance.email,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True
        )
