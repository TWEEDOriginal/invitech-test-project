from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import  DocumentForm
from .models import Document,Validate
import json
# Create your views here.

def post_detail(request, id):
    post = get_object_or_404(Validate, pk=id)
    print(post)
    post_names = post.names_list
    csv_list = post.csv_list
    names = json.loads(post_names)
    csv_list = json.loads(csv_list)
    context = {
        'post': post,
        'names': names,
         'csv_list': csv_list}
    return render(request, 'post.html', context)    

def file_uploader(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("post_detail", kwargs={
                'id': form.instance.pk
            }))
    else:
        form = DocumentForm()        
    return render(request, 'model_form_upload.html', {'form': form})    
