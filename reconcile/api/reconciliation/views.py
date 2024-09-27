from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

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
            # Reconcile the data
            # Save file and report to database
            return Response(data=files)


class ReconciliationReportView(APIView):
    def get(self, request: Request):
        return Response({'data': "It's working"})
