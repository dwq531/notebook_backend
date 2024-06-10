from .models import Note, Content
from .forms import NoteForm, ContentForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import NoteSerializer,ContentSerializer
import json
from django.http import Http404
from django.http import FileResponse
from django.core.files.storage import default_storage




def upload_note(request):
    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_id = note_form.cleaned_data['note_id']
            note = Note.objects.filter(note_id=note_id).first()
            if note:
                for field, value in note_form.cleaned_data.items():
                    setattr(note, field, value)
                note.save()
                message = 'Note updated'
            else: 
                note = Note.objects.create(**note_form.cleaned_data)
                message = 'Note created'
            return JsonResponse({'message': message}, status=200)
        else:
            for note in Note.objects.all():
                print(note.note_id)
            print(note_form.errors)
            return JsonResponse({'message': 'Invalid form'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    
def upload_content(request):
    if request.method == 'POST':
        content_form = ContentForm(request.POST, request.FILES)
        if content_form.is_valid():
            print(content_form.cleaned_data)
            content_id = content_form.cleaned_data.get('content_id')
            content, created = Content.objects.get_or_create(content_id=content_id, defaults=content_form.cleaned_data)
            if created:
                message = 'Content created'
            else:
                if content.file and content.file.name:
                    print(f"Deleting old file: {content.file.name}")
                    default_storage.delete(content.file.name)
                for field, value in content_form.cleaned_data.items():
                    setattr(content, field, value)
                content.save()
                message = 'Content updated'
            return JsonResponse({'message': message}, status=200)
        else:
            print(content_form.errors)
            return JsonResponse({'message': 'Invalid form'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    
def get_notes(request,user_id):
    if request.method == 'GET':
        notes = Note.objects.filter(user_id=user_id)
        notes = NoteSerializer(notes, many=True).data
        return JsonResponse(notes,safe=False, status=200)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    
def get_note(request,note_id):
    if request.method == 'GET':
        note = get_object_or_404(Note, note_id=note_id)
        note = NoteSerializer(note).data
        return JsonResponse(note,safe=False, status=200)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

def get_note_content(request,note_id):
    if request.method == 'GET':
        note = get_object_or_404(Note, note_id=note_id)
        contents = note.contents.all()
        contents = ContentSerializer(contents, many=True).data
        print(contents)
        note = NoteSerializer(note).data
        return JsonResponse({"contents":contents,"note":note}, status=200)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    

def download_file(request, content_id):
    file_instance = get_object_or_404(Content, content_id=content_id)
    file_path = file_instance.file.path
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
        return response
    except FileNotFoundError:
        raise Http404("File not found")
    
def delete_content(request,content_id):
    if request.method == 'POST':
        content = get_object_or_404(Content, content_id=content_id)
        print(ContentSerializer(content).data)
        if content.file and content.file.name:
            print(f"Deleting old file: {content.file.name}")
            default_storage.delete(content.file.name)
        if content is not None:
            content.delete()
        
        return JsonResponse({'message': 'Content deleted'}, status=200)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

def delete_note(request,note_id):
    if request.method == 'POST':
        note = get_object_or_404(Note, note_id=note_id)
        contents = note.contents.all()
        print(NoteSerializer(note).data)
        for content in contents:
            if content.file and content.file.name:
                    print(f"Deleting old file: {content.file.name}")
                    default_storage.delete(content.file.name)
            if content is not None:
                content.delete()   
        if note is not None:
            note.delete()
        return JsonResponse({'message': 'Note deleted'}, status=200)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)