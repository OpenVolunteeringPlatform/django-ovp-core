from ovp_core.serializers import GoogleAddressSerializer

def address_validate(address):
  address_sr = GoogleAddressSerializer(data=address)
  address_sr.is_valid(raise_exception=True)
