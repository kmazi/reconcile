from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers

from reconcile.api.reconciliation.models import Report
from reconcile.api.reconciliation.normalizer import normalize
from reconcile.api.reconciliation.reconciler import reconcile_files


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

    def create(self, validated_data) -> Report:
        files = validated_data
        # Normalize the data
        normalized_source = normalize(data=files['source_file'])
        normalized_target = normalize(data=files['target_file'])
        # Reconcile the data
        report = reconcile_files(source=normalized_source,
                                 target=normalized_target)
        # Save file and report to database
        report = Report.objects.create(
            source_records_missing_in_target=report[
                'source_records_missing_in_target'],
            target_records_missing_in_source=report[
                'target_records_missing_in_source'],
            descrepancies=report['descrepancies'],
            source_columns_missing_in_target=report[
                'source_columns_missing_in_target'],
            target_columns_missing_in_source=report[
                'target_columns_missing_in_source'],)
        return report
