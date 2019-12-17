from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # print(latest_question_list)

    # template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list
    }

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # Q. 문법...
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse(f"Your'e looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
