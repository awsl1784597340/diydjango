from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from faker import models


def showservant(request):
    data = {}
    data['status'] = 0
    faker_index = models.Servant.objects.values().all().order_by('No')
    # json_data = serializers.serialize('json', faker_index, ensure_ascii=False)
    # json_data = json.loads(json_data)
    # print(json_data)
    json_data = list(faker_index)
    data['message'] = json_data
    return JsonResponse(data, safe=False)


def index(request):
    return render(request, 'index.html')


def post(request):
    classrange = ['Saber', 'Archer', 'Lancer','Assassin', 'Rider', 'Caster','Ruler', 'MoonCancer', 'Avenger','Alterego',
     'Foreigner', 'Berserker', 'Shielder']
    genderrange=['male', 'female', 'unknown']
    object = {}
    object1 = {}
    if request.method == 'POST':
        object['No'] = request.POST.get('No')
        object['name'] = request.POST.get('name')
        object['classname'] = request.POST.get('class')
        object['nickname'] = request.POST.get('nickname')
        object['gender'] = request.POST.get('gender')

        if object['classname'] not in classrange:
            object['status'] = 2
            print(object['status'])
            return JsonResponse(object1)
        if object['gender'] not in genderrange:
            object['status'] = 2
            print(object['status'])
            return JsonResponse(object1)

        try:
            models.Servant.objects.create(No=object['No'], name=object['name'], classname=object['classname'],
                                          nickname=object['nickname'],gender=object['gender'])
            object1['status'] = 0
        except:
            object1['status'] = 1
    return JsonResponse(object1)


# Create your views here.
