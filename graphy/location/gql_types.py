from graphene_django import DjangoObjectType

from graphy.location.models import Address, County, Municipality, ZipCode


class CountyType(DjangoObjectType):
    class Meta:
        model = County
        only_fields = ('id', 'name', 'code', 'country')


class MunicipalityType(DjangoObjectType):
    class Meta:
        model = Municipality
        only_fields = ('id', 'name', 'county')


class ZipCodeType(DjangoObjectType):
    class Meta:
        model = ZipCode
        only_fields = ('id', 'code', 'name', 'municipality', 'county')


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        only_fields = (
            'id',
            'street_address',
            'zip_code',
            'country',
            'latitude',
            'longitude',
        )