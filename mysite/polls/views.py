from django.shortcuts import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
# Create your views here.
def index(request):
    # return HttpResponse("Hello, World")
    """ latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) """
    # httpResponse 사용시
    """    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request)) """
    # render 사용시  httpRespons 보다 단축키로 만든 장고 단축키
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    # httpResponse 
    # return HttpResponse("You're looking at question %s." % question_id)
    # 404 예외 처리  + redner + try catch ber
    """   try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question}) """

    # render + get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    