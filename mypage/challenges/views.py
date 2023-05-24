from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect


monthly_challenges = {
    "january": 'eat no solid food for 1 month',
    'febuary':'buy data for yourself',
    'march':'save more money bunmi',
    'april':'eat no solid food for 1 month',
    'may':'buy data for yourself',
    'june':'save more money bunmi',
    'july':'eat no solid food for 1 month',
    'august': 'buy data for yourself',
    'september':'save more money bunmi',
    'october':'eat no solid food for 1 month',
    'november': 'buy data for yourself',
    'december':'save more money bunmi'
}
def monthly_challenge(request, month):
    try:
        challenge_test= monthly_challenges[month]
        response_data= f'<h1>{challenge_test}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('not supported')
    

def monthly_challengebynum(request,month):
    forward_month=list(monthly_challenges.keys())
    if month > len(forward_month):
        return HttpResponseNotFound('wrong number')
    redirect= forward_month[month-1]
    dynamic_redirect= reverse('month-challenge', args=[redirect])
    return HttpResponseRedirect(redirect)

def index(request):
    list_item =""
    forward_month=list(monthly_challenges.keys())
    for month in forward_month:
        month_path= reverse('month-challenge', args=[month])
        capitalized_month= month.capitalize()
        list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data= f'<ul>{list_item}</ul>'
    return HttpResponse(response_data)

