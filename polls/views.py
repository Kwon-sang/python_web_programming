from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse

from polls.models import Question, Choice


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.all().order_by('-created_at')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': question,
                   'error_message': "하나를 선택해 주세요."}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question_id)


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
