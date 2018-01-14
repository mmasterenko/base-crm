from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .collection_tools import transform_values


class ReadableChoiceField(serializers.ChoiceField):

    """
    This Django Rest Framework field serializes and deserializes choices by the
    model field's human-readable choices.
    """

    def __init__(self, choices=None, transform=None, **kwargs):
        if choices is None:
            choices = []
        super().__init__(choices, **kwargs)
        self.transform = transform

    def bind(self, field_name, parent):
        super().bind(field_name, parent)

        if not self.choices:
            self.model_field = self.parent.Meta.model._meta.get_field(field_name)
            self.choices = dict(self.model_field.choices)

        if self.transform:
            self.choices = transform_values(self.choices, self.transform)

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for value, name in self.choices.items():
            if name == data:
                return value
        self.fail('invalid_choice', input=data)

    def to_representation(self, value):
        return self.choices[value]


class PasswordField(serializers.Field):
    """
    Converts password into hash

    store as: hash
    display as: hash
    """
    def to_representation(self, password):
        return password

    def to_internal_value(self, raw_password):
        return make_password(raw_password)
