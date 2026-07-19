import os

from django.core.wsgi import get_wsgi_application

# تم ضبط اسم المجلد بدقة هنا لتفادي أي خطأ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()