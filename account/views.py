from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import date, timedelta

from .forms import RegisterForm

from django.db.models import Avg

from journal.models import Journal_Page



def login(request):
    return render(request, 'registration/login.html')

def redirect_login(request):
    return redirect('/account/login')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login', permanent=True)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})

def profile(request):
    if request.user.is_authenticated:
        latest_journal_page_list = Journal_Page.objects.filter(author=request.user).order_by('-pub_date')

        d=date.today()-timedelta(days=6)
        last_weeks_page_list = Journal_Page.objects.filter(author=request.user).filter(pub_date__gte=d).filter(pub_date__lte=date.today())

        context = {
            'journal_count': latest_journal_page_list.count(),
        }

        # First, check if anything is in our entries list
        if context['journal_count'] > 0:
            context['satisfaction_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('satisfaction_rating')).values())[0])
            context['stress_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('stress_rating')).values())[0])
            context['fitness_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('fitness_num')).values())[0])
            context['nutrition_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('nutrition_num')).values())[0])
            context['productivity_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('productivity_num')).values())[0])
            context['social_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('social_num')).values())[0])
            context['sleep_avg'] = "{0:.2f}".format(list(latest_journal_page_list.aggregate(Avg('sleep_num')).values())[0])
        else:
            context['satisfaction_avg'] = "--"
            context['stress_avg'] = "--"
            context['fitness_avg'] = "--"
            context['nutrition_avg'] = "--"
            context['productivity_avg'] = "--"
            context['social_avg'] = "--"
            context['sleep_avg'] = "--"

        if last_weeks_page_list.count() > 0:
            context['recent_satisfaction_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('satisfaction_rating')).values())[0])
            context['recent_stress_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('stress_rating')).values())[0])
            context['recent_fitness_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('fitness_num')).values())[0])
            context['recent_nutrition_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('nutrition_num')).values())[0])
            context['recent_productivity_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('productivity_num')).values())[0])
            context['recent_social_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('social_num')).values())[0])
            context['recent_sleep_avg'] = "{0:.2f}".format(list(last_weeks_page_list.aggregate(Avg('sleep_num')).values())[0])


            # Calculate percentages up or down here and pass with the context if you want
            raw_satisfaction_trend = list(last_weeks_page_list.aggregate(Avg('satisfaction_rating')).values())[0] / list(latest_journal_page_list.aggregate(Avg('satisfaction_rating')).values())[0] - 1
            context['satisfaction_trend'] = "{0:.1f}".format(raw_satisfaction_trend*100) + "%"
            if(raw_satisfaction_trend > 0):
                context['satisfaction_trend'] = "+" + context['satisfaction_trend']

            raw_stress_trend = list(last_weeks_page_list.aggregate(Avg('stress_rating')).values())[0] / list(latest_journal_page_list.aggregate(Avg('stress_rating')).values())[0] - 1
            context['stress_trend'] = "{0:.1f}".format(raw_stress_trend * 100) + "%"
            if(raw_stress_trend > 0):
                context['stress_trend'] = "+" + context['stress_trend']

            raw_fitness_trend = list(last_weeks_page_list.aggregate(Avg('fitness_num')).values())[0] / list(latest_journal_page_list.aggregate(Avg('fitness_num')).values())[0] - 1
            context['fitness_trend'] = "{0:.1f}".format(raw_fitness_trend*100) + "%"
            if(raw_fitness_trend > 0):
                context['fitness_trend'] = "+" + context['fitness_trend']

            raw_nutrition_trend = list(last_weeks_page_list.aggregate(Avg('nutrition_num')).values())[0] / list(latest_journal_page_list.aggregate(Avg('nutrition_num')).values())[0] - 1
            context['nutrition_trend'] = "{0:.1f}".format(raw_nutrition_trend*100) + "%"
            if(raw_nutrition_trend > 0):
                context['nutrition_trend'] = "+" + context['nutrition_trend']

            raw_productivity_trend = list(last_weeks_page_list.aggregate(Avg('productivity_num')).values())[0] / list(latest_journal_page_list.aggregate(Avg('productivity_num')).values())[0] - 1
            context['productivity_trend'] = "{0:.1f}".format(raw_productivity_trend*100) + "%"
            if(raw_productivity_trend > 0):
                context['productivity_trend'] = "+" + context['productivity_trend']

            raw_social_trend = list(last_weeks_page_list.aggregate(Avg('social_num')).values())[0] / list(latest_journal_page_list.aggregate(Avg('social_num')).values())[0] - 1
            context['social_trend'] = "{0:.1f}".format(raw_social_trend*100) + "%"
            if(raw_social_trend > 0):
                context['social_trend'] = "+" + context['social_trend']

            raw_sleep_trend = list(last_weeks_page_list.aggregate(Avg('sleep_num')).values())[0] / list(latest_journal_page_list.aggregate(Avg('sleep_num')).values())[0] - 1
            context['sleep_trend'] = "{0:.1f}".format(raw_sleep_trend*100) + "%"
            if(raw_sleep_trend > 0):
                context['sleep_trend'] = "+" + context['sleep_trend']

        else:
            context['recent_satisfaction_avg'] = "--"
            context['recent_stress_avg'] = "--"
            context['recent_fitness_avg'] = "--"
            context['recent_nutrition_avg'] = "--"
            context['recent_productivity_avg'] = "--"
            context['recent_social_avg'] = "--"
            context['recent_sleep_avg'] = "--"

            context['satisfaction_trend'] = ""
            context['fitness_trend'] = ""
            context['exercise_trend'] = ""
            context['nutrition_trend'] = ""
            context['productivity_trend'] = ""
            context['social_trend'] = ""
            context['sleep_trend'] = ""

        return render(request, 'account/profile.html', context)
    else:
        return render(request, 'reflector/index.html')