from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers


def is_csv_file(file: UploadedFile):
    """Raise validation error if file is not a CSV."""
    if file.content_type != 'text/csv':
        raise serializers.ValidationError('File must be a CSV')


def max_size_validator(file: UploadedFile):
    """Raise validation error if file is too large."""
    if file.size > 536870912:
        raise serializers.ValidationError('File must not exceed 500MB')


FILE_VALIDATORS = [is_csv_file, max_size_validator]


class FileUploadSerializer(serializers.Serializer):
    """"Serializer for file upload."""
    source_file = serializers.FileField(max_length=255,
                                        allow_empty_file=False,
                                        validators=FILE_VALIDATORS)
    target_file = serializers.FileField(max_length=255,
                                        allow_empty_file=False,
                                        validators=FILE_VALIDATORS)
