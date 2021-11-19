from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

monthly_challenges_dict = {
    "january": "Start the gym 🦾",
    "february": "Push it to the limits 🦍",
    "march": "Fighting 'til I'm dead 💀, I eat 'til I'm fed 🤤🍖🍚",
    "april": "And then I'll do it all again ♻",
    "may": "Start the gym 🦾",
    "june": "Push it to the limits 🦍",
    "july": "Fighting 'til I'm dead 💀, I eat 'til I'm fed 🤤🍖🍚",
    "august": "And then I'll do it all again ♻",
    "september": "Start the gym 🦾",
    "october": "Push it to the limits 🦍",
    "november": "Fighting 'til I'm dead 💀, I eat 'til I'm fed 🤤🍖🍚",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Are there more then 12 months you BAKA? 😑😑😑")
    if month < 1:
        return HttpResponseNotFound("Start from 1 you dummy! 🙄 ")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.capitalize()
        })
    except:
        return HttpResponseNotFound("Maybe in your univers that might be a month! 👾👽")
