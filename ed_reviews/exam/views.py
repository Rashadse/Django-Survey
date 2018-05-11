from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework import generics

from . import models
from . import serializers

from .models import Survey, Category
from .form import ResponseForm


class ListCreateQuestion(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class RetrieveUpdateDestroyQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class ListCreateResponse(generics.ListCreateAPIView):
    queryset = models.Response.objects.all()
    serializer_class = serializers.ResponseSerializer


class RetrieveUpdateDestroyResponse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Response.objects.all()
    serializer_class = serializers.ResponseSerializer


def home_view(request):
    return render( request, 'index.html' )


def rest_view(request):
    return render( request, 'rest.html' )


@login_required
def survey_forwarding(request, id):
    survey = Survey.objects.get(id=id)
    category_items = Category.objects.filter(survey=survey)
    categories = [c.name for c in category_items]
    print( 'categories for this survey:' )
    print( categories )
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/confirm/")
    else:
        form = ResponseForm(survey=survey)

    return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'categories': categories})


def confirm(request):
    return render(request, 'confirm.html')
