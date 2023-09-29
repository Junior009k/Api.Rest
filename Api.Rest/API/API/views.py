from typing import Any
from django import http
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Persona
from django.http import JsonResponse
import json
class PersonaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request,id=0):
        if id>0:
            personas=list(Persona.objects.filter(id=id).values())
            if len(personas)>0:
                persona=personas[0]
                datos = {'message' : 'success', 'persona':persona}
            else:
                datos = {'message' : 'no found...'}
            return JsonResponse(datos)
        else:
            personas=list(Persona.objects.values())
            if len(personas)>0:
                datos = {'message' : 'success', 'personas':personas}
            else:
                datos = {'message' : 'no found...'}
            return JsonResponse(datos)
    
    def post(self, request):
       #print(request.body)
       jd=json.loads(request.body)
       #print(jd)
       Persona.objects.create(name=jd['name'],last_name=jd['last_name'],type_document=jd['type_document'],number_document=jd['number_document'],webSite=jd['webSite'],birthdate=jd['birthdate'])
       datos = {'message' : 'success'}
       return JsonResponse(datos)
    def put(self, request,id):
        jd=json.loads(request.body)
        if id>0:
            personas=list(Persona.objects.filter(id=id).values())
            if len(personas)>0:
                persona=Persona.objects.get(id=id)
                persona.name=jd['name']
                persona.last_name=jd['last_name']
                persona.type_document=jd['type_document']
                persona.number_document=jd['number_document']
                persona.webSite=jd['webSite']
                persona.birthdate=jd['birthdate']
                persona.save()
                datos = {'message' : 'success'}
            else:
                datos = {'message' : 'no found...'}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            Persona.objects.filter(id=id).delete()
            datos = {'message' : 'success'}
        else:
            datos = {'message' : 'no found...'}
        return JsonResponse(datos)