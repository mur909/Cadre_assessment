# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from Result import models
# from Result import serializers
#
#
# # Create your views here.
#
# class Demo(APIView):
#     def get(self, request):
#         # 从数据库中拿数据
#         queryset = models.Result.objects.all()
#         # 序列化所有的数据
#         ser_obj = serializers.ResultSerializer(queryset, many=True)
#         # 返回序列化好的数据
#         return Response(ser_obj.data)