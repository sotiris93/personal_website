from rest_framework import serializers
from project.models import Project, Skill


class ProjectSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Skill.objects.all()
    )

    class Meta:
        model = Project
        fields = '__all__'