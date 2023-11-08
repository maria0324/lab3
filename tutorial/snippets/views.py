from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from .models import Snippet
from .serializers import SnippetSerializer
from django.contrib.auth.models import User
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
   queryset = Snippet.objects.all()
   serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Snippet.objects.all()
   serializer_class = SnippetSerializer

   class UserList(generics.ListAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer

   class UserDetail(generics.RetrieveAPIView):
      queryset = User.objects.all()
      serializer_class = UserSerializer

