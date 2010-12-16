from django.conf import settings
import django

DJANGO10_COMPAT = django.VERSION[0] < 1 or (django.VERSION[0] == 1 and django.VERSION[1] < 1)

STATIC_URL = getattr(settings, 'STATIC_URL', settings.MEDIA_URL)
MEDIA_PATH = getattr(settings, 'EDITOR_MEDIA_PATH', '%s/editor/' % STATIC_URL)
