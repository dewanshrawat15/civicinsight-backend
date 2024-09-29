from .helper import GeminiHelper
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serialisers import NewComplaintSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser

# Create your views here.

gemini_helper = GeminiHelper()

class UserComplaintview(APIView):

    parser_classes = (MultiPartParser,)

    permission_classes = (AllowAny, )
    serializer_class = NewComplaintSerializer

    @swagger_auto_schema(request_body=NewComplaintSerializer)
    def post(self, request):
        serializer = self.serializer_class(data = request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)