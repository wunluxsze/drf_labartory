from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.status import HTTP_200_OK
from .models import User, Profile, Country, Exscursion, Tour
from .serializers import UserRegisterSerializer, UserLoginSerializer, TourSerializer , ProfileSerializer, CountrySerializer, ExcursionSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', "POST"])
@permission_classes((AllowAny,))
def get_create_tours(request):
    if request.method == "GET":
        tour = Tour.objects.all()
        serializer = TourSerializer(tour, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TourSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((AllowAny,))
def get_edit_delete_tours(request, pk):
    if request.method == 'GET':
            try:
                tour = Tour.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TourSerializer(tour, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                tour = Tour.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TourSerializer(data=request.data, instance=tour, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                tour = Tour.objects.get(id=pk)
                tour.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Tour.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', "POST"])
@permission_classes((IsAdminUser,))
def get_create_country(request):
    if request.method == "GET":
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((IsAdminUser,))
def get_edit_delete_country(request, pk):
    if request.method == 'GET':
            try:
                country = Country.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CountrySerializer(country, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                country = Country.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CountrySerializer(data=request.data, instance=country, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                country = Country.objects.get(id=pk)
                country.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Tour.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', "POST"])
@permission_classes((IsAdminUser,))
def get_create_excursion(request):
    if request.method == "GET":
        excursion = Exscursion.objects.all()
        serializer = ExcursionSerializer(excursion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExcursionSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((IsAdminUser,))
def get_edit_delete_excursion(request, pk):
    if request.method == 'GET':
            try:
                excursion = Exscursion.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ExcursionSerializer(excursion, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                excursion = Exscursion.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ExcursionSerializer(data=request.data, instance=excursion, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                excursion = Exscursion.objects.get(id=pk)
                excursion.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Tour.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', "POST"])
@permission_classes((IsAuthenticated,))
def get_create_profile(request):
    if request.method == "GET":
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_edit_delete_profile(request, pk):
    if request.method == 'GET':
            try:
                profile = Profile.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProfileSerializer(profile, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                profile = Profile.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProfileSerializer(data=request.data, instance=profile, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                profile = Profile.objects.get(id=pk)
                profile.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Tour.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['data'] = serializer.data
            user = serializer.user
            token = Token.objects.create(user=user)
            print(Token)
            return Response({'user_token': token.key}, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

class LoginUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'error': {
                    'code': 401,
                    'message': 'Authenticated Failed'
                }
            })
        user = serializer.validated_data
        print('kostya', user)
        if user:
            token_object, token_created = Token.objects.get_or_create(user=user)
            token = token_object if token_object else token_created

            return Response({'user_token': token.key}, status=HTTP_200_OK)
        return Response({'error': {'message': 'Authenticated failed'}})

class LogOutUserView(ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response({
                {'error': {
                    'code': 401,
                    'message': 'Logout failed'
                }
                }
            }, status=401)

        logout(request)

        return Response({
            'data': {
                'message': 'logout'
            }
        }, status=200)