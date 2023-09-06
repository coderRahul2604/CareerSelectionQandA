from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from Career.models import Career, Career2
from django.db.models import Q
from .models import Question,Answer,Comment, Like, Dislike

# Create your views here.

def Quehtml(request):
    if 'career' in request.GET:
        career = request.GET['career']
        career_query = Q(tags__icontains=career)
        career_results = Career.objects.filter(career_query)
        career2_results = Career2.objects.filter(career_query)
        results = list(career_results) + list(career2_results)
        return render(request, 'search.html', {'career': results})
    if 'que' in request.GET:
        que=request.GET['que']
        quests=Question.objects.filter(title__icontains=que).order_by('-id')
    else:
        quests=Question.objects.all().order_by('-id')

    return render(request, 'Question/Question.html', {'quests':quests})

def Detailque(request, id):
    quest=get_object_or_404(Question, pk=id)
    tags=quest.tags.split(',')

    try:
        answer = Answer.objects.filter(question=quest)
    except Answer.DoesNotExist:
        answer = None

    return render(request, 'Question/detailque.html', {'quest':quest, 'tags':tags, 'answer':answer})


def add_comment(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = Comment()
            comment.answer = answer
            comment.comment = request.POST.get('comment')
            comment.user = request.user
            comment.save()
            comment_date_time = comment.add_time
            return redirect(reverse('Detailque', args=[answer.question.id]))
    else:
        return render(request, 'Login/Signup.html')

def add_answer(request, quest_id):
    question = get_object_or_404(Question, pk=quest_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            answer = Answer()
            answer.question = question
            answer.user = request.user
            answer.detail = request.POST.get('useranswer')
            answer.tags = ''
            answer.save()
            return redirect(reverse('Detailque', args=[quest_id]))
    else:
        return render(request, "Login/signup.html")

    return render(request, 'Question/detailque.html', {'quest': question})

def save_like(request):
    if request.user.is_authenticated: 
        if request.method=='POST':
            answerid=request.POST['answerid']
            answer=Answer.objects.get(pk=answerid)
            user=request.user
            check=Like.objects.filter(answer=answer,user=user).count()
            if check > 0:
                return JsonResponse({'bool':False})
            else:
                Like.objects.create(
                    answer=answer,
                    user=user
                )
                return JsonResponse({'bool':True})
    else:
        return render(request, "Login/signup.html")
            

def save_dislike(request):
    if request.user.is_authenticated:     
        if request.method=='POST':
            answerid=request.POST['answerid']
            answer=Answer.objects.get(pk=answerid)
            user=request.user
            check=Dislike.objects.filter(answer=answer,user=user).count()
            if check > 0:
                return JsonResponse({'bool':False})
            else:
                Dislike.objects.create(
                    answer=answer,
                    user=user
                )
                return JsonResponse({'bool':True})

    else:
        return HttpResponse(render(request, "Login/signup.html"))