from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Notes
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def note_list(request):
    if request.method == "GET":
        notes = Notes.objects.all()
        serializer = NoteSerializer(notes, many = True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)