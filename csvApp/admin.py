from django.contrib import admin
from .models import Document, Validate
# Register your models here.

class ValidateInline(admin.StackedInline):
    model = Validate
    extra = 1
class DocumentAdmin(admin.ModelAdmin):
      inlines = [ValidateInline]    
admin.site.register(Document, DocumentAdmin)
admin.site.register(Validate)