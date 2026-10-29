from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .services import get_stats, register_user
class StatsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(get_stats(), status=status.HTTP_200_OK)
class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = register_user(serializer.validated_data["email"])
        return Response(result, status=status.HTTP_201_CREATED)
