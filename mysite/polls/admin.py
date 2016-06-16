from django.contrib import admin

from .models import Question,Choice
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		( 'Question Info', {'fields' : ['question_text']}),
		('Date info',{'fields':['pub_date'], 'classes':['collapse']}),
	]
	list_display = ('question_text', 'pub_date')
	inlines = [ChoiceInline]
	search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
