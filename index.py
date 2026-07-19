import os
import sys

# توجيه بايثون لقراءة المجلدات الداخلية للمشروع
sys.path.append(os.path.join(os.path.dirname(__file__), 'My_Portfolio_Project'))

# استدعاء تطبيق الـ WSGI الخاص بدجانغو
from portfolio_project.wsgi import application
