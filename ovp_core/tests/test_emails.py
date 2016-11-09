from django.test import TestCase
from django.core import mail

import ovp_core.emails

class TestBaseMail(TestCase):
  def test_email_trigger(self):
    """Assert that email is sent to outbox"""
    bm = ovp_core.emails.BaseMail('a@b.c')
    bm.sendEmail('base', '', {})
    self.assertTrue(len(mail.outbox) > 0)

  def test_async_email_trigger(self):
    """Assert that async emails are sent to outbox"""
    bm = ovp_core.emails.BaseMail('a@b.c', async_mail=True)
    bm.sendEmail('base', '', {}).join()
    self.assertTrue(len(mail.outbox) > 0)
