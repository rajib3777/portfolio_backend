from rest_framework import generics, permissions
from .models import Project, ProjectCategory
from .serializers import ProjectSerializer, ProjectCategorySerializer

class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Project.objects.all()
        category = self.request.query_params.get("category")
        search = self.request.query_params.get("search")
        featured = self.request.query_params.get("featured")

        if category:
            qs = qs.filter(category__name__iexact=category)
        if search:
            qs = qs.filter(title__icontains=search)
        if featured == "true":
            qs = qs.filter(featured=True)

        return qs


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"
    permission_classes = [permissions.AllowAny]


class ProjectCategoryListView(generics.ListAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [permissions.AllowAny]
