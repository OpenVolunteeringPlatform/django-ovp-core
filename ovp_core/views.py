from rest_framework import response
from rest_framework import decorators
from rest_framework import status

from ovp_core import models
from ovp_core import serializers
from ovp_core import helpers
from ovp_core import emails

@decorators.api_view(["GET"])
def startup(request):
  """ This view provides initial data to the client, such as available skills and causes """
  skills = serializers.SkillSerializer(models.Skill.objects.all(), many=True)
  causes = serializers.CauseSerializer(models.Cause.objects.all(), many=True)

  return response.Response({
    "skills": skills.data,
    "causes": causes.data
  })


@decorators.api_view(["POST"])
def contact(request):
  settings = helpers.get_settings()
  valid_emails = settings.get("VALID_CONTACT_RECIPIENTS", [])

  name = request.data.get("name", "")
  message = request.data.get("message", "")
  email = request.data.get("email", "")
  recipients = request.data.get("recipients", [])
  context = {"name": name, "message": message, "email": email}

  # Check if all recipients are valid
  for recipient in recipients:
    if recipient not in valid_emails:
      return response.Response({"detail": "Invalid recipients."}, status.HTTP_400_BAD_REQUEST)


  contact = emails.ContactFormMail(recipients)
  contact.sendContact(context=context)

  return response.Response({"success": True})

