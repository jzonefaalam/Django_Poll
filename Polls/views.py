from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from Polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'Polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    context = {'question' : question}

    return render(request, 'Polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    context = {'question' : question}

    return render(request, 'Polls/result.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question' : question, 'error_message' : "You did not select a choice."}
        return render(request, 'Polls/detail.html', context)
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('Polls:result', args = (question.id, )))