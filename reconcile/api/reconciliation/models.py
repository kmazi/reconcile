from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


# Create your models here.
class Report(models.Model):
    """Model to store report."""

    id = models.AutoField(primary_key=True)
    source_records_missing_in_target = models.TextField(null=True)
    target_records_missing_in_source = models.TextField(null=True)
    source_columns_missing_in_target = ArrayField(
        base_field=models.TextField(), null=True)
    target_columns_missing_in_source = ArrayField(
        base_field=models.TextField(), null=True)
    descrepancies = models.TextField(null=True)
    created_on = models.DateTimeField(default=timezone.now)
