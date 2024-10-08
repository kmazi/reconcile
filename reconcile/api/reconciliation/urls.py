from django.urls import path

from .views import CSVUploadView, ReconciliationReportView

urlpatterns = [
    path('upload_csv', CSVUploadView.as_view(), name="csv_upload"),
    path('report/<int:report_id>',
         ReconciliationReportView.as_view(), name="file_report"),
]
