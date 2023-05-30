from django.shortcuts import render
from rest_framework import mixins, generics

from mixcrud.models import Student
from mixcrud.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 2


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination

# #########################################################
#
# class StudentList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     ######################################################

# class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
