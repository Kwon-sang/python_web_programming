from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    # fields = ['question_text', 'created_at']
    list_display = ['question_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
