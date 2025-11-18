from django.contrib import admin
from .models import (
    HeroSection, AboutSection, SkillCategory, Skill,
    Experience, Education, SocialLink, Stats
)

admin.site.register(HeroSection)
admin.site.register(AboutSection)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(SocialLink)
admin.site.register(Stats)