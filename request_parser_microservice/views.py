from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import get_language


def headerparse(request):

    ip = request.META['REMOTE_ADDR']
    language = get_language()
    browser = request.META['HTTP_USER_AGENT']
    software = browser.split(';')[0].split('(')[1]
    OS = browser.split(';')[1].split(')')[0]
    json_obj = {}
    json_obj['ip'] = ip
    json_obj['language'] = language
    json_obj['software'] = software
    json_obj['Operational System'] = OS
    return JsonResponse(json_obj)
