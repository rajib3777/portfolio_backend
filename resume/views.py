from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

from portfolio.models import (
    HeroSection, AboutSection, Education, Experience,
    SkillCategory
)
from projects.models import Project

def dynamic_resume(request):
    """
    তোমার portfolio + projects ডাটা নিয়ে
    একটায় professional resume PDF বানাবে।
    """

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="resume.pdf"'

    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    styles = getSampleStyleSheet()
    elements = []

    hero = HeroSection.objects.first()
    about = AboutSection.objects.first()

    # Header
    if hero:
        elements.append(Paragraph(f"<b>{hero.name}</b>", styles["Title"]))
        elements.append(Paragraph(hero.title, styles["Heading2"]))
        elements.append(Spacer(1, 12))

    if about:
        contact_line = f"{about.location} | {about.email} | {about.phone}"
        elements.append(Paragraph(contact_line, styles["Normal"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(about.short_bio, styles["BodyText"]))
        elements.append(Spacer(1, 20))

    # Education
    elements.append(Paragraph("<b>Education</b>", styles["Heading2"]))
    for edu in Education.objects.all():
        line = f"{edu.degree} - {edu.institution} ({edu.start_year}-{edu.end_year})"
        elements.append(Paragraph(line, styles["BodyText"]))
    elements.append(Spacer(1, 16))

    # Experience
    elements.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
    for exp in Experience.objects.all():
        duration = f"{exp.start_date} - {'Present' if exp.is_current else exp.end_date}"
        line = f"{exp.role} @ {exp.company} ({duration})"
        elements.append(Paragraph(line, styles["BodyText"]))
        if exp.description:
            elements.append(Paragraph(exp.description, styles["BodyText"]))
        elements.append(Spacer(1, 8))
    elements.append(Spacer(1, 16))

    # Skills
    elements.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
    for cat in SkillCategory.objects.all():
        elements.append(Paragraph(f"<b>{cat.name}</b>", styles["BodyText"]))
        skills_line = ", ".join([s.name for s in cat.skills.all()])
        elements.append(Paragraph(skills_line, styles["BodyText"]))
    elements.append(Spacer(1, 16))

    # Projects
    elements.append(Paragraph("<b>Projects</b>", styles["Heading2"]))
    for proj in Project.objects.all():
        elements.append(Paragraph(f"<b>{proj.title}</b>", styles["BodyText"]))
        elements.append(Paragraph(proj.description[:200] + "...", styles["BodyText"]))
        tech = f"Tech: {proj.tech_stack}"
        elements.append(Paragraph(tech, styles["BodyText"]))
        elements.append(Spacer(1, 8))

    doc.build(elements)
    return response
