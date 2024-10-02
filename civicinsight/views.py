from .helper import GeminiHelper
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serialisers import NewComplaintSerializer, FetchComplaintsSerializer
from .models import RequestModel
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser

# Create your views here.

gemini_helper = GeminiHelper()

class UserComplaintview(APIView):

    parser_classes = (MultiPartParser,)

    permission_classes = (IsAuthenticated, )
    serializer_class = NewComplaintSerializer

    @swagger_auto_schema(request_body=NewComplaintSerializer)
    def post(self, request):
        serializer = self.serializer_class(data = request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserComplaintsHistoryView(APIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = FetchComplaintsSerializer

    def get(self, request):
        try:
            previous_complaints = RequestModel.objects.filter(created_by = request.user)
            serializer = self.serializer_class(previous_complaints, many = True, context={'request': request})
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "Something went wrong"
            }, status = status.HTTP_400_BAD_REQUEST)

class UserComplaintDetailView(APIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = FetchComplaintsSerializer

    def get(self, request):
        try:
            complaintId = self.request.query_params.get('complaintId')
            if complaintId is not None:
                request_model = RequestModel.objects.filter(id = complaintId)
                if len(request_model) != 0:
                    serializer = self.serializer_class(request_model[0], context={'request': request})
                    return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({
                "message": "Something went wrong"
            }, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                "message": "Something went wrong"
            }, status = status.HTTP_400_BAD_REQUEST)