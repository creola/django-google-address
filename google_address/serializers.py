from google_address import models
from rest_framework import serializers


class GoogleAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.GoogleAddress
    fields = ['raw', 'raw2', 'address_line', 'city_state']
    read_only_fields = ['address_line', 'city_state']


class GoogleAddressLatLngSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.GoogleAddress
    fields = ['raw', 'raw2', 'address_line', 'city_state', 'lat', 'lng']
    read_only_fields = ['address_line', 'city_state']


class GoogleAddressCityStateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.GoogleAddress
    fields = ['city_state']

