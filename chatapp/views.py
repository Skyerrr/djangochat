from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .models import Room, Message


def frontpage(request):
    return render(request, "base.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("frontpage")

    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


@login_required
def view_rooms(request):
    rooms = Room.objects.all()

    return render(request, "rooms.html", {"rooms": rooms})


@login_required
def view_room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, "room.html", {"room": room, "messages": messages})
