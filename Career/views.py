from django.shortcuts import render, redirect,get_object_or_404
from Career.models import Career, Career2
from Question.models import Question
from django.db.models import Q


# Create your views here.
def Careerpage(request):
    if 'career' in request.GET:
        career = request.GET['career']
        career_query = Q(tags__icontains=career)
        career_results = Career.objects.filter(career_query)
        career2_results = Career2.objects.filter(career_query)
        results = list(career_results) + list(career2_results)
        return render(request, 'search.html', {'career': results})
    return render(request, 'Career/career.html')

def askque(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            que = Question()
            que.title = request.POST.get('quetitle')
            que.details = request.POST.get('details')
            que.tags = request.POST.get('tags')
            que.user = request.user
            que.save()
            comment_date_time = que.add_time
            return redirect('Career')
    else:
        return render(request, 'Login/Signup.html')

def Highpaying(request):
    cares=Career.objects.filter(category__icontains="Highpaying").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def TopDemanded(request):
    cares=Career.objects.filter(category__icontains="Top Demanded").values()
    context={'cares':cares }
    return render(request, 'Career/Career_option.html', context)

def Unknown(request):
    cares=Career.objects.filter(category__icontains="Unknown").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def CareersBySubjects(request):
    cares=Career.objects.filter(category__icontains="CareersBySubjects").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Unique(request):
    cares=Career.objects.filter(category__icontains="Unique").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def SkillsRequired(request):
    cares=Career.objects.filter(category__icontains="Skill").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def GovernmentSector(request):
    cares=Career2.objects.filter(category__icontains="Government").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Creative(request):
    cares=Career2.objects.filter(category__icontains="Creative").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Sports(request):
    cares=Career2.objects.filter(category__icontains="Sports").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Healthcare(request):
    cares=Career.objects.filter(category__icontains="Healthcare").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Finance(request):
    cares=Career.objects.filter(category__icontains="Finance").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def IT(request):
    cares=Career.objects.filter(category__icontains="IT").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Management(request):
    cares=Career.objects.filter(category__icontains="Management").values()
    context={'cares':cares}
    return render(request, 'Career/Career_option.html', context)

def Career_detail(request, id):
    care_names = Career.objects.filter(cno=id)
    cname = care_names[0].cname
    quests = Question.objects.filter(tags__icontains=cname.lower())
    context = {'care_names': care_names, 'quests': quests}
    return render(request, 'Career/Career_detail.html', context)


def Career_detail2(request, id):
    care_names= Career2.objects.filter(cno=id)
    cname = care_names[0].cname.lower()
    quests=Question.objects.filter(tags__icontains=cname)
    context = {'care_names':care_names, 'quests':quests}
    return render(request, 'Career/Career_detail.html', context)