from django.shortcuts import render
from django.core import serializers

import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class AllGearAPIView(APIView):

    def get(self, request, format=None):
        try:
            all_gear = Products.objects.all()
            data = []

            for gear in all_gear:
                data.append({
                    "name": gear.name,
                    "description1": gear.description1,
                    "description2": gear.description2,
                    "description3": gear.description3,
                    "description4": gear.description4,
                    "description5": gear.description5,
                    "description6": gear.description6,
                    "description7": gear.description7,
                    "description8": gear.description8,
                    "description9": gear.description9,
                    "description10": gear.description10,
                    "category": gear.category.title,

                })

            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitGearAPIView(APIView):

    def post(self, request, format=None):

        try:
            serializer = serializers.SubmitGearSerializer(data=request.data)
            if serializer.is_valid():
                name = serializer.data.get('name')
                description1 = serializer.data.get('description1')
                description2 = serializer.data.get('description2')
                description3 = serializer.data.get('description3')
                description4 = serializer.data.get('description4')
                description5 = serializer.data.get('description5')
                description6 = serializer.data.get('description6')
                description7 = serializer.data.get('description7')
                description8 = serializer.data.get('description8')
                description9 = serializer.data.get('description9')
                description10 = serializer.data.get('description10')
                category_id = serializer.data.get('category_id')

            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)

            category = Category.objects.get(id=category_id)

            products = Products()
            products.name = name
            products.description1 = description1
            products.description2 = description2
            products.description3 = description3
            products.description4 = description4
            products.description5 = description5
            products.description6 = description6
            products.description7 = description7
            products.description8 = description8
            products.description9 = description9
            products.description10 = description10
            products.category = category
            products.save()

            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteGearAPIView(APIView):
    def post(self, request, format=None):
        try:
            serializer = serializers.DeleteGearSerializer(data=request.data)

            if serializer.is_valid():
                gear_id = serializer.data.get('gear_id')
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)

            Products.objects.filter(id=gear_id).delete()

            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
