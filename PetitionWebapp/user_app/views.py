from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import random
import threading
from .serializers import *

@method_decorator(csrf_exempt, name='dispatch')
class RegisterationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request,*args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object.set_password(serializer.data.get("new_password1"))
            self.object.save()
            response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailThread(threading.Thread):
    def __init__(self):
        self.email = None
        threading.Thread.__init__(self)

    def send_email(msg, randomcode, name, email_address):
        email_body = render_to_string(
                        "user_app/email.html",
                        {"message":msg, "randomcode":randomcode, "full_name":name}
                    )
        email = EmailMessage(
            f'{msg} CODE',
            email_body,
            'PETITION WEBAPP',
            [email_address],
        )
        email.content_subtype = "html"
        email.fail_silently = False
        email.send()


@method_decorator(csrf_exempt, name='dispatch')
class SendRegisterEmail(GenericAPIView):
    serializer_class=SendregisterEmailSerializer
    def post(self,request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        randomcode = random.randrange(1111, 9999)
        msg="Registration"
        if serializer.is_valid():
            EmailThread().send_email(msg, randomcode, serializer.data['username'], serializer.data['email'])
            return Response({'code':randomcode},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class SendResetPasswordEmail(GenericAPIView):
    serializer_class=SendpasswordresetEmailSerializer
    def post(self,request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        randomcode = random.randrange(1111, 9999)
        msg="Reset Password"
        if serializer.is_valid():
            full_name=(get_object_or_404(User, email=serializer.validated_data['email']).username)
            EmailThread().send_email(msg, randomcode, full_name, serializer.data['email'])
            return Response({'code':randomcode},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ResetPasswordView(UpdateAPIView):
    serializer_class=ResetPasswordSerializer
    model = User
    permissions=(AllowAny)
    def update(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object=get_object_or_404(User, email=serializer.validated_data['email'])
            self.object.set_password(serializer.data.get("new_password1"))
            self.object.save()
            response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfileView(UpdateAPIView):
    serializer_class = PrivateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.request.user.id
        queryset = User_Model.objects.get(id=user_id)
        return queryset


@method_decorator(csrf_exempt, name='dispatch')
class GetProfileView(RetrieveAPIView):
    serializer_class = PublicProfileSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        profile = get_object_or_404(User_Model, pk=pk)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
