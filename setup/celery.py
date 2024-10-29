from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Configura o Celery com o settings do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('sectrans')

# Lê configurações do Celery do settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre automaticamente as tasks dos apps Django
app.autodiscover_tasks()