# class-based view
from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class VoteView(View):
    def post(self, request, question_id):
        try:
            choice_pk = request.POST['choice']
            choice = get_object_or_404(Choice, pk=choice_pk)
        except:
            return redirect('polls:detail', question_id=question_id)
        else:
            choice.votes += 1
            choice.save()

        return redirect('polls:results', question_id=question_id)
