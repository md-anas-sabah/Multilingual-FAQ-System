# faqs/serializers.py
from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at']

    def to_representation(self, instance):
        lang = self.context.get('language', 'en')
        return {
            'id': instance.id,
            'question': instance.get_question(lang),
            'answer': instance.get_answer(lang),
            'created_at': instance.created_at
        }