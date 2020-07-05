from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            new_img = form.save(commit=False)
            new_img.user = request.user
            new_img.save()
            messages.success(request, 'Image added successfuly')
            return redirect(new_img.get_absolute_url())

    else:
        form = ImageCreateForm(request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})
