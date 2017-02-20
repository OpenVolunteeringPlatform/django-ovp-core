from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template
from django.template.loader import get_template
from django.conf import settings
from django.utils import translation

from ovp_core.helpers import get_settings, is_email_enabled, get_email_subject

import threading

class EmailThread(threading.Thread):
  def __init__(self, msg):
    self.msg = msg
    threading.Thread.__init__(self)

  def run (self):
    return self.msg.send() > 0


class BaseMail:
  """
  This class is responsible for firing emails
  """
  from_email = ''

  def __init__(self, email_address, async_mail=None, locale=None):
    self.email_address = email_address
    self.async_mail = async_mail
    self.locale = locale or get_settings().get('LANGUAGE_CODE', 'en-us')

  def sendEmail(self, template_name, subject, context={}):
    if not is_email_enabled(template_name):
      return False

    subject = get_email_subject(template_name, subject)

    self.__setLocale()
    ctx = Context(inject_client_url(context))
    text_content = get_template('email/{}.txt'.format(template_name)).render(ctx)
    html_content = get_template('email/{}.html'.format(template_name)).render(ctx)
    self.__resetLocale()

    msg = EmailMultiAlternatives(subject, text_content, self.from_email, [self.email_address])
    msg.attach_alternative(html_content, "text/html")

    if self.async_mail:
      async_flag="async"
    elif self.async_mail == None:
      async_flag=getattr(settings, "DEFAULT_SEND_EMAIL", "async")

    if async_flag == "async":
      t = EmailThread(msg)
      t.start()
      result = t
    else:
      result = msg.send() > 0

    return result

  def __setLocale(self):
    self.__active_locale = translation.get_language()
    translation.activate(self.locale)

  def __resetLocale(self):
    translation.activate(self.__active_locale)
    self.__active_locale = None

class ContactFormMail(BaseMail):
  """
  This class is reponsible for firing emails sent through the contact form
  """
  def __init__(self, recipients, async_mail=None):
    self.recipients = recipients
    self.async = async_mail

  def sendContact(self, context={}):
    """
    Send contact form message to single or multiple recipients
    """
    for recipient in self.recipients:
      super(ContactFormMail, self).__init__(recipient, self.async)
      self.sendEmail('contactForm', 'New contact form message', context)


#
# Helpers
#

def inject_client_url(ctx):
  s = get_settings()
  ctx['CLIENT_URL'] = s.get("CLIENT_URL", "")
  return ctx
