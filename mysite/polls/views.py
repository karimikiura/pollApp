from multiprocessing import context
from re import template
from urllib import response
from django.http import HttpResponse #-> to remove
from django.template import loader # to remove 
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# models
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html', context)


# poll detail

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does Not Exist!")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the reaults of question %s."
    return HttpResponse(response %question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
