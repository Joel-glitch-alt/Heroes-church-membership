from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Member

# PDF export action
def export_members_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="members.pdf"'

    p = canvas.Canvas(response)
    y = 800

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, y, "Members List")
    y -= 40

    # Table header
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Full Name")
    p.drawString(200, y, "Contact")
    p.drawString(350, y, "Location")
    p.drawString(450, y, "Invited By")
    y -= 20
    p.setFont("Helvetica", 10)

    for member in queryset:
        p.drawString(50, y, member.full_name)
        p.drawString(200, y, member.contact)
        p.drawString(350, y, member.location)
        invited_by = member.invited_by.full_name if member.invited_by else "-"
        p.drawString(450, y, invited_by)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    return response

export_members_pdf.short_description = "Export selected members to PDF"

# Admin registration
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'contact', 'location', 'invited_by', 'date_joined', 'created_at')
    search_fields = ('first_name', 'last_name', 'location', 'contact')
    list_filter   = ('date_joined', 'location')
    ordering      = ('-created_at',)
    list_per_page = 5  # Pagination
    actions = [export_members_pdf]  # <-- add the PDF export action here

    fieldsets = (
        ('Personal details', {
            'fields': ('first_name', 'last_name', 'contact', 'location', 'date_joined')
        }),
        ('Referral', {
            'fields': ('invited_by',)
        }),
    )