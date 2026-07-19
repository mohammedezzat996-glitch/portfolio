from django.contrib import admin
from .models import Project, Category, Skill, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # تم تعديل sent_at إلى created_at لتتوافق مع الموديل الجديد
    list_display = ('name', 'subject', 'created_at') 
    readonly_fields = ('created_at',)