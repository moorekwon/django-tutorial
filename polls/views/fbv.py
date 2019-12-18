from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # print(latest_question_list)

    # template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list
    }

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


# generic view
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {'question': question})


# generic view
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)

    # django-tutorial code
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})


# generic view
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


def vote(request, question_id):
    # 특정 Question에 해당하는 특정 Choice의 votes를 1 늘리기
    # 이후 특정 Question에 해당하는 results 페이지로 이동
    if request.method == 'POST':
        # 아무것도 선택되지 않은 경우, detail 페이지로 다시 이동(redirect)
        try:
            choice_pk = request.POST['choice']
            # 전달받은 Choice pk에 해당하는 Choice 객체
            # choice = question.choice_set.get(pk=choice_pk)
            choice = get_object_or_404(Choice, pk=choice_pk)
        except:
            return redirect('polls:detail', question_id=question_id)
        else:
            # 선택된 Choice의 votes 값 1 증가
            choice.votes += 1
            choice.save()

        # results 페이지로 이동
        return redirect('polls:results', question_id=question_id)

    # django-tutorial code
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExits):
    #     context = {
    #         'question': question,
    #         'error_message': "You didn't select a choice."
    #     }
    #     return render(request, 'polls/detail.html', context)
    # else:
    #     selected_choice.votes += 1
    #     # print(selected_choice.votes)
    #     selected_choice.save()
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
