from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # Катталгандан кийин дароо сайтка киргизип коюу үчүн (каалоого жараша)
from django.http import HttpRequest, HttpResponse

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Колдонуучуну маалымат базасына сактайт
            login(request, user)  # Катталгандан кийин дароо логин кылгыңыз келсе ушул сапты ачып койсоңуз болот
            return redirect("post_list")  # Логин баракчасына багыттайт
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})