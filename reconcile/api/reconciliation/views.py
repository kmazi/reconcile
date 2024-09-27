from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from reconcile.api.reconciliation.serializers import FileUploadSerializer


# Create your views here.
class CSVUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request: Request):
        serializer = FileUploadSerializer(data=request.data)
        return Response(data=request.data)


class ReconciliationReportView(APIView):
    def get(self, request: Request):
        return Response({'data': "It's working"})
