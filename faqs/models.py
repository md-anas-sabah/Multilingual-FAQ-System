# faqs/models.py
from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(help_text="Enter the question in English")
    answer = RichTextField(help_text="Enter the answer in English")
    
   
    question_hi = models.TextField(blank=True, null=True, help_text="Hindi translation of the question")
    answer_hi = RichTextField(blank=True, null=True, help_text="Hindi translation of the answer")
    

    question_bn = models.TextField(blank=True, null=True, help_text="Bengali translation of the question")
    answer_bn = RichTextField(blank=True, null=True, help_text="Bengali translation of the answer")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']

    def __str__(self):
        return self.question[:50]  

    def get_translated_field(self, field_name, language):
        """
        Get the translated version of a field based on language code
        """
        cache_key = f'faq_{self.id}_{field_name}_{language}'
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        if language == 'en' or not language:
            value = getattr(self, field_name)
        else:
            translated_field = f'{field_name}_{language}'
            value = getattr(self, translated_field)
            
            if not value:
                original_value = getattr(self, field_name)
                try:
                    translator = Translator()
                    translation = translator.translate(original_value, dest=language)
                    value = translation.text
                    # Save the translation to database
                    setattr(self, translated_field, value)
                    self.save()
                except Exception as e:
                    value = getattr(self, field_name)


        cache.set(cache_key, value, timeout=3600) 
        return value

    def get_question(self, language=None):
        """Get the question in the specified language"""
        return self.get_translated_field('question', language)

    def get_answer(self, language=None):
        """Get the answer in the specified language"""
        return self.get_translated_field('answer', language)