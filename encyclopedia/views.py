import os
import random as random_library

from django.shortcuts import render

from . import util
from .forms import SearchForm, EncyclopediaForm


def index(request):
    context = {
        "entries": util.list_entries(),
        'form': SearchForm(),
    }

    return render(request, "encyclopedia/index.html", context)


def detail(request, title):
    data = util.get_entry(title)
    if data is None:
        return render(request, "encyclopedia/404.html")
    context = {
        'title': title,
        'data': data,
    }
    return render(request, "encyclopedia/detail.html", context)


def search(request):
    entries = util.list_entries()
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = form.data.get('text')

        if text in entries:
            data = util.get_entry(text)
            context = {
                'title': text,
                'data': data,
            }
            return render(request, "encyclopedia/detail.html", context)
        else:
            data = []
            for e in entries:
                if text in e:
                    data.append(e)
            context = {
                'text': text,
                'entries': data,
            }
            return render(request, "encyclopedia/search.html", context)


def add(request):
    if request.method == 'POST':
        form = EncyclopediaForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            title = form.cleaned_data['title']
            entries = util.list_entries()
            if title in entries:
                return render(request, "encyclopedia/entry_exist_error.html")

            util.save_entry(title, text)
            return render(request, "encyclopedia/index.html")

    return render(request, "encyclopedia/add.html", {
        'enc_form': EncyclopediaForm(),
    })


def edit(request, title):
    print(request.method)
    print(title)
    # TODO: da se dodade edit


def random(request):
    pages = os.listdir('encyclopedia/templates/encyclopedia')
    idx = random_library.randint(0, len(pages))

    entries = util.list_entries()
    idx2 = random_library.randint(0, len(entries))

    if pages[idx] in ['detail.html', 'edit.html']:
        return render(request, f"encyclopedia/{pages[idx]}/{entries[idx2]}")

    return render(request, f"encyclopedia/{pages[idx]}")
