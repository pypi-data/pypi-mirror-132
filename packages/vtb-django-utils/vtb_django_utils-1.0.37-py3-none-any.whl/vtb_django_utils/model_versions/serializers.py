from abc import ABCMeta
from functools import wraps

from django.db import transaction
from rest_framework import serializers


def create_version_decorator(func):
    @wraps(func)
    def __wrap(*args, **kwargs):
        validated_data = kwargs.get('validated_data', None) or args[-1]
        version = validated_data.pop('version', None)
        instance = func(*args, **kwargs)
        # Апдейтим версию version или создаем новую, если ее нет. Если version не указана, то создаем следующую
        _, model_version = instance.create_or_update_version(version)
        instance.version = model_version.version
        return instance

    return __wrap


class VersionedModelSerializer(serializers.ModelSerializer):
    __metaclass__ = ABCMeta
    version = serializers.CharField(required=False, allow_blank=True, allow_null=True, default='')
    last_version = serializers.CharField(source='last_version_query')
    version_list = serializers.ListField(source='version_list_query')

    class Meta:
        model = None

    @transaction.atomic()
    @create_version_decorator
    def create(self, validated_data):
        return super().create(validated_data)

    @transaction.atomic()
    @create_version_decorator
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
