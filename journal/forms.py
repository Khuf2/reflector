from django import forms
from .models import Journal_Page
from django.forms.widgets import DateInput



class JournalForm(forms.ModelForm):
    pub_date     = forms.DateField(label="Date", input_formats=['%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y', '%b %d %Y', '%b %d, %Y', '%d %b %Y', '%d %b, %Y', ], widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

    satisfaction_rating = forms.ChoiceField(label="Satisfaction", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))
    stress_rating       = forms.ChoiceField(label="Stress", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))

    # fitness_num       = forms.IntegerField(label='Exercise', max_value=10, min_value=1)
    
    fitness_num = forms.ChoiceField(label="Exercise", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))
    fitness_resp      = forms.CharField(
                            label="",
                            required=False, 
                            widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Describe how you exercised today (optional).",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows": 15,
                                        'cols': 60
                                    }
                                )
                            )

    nutrition_num       = forms.ChoiceField(label="Nutrition", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))
    nutrition_resp      = forms.CharField(
                            label="",
                            required=False, 
                            widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Describe how you ate today (optional).",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows": 15,
                                        'cols': 60
                                    }
                                )
                            )

    productivity_num       = forms.ChoiceField(label="Productivity", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))
    productivity_resp      = forms.CharField(
                            label="",
                            required=False, 
                            widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Describe what you got done today (optional).",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows": 15,
                                        'cols': 60
                                    }
                                )
                            )

    social_num       = forms.ChoiceField(label="Social", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))
    social_resp      = forms.CharField(
                            label="",
                            required=False, 
                            widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Describe who you hung out with today (optional).",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows": 15,
                                        'cols': 60
                                    }
                                )
                            )

    sleep_num       = forms.ChoiceField(label="Sleep", choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'my_radio'}))
    sleep_resp      = forms.CharField(
                            label="",
                            required=False, 
                            widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Describe how you slept last night (optional).",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows": 15,
                                        'cols': 60
                                    }
                                )
                            )
    
    extra_resp      = forms.CharField(
                            label="Extra",
                            required=False, 
                            widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Anything extra that needs to be said here.",
                                        "class": "new-class-name two",
                                        "id": "my-id-for-textarea",
                                        "rows": 10,
                                        'cols': 60
                                    }
                                )
                            )
    
    class Meta:
        model = Journal_Page
        exclude = ('author',)
        widgets = {
            'pub_date': DateInput(attrs={'type': 'date'}),
        }

