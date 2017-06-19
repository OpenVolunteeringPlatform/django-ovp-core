from django.conf import settings
from django.utils.translation import ugettext as _
import importlib

def get_settings(string="OVP_CORE"):
  return getattr(settings, string, {})


def import_from_string(val):
  try:
    # Nod to tastypie's use of importlib.
    parts = val.split('.')
    module_path, class_name = '.'.join(parts[:-1]), parts[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_name)
  except ImportError as e:
    msg = "Could not import '%s' for setting. %s: %s." % (val, e.__class__.__name__, e)
    raise ImportError(msg)


def is_email_enabled(email):
  """ Emails are activated by default. Returns false
      if an email has been disabled in settings.py
  """
  s = get_settings(string="OVP_EMAILS")
  email_settings = s.get(email, {})

  enabled = True
  if email_settings.get("disabled", False):
    enabled = False

  return enabled


def get_email_subject(email, default):
  """ Allows for email subject overriding from settings.py  """
  s = get_settings(string="OVP_EMAILS")
  email_settings = s.get(email, {})

  title = email_settings.get("subject", default)

  return _(title)


def get_address_model():
  """ Returns application address model

  The address model can be modified by setting OVP_CORE.ADDRESS_MODEL.

  Returns:
    class: Address model class

    The default model returned is ovp_core.models.GoogleAddress

  """
  model_name = get_settings().get("ADDRESS_MODEL", "ovp_core.models.GoogleAddress")
  return import_from_string(model_name)
