import os
CHAPA_SECRET_KEY = os.getenv("CHAPA_SECRET_KEY")
# Celery settings
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Email backend (example using console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'noreply@example.com'
