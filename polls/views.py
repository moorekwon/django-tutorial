from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }

    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))
    # return render(request, 'polls/index.html')


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exits!')
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)
    # return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
