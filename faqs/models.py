from django.db import models
from googletrans import Translator
from ckeditor.fields import RichTextField


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def translate_text(self, text, lang):
        translator = Translator()
        try:
            translation = translator.translate(text, dest=lang)
            return translation.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return text

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, "hi")
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, "bn")
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, "hi")
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, "bn")
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        return getattr(self, f"question_{lang}", self.question)

    def get_translated_answer(self, lang):
        return getattr(self, f"answer_{lang}", self.answer)

    def __str__(self):
        return self.question
