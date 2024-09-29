from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from reconcile.api.reconciliation.models import Report
from reconcile.api.reconciliation.serializers import FileUploadSerializer


# Create your views here.
class CSVUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request: Request):
        # Validate incoming files
        serializer = FileUploadSerializer(data=request.FILES)
        if serializer.is_valid(raise_exception=True):
            report = serializer.create(
                validated_data=serializer.validated_data)

            return Response(data={'message': 'Files uploaded successfully',
                                  'report_id': report.id}, status=201)


class ReconciliationReportView(APIView):
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'reconciliation/report.html'

    def get(self, request: Request, report_id: int):
        report = get_object_or_404(Report, id=report_id)
        return Response({'report': report})
