# from django.contrib import admin
#
# from polls.models import Question, Choice
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     pass


# practice
from django.contrib import admin

from polls.models import Question

admin.site.register(Question)
