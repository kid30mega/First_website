from django.shortcuts import render


rooms = [
    {"id": 1, "name": "let learn python!"},
    {"id": 2, "name": "design with me"},
    {"id": 3, "name": "Fronted develop"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request):
    return render(request, "base/room.html")
