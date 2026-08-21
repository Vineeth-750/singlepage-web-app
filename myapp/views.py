from django.shortcuts import render, redirect
from .models import UserDetails


def user_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        UserDetails.objects.create(
            name=name,
            age=age,
            phone=phone,
            address=address
        )

        return redirect("user_form")

    return render(request, "index.html")