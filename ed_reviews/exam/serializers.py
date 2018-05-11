from rest_framework import serializers
from . import models


class QuestionSerializer( serializers.ModelSerializer ):
    class Meta:
        fields = (
            'text',
            'required',
            'category',
            'survey',
            'question_type',
            'choices'
        )

        model = models.Question


class ResponseSerializer( serializers.ModelSerializer ):
    class Meta:
        extra_kwargs = {
            'your_email': {'write_only': True},
            'interview_uuid': {'read_only': True}
        }
        fields = (
            'interview_uuid',
            'survey',
            'interviewer',
            'interviewee',
            'your_email',
            'conditions',
            'comments'
        )

        model = models.Response
