from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import *

@method_decorator(csrf_exempt, name='dispatch')
class PetitionView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PetitionSerializer


@method_decorator(csrf_exempt, name='dispatch')
class SignPetitionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SignPetitionSerializer
