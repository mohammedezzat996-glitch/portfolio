from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "القسم"
        verbose_name_plural = "الأقسام"


class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم المهارة")
    proficiency = models.IntegerField(default=100, verbose_name="نسبة الإتقان (%)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "المهارة"
        verbose_name_plural = "المهارات"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المشروع")
    description = models.TextField(verbose_name="وصف المشروع الكامل")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="القسم")
    live_link = models.URLField(blank=True, null=True, verbose_name="رابط معاينة حية للمشروع")
    
    # التعديل الجديد لرابط جوجل درايف هنا
    code_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="رابط تحميل المشروع (Google Drive)")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "المشروع"
        verbose_name_plural = "المشاريع"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المرسل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    subject = models.CharField(max_length=200, verbose_name="العنوان / الموضوع")
    message = models.TextField(verbose_name="نص الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإرسال")

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "رسالة التواصل"
        verbose_name_plural = "رسائل التواصل"