from django.conf import settings

def get_settings():
  return getattr(settings, "OVP_CORE", {})
