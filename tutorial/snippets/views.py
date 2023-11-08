from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, renderers
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer

from .models import Snippet
from .serializers import SnippetSerializer
from django.contrib.auth.models import User
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


@api_view(['GET'])
def api_root(request, format=None):
   return Response({
       'users': reverse('user-list', request=request, format=format),
       'snippets': reverse('snippet-list', request=request, format=format)
   })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetHighlight(generics.GenericAPIView):
   queryset = Snippet.objects.all()
   renderer_classes = [renderers.StaticHTMLRenderer]

   def get(self, request, **kwargs):
       snippet = self.get_object()
       return Response(snippet.highlighted)



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
