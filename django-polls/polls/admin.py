from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}), # ask abdulrehman about how the program knows where to apply which affect    
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]})
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date", "question_text",] #added question_text for no reason
    search_fields = ["question_text"]
    

admin.site.register(Question, QuestionAdmin)