from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from reconcile.api.reconciliation.models import Report
from reconcile.api.reconciliation.normalizer import normalize
from reconcile.api.reconciliation.reconciler import reconcile_files
from reconcile.api.reconciliation.serializers import FileUploadSerializer


# Create your views here.
class CSVUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request: Request):
        # Validate incoming files
        serializer = FileUploadSerializer(data=request.FILES)
        if serializer.is_valid(raise_exception=True):
            files = serializer.validated_data
            # Normalize the data
            normalized_source = normalize(data=files['source_file'])
            normalized_target = normalize(data=files['target_file'])
            # Reconcile the data
            report = reconcile_files(source=normalized_source,
                                     target=normalized_target)
            # Save file and report to database
            report = Report(source_records_missing_in_target=report['source_records_missing_in_target'],
                            target_records_missing_in_source=report['target_records_missing_in_source'],
                            descrepancies=report['descrepancies'])
            report.save()
            return Response(data={'message': 'Files uploaded successfully',
                                  'report_id': report.id}, status=201)


class ReconciliationReportView(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'reconciliation/report.html'

    def get(self, request: Request, report_id: int):
        report = Report.objects.get(id=report_id)
        return Response({'report': report})
