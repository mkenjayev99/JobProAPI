from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions

from .models import Account, WorkHistory
from .serializers import LoginSerializer, WorkHistorySerializer, RegisterSerializer, AccountSerializer
from .permissions import IsOwnerOrReadOnly


class AccountRegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/api/register/
    serializer_class = RegisterSerializer
    queryset = Account.objects.all()

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': "Account successfully created"}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/api/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({serializer.data['tokens']}, status=status.HTTP_200_OK)


class AccountListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/account/list/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if qs:
            return qs.filter(role=1)
        return qs


class AccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerOrReadOnly]


class WorkHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class WorkHistoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

