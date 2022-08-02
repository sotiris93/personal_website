import django_filters
from django_filters import CharFilter
from django import forms


from .models import *

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr="icontains", label='Title')
    skills = django_filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all(),
        widget= forms.CheckboxSelectMultiple )
    class Meta:
        model = Project
        fields = ['title', 'skills']