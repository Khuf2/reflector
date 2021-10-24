from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.db import IntegrityError
from datetime import date, datetime
from pytz import timezone
import pytz

from .forms import JournalForm
from .models import Journal_Page



def index(request):
    return render(request, 'reflector/index.html')

def usage(request):
    return render(request, 'reflector/usage.html')

def significance(request):
    return render(request, 'reflector/significance.html')

def journal(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.POST.get('date_search') is not None and request.POST.get('submit_date_search') is not None:
            searched_page = Journal_Page.objects.filter(author=request.user).filter(pub_date=request.POST.get('date_search')).order_by('-pub_date')
            context = {
                'latest_journal_page_list': searched_page,
                'filtered': True
            }
            return render(request, 'journal/journal.html', context)

        elif request.method == "POST" and request.POST.get('query_go') is not None:

            if request.POST['the_bar'] != '':
                polished_bar = int(request.POST['the_bar'])

                # 1 : Satisfaction
                if request.POST['category'] == 'satisfaction_rating':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(satisfaction_rating__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(satisfaction_rating__lte=polished_bar).order_by('-pub_date')
                
                # 2 : Stress
                if request.POST['category'] == 'stress_rating':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(stress_rating__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(stress_rating__lte=polished_bar).order_by('-pub_date')
                
                # 3 : Fitness
                if request.POST['category'] == 'fitness_num':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(fitness_num__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(fitness_num__lte=polished_bar).order_by('-pub_date')
                
                # 4 : Nutrition
                if request.POST['category'] == 'nutrition_num':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(nutrition_num__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(nutrition_num__lte=polished_bar).order_by('-pub_date')

                # 5 : Productivity
                if request.POST['category'] == 'productivity_num':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(productivity_num__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(productivity_num__lte=polished_bar).order_by('-pub_date')

                # 6: Social
                if request.POST['category'] == 'social_num':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(social_num__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(social_num__lte=polished_bar).order_by('-pub_date')

                # 7 : Sleep
                if request.POST['category'] == 'sleep_num':
                    if request.POST['up_or_down'] == 'GTE':
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(sleep_num__gte=polished_bar).order_by('-pub_date')
                    else:
                        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).filter(sleep_num__lte=polished_bar).order_by('-pub_date')


                context = {
                    'latest_journal_page_list': latest_journal_page_list,
                    'filtered': True,
                }
                
                return render(request, 'journal/journal.html', context)
            
        
        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).order_by('-pub_date')
        context = {
            'latest_journal_page_list': latest_journal_page_list,
            'filtered': False
        }
        
        return render(request, 'journal/journal.html', context)

    else:
        return render(request, 'reflector/index.html')
    
def journal_add(request):
    form = JournalForm(request.POST or None)
    if form.is_valid():
        try:
            new_page = form.save(commit=True)
            new_page.author = request.user
            new_page.save()
        except IntegrityError as e:
            return render(request, "reflector/IntegrityError.html")
        
        return redirect('journal')
    else:
        form = JournalForm()
        context = {
            'form': form,
            'today': date.today(),
        }
    return render(request, "journal/journal_add.html", context)

def journal_delete(request, pageID):
    Journal_Page.objects.filter(author=request.user, id=pageID).delete()
    return redirect('journal')

def journal_edit(request, pageID):
    page_to_edit = get_object_or_404(Journal_Page,id=int(pageID))
    form = JournalForm(request.POST or None, instance=page_to_edit)

    context = {
        'form': form,
    }

    if form.is_valid():
        try:
            form.save()
        except IntegrityError as e:
            return render(request, "reflector/IntegrityError.html")
        return redirect('journal')
    return render(request, "journal/journal_add.html", context)

def graph(request):
    if request.user.is_authenticated:
        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).order_by('pub_date')

        dates = []
        for x in list(latest_journal_page_list.values('pub_date')):
            dates.append(x['pub_date'])

        satisfactions = []
        for x in list(latest_journal_page_list.values('satisfaction_rating')):
            satisfactions.append(x['satisfaction_rating'])

        stresses = []
        for x in list(latest_journal_page_list.values('stress_rating')):
            stresses.append(x['stress_rating'])

        fitness = []
        for x in list(latest_journal_page_list.values('fitness_num')):
            fitness.append(x['fitness_num'])

        nutrition = []
        for x in list(latest_journal_page_list.values('nutrition_num')):
            nutrition.append(x['nutrition_num'])

        productivity = []
        for x in list(latest_journal_page_list.values('productivity_num')):
            productivity.append(x['productivity_num'])

        social = []
        for x in list(latest_journal_page_list.values('social_num')):
            social.append(x['social_num'])

        sleep = []
        for x in list(latest_journal_page_list.values('sleep_num')):
            sleep.append(x['sleep_num'])


        context = {
            'latest_journal_page_list': latest_journal_page_list,
            'dates': dates,
            'satisfactions': satisfactions,
            'stresses': stresses,
            'fitness': fitness,
            'nutrition': nutrition,
            'productivity': productivity,
            'social': social,
            'sleep': sleep,
        }
        return render(request, "journal/graph.html", context)

    return render(request, "reflector/index.html")