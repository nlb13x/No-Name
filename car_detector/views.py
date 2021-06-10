from django.http import HttpResponse
from .models import Question, Choice,  traffic
from django.shortcuts import render


def index(request):
    latest_q_lst = Question.objects.order_by('-pub_date')
    context = {'q_l' : latest_q_lst}
    return render(request, 'car_detector/index.html', context)

def detail(requst, question_id):
    response = "traffic %s"
    return HttpResponse(response % question_id)