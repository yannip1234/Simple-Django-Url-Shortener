from django.shortcuts import render
from .models import URL
from .forms import CreateURLForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    if request.method == "POST":
        form = CreateURLForm(request.POST)
        if form.is_valid():
            print("OK")
            original_url = form.cleaned_data['original_url']
            shortened_path = form.cleaned_data['shortened_path']
            print(URL.objects.filter(shortened_path=shortened_path).count())
            if URL.objects.filter(shortened_path=shortened_path).count() is 1:
                print("OK")
                return render(request, "shorten/index.html", {
                    "form": CreateURLForm(request.POST, 'error'),
                    "error": -1
                })
            else:
                new_url = URL(original_url=original_url, shortened_path=shortened_path)
                new_url.save()
                return render(request, "shorten/result.html", {
                    "url": original_url,
                    "path": shortened_path
                })
        else:
            return render(request, "shorten/index.html", {
                "form": form
            })

    return render(request, "shorten/index.html", {
        "form": CreateURLForm()
    })


def url_go(request, url_id):
    url = URL.objects.get(shortened_path=url_id)
    return HttpResponseRedirect(url.original_url)

# def result(request):
