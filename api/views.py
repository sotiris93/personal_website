from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import Project, Skill
from .serializers import ProjectSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def getData(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer= ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def update(request, pk):
    item = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(instance=item, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete(request, pk):
    item = get_object_or_404(Project, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

