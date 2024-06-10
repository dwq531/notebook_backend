from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .forms import UserForm
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.http import Http404
import os
from django.conf import settings
def upload_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user_id = user_form.cleaned_data.get('user_id')
            user, created = User.objects.get_or_create(user_id=user_id, defaults=user_form.cleaned_data)
            if created:
                message = 'User created'
            else:
                if user.image and user.image.name:
                    file_path = os.path.join(settings.MEDIA_ROOT, user.image.name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleting old file: {file_path}")
                for field, value in user_form.cleaned_data.items():
                    setattr(user, field, value)
                user.save()
                message = 'User updated'
            return JsonResponse({'message': message}, status=200)
        else:
            print(user_form.errors)
            return JsonResponse({'message': 'Invalid form'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

def get_user_by_name(request,username):
    if request.method == 'GET':
        user = User.objects.filter(username=username).first()
        print(UserSerializer(user).data)
        if user:
            return JsonResponse(UserSerializer(user).data,safe=False, status=200)
        else:
            return JsonResponse({'message': 'User not found'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)
    
def download_file(request,user_id):
    user = get_object_or_404(User, user_id=user_id)
    file_path = user.image.path
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{user.image.name}"'
        return response
    except FileNotFoundError:
        raise Http404("File not found")