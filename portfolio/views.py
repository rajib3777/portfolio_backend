from rest_framework import generics
from .models import (
    HeroSection, AboutSection, SkillCategory, Project,
    Experience, Education, SocialLink, Stats
)
from .serializers import (
    HeroSectionSerializer, AboutSectionSerializer, SkillCategorySerializer,
    ProjectSerializer, ExperienceSerializer, EducationSerializer,
    SocialLinkSerializer, StatsSerializer
)


class HeroDetailView(generics.RetrieveAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

    def get_object(self):
        return HeroSection.objects.first()


class AboutDetailView(generics.RetrieveAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

    def get_object(self):
        return AboutSection.objects.first()


class SkillCategoryListView(generics.ListAPIView):
    queryset = SkillCategory.objects.prefetch_related('skills').all()
    serializer_class = SkillCategorySerializer


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = Project.objects.all().order_by('-created_at')
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')

        if category:
            qs = qs.filter(category__name__iexact=category)
        if search:
            qs = qs.filter(title__icontains=search)
        return qs


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all().order_by('-start_date')
    serializer_class = ExperienceSerializer


class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all().order_by('-start_year')
    serializer_class = EducationSerializer


class SocialLinkListView(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class StatsDetailView(generics.RetrieveAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    def get_object(self):
        return Stats.objects.first()
