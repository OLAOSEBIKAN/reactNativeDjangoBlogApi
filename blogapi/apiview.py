from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post

from .serializers import RegisterSerializer, PostSerializer


class RegisterUser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                return Response({"token": user.auth_token.key})
            except ValueError:
                return Response({"error": "Unable To Login"},
                                status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

            '''if user is not None:
            try:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                userprofile = UserProfile.objects.get(email=email)
                user_token = Token()
                user_token.user = userprofile
                user_token.token = token
                user_token.save()
                return Response({"token": token})
            except Error:
                return Response({"error": "Unable "},
                                status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response({"error": "Unable to login with the provided Credentials"},
                            status=status.HTTP_400_BAD_REQUEST)'''


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
