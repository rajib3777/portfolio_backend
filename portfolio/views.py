from rest_framework import generics, permissions
from .models import (
    HeroSection, AboutSection, SkillCategory,
    Experience, Education, SocialLink, Stats
)
from .serializers import (
    HeroSectionSerializer, AboutSectionSerializer, SkillCategorySerializer,
    ExperienceSerializer, EducationSerializer, SocialLinkSerializer,
    StatsSerializer
)

class HeroDetailView(generics.RetrieveAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return HeroSection.objects.first()


class AboutDetailView(generics.RetrieveAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return AboutSection.objects.first()


class SkillCategoryListView(generics.ListAPIView):
    queryset = SkillCategory.objects.prefetch_related("skills").all()
    serializer_class = SkillCategorySerializer
    permission_classes = [permissions.AllowAny]


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all().order_by("-start_date")
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all().order_by("-start_year")
    serializer_class = EducationSerializer
    permission_classes = [permissions.AllowAny]


class SocialLinkListView(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [permissions.AllowAny]


class StatsDetailView(generics.RetrieveAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return Stats.objects.first()