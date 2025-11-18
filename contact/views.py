from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        message_obj = serializer.save()
        # optional email
        try:
            send_mail(
                subject=f"New Contact: {message_obj.subject}",
                message=message_obj.message,
                from_email=message_obj.email,
                recipient_list=[getattr(settings, "DEFAULT_FROM_EMAIL", "admin@example.com")],
                fail_silently=True,
            )
        except Exception:
            pass
