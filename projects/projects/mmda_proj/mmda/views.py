from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic

from .models import Choice, Question


#def index(request):
#    return HttpResponse("<title>Bootstrap Layouts</title>")

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
'''
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mmda/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''
'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'mmda/index.html', context)



def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'mmda/detail.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mmda/results.html', {'question': question})

'''
class IndexView(generic.ListView):
    template_name = 'mmda/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]'''
def IndexView(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mmda/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

class AddFileView(generic.ListView):
    template_name = 'mmda/add_file.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class AddPageView(generic.ListView):
    template_name = 'mmda/add_webpage.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class AddKeywordsView(generic.ListView):
    template_name = 'mmda/keywords.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class QueryView(generic.ListView):
    template_name = 'mmda/query.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'mmda/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'mmda/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'mmda/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mmda:results', args=(question.id,)))
