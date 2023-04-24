from django.shortcuts import get_object_or_404, render
from hometasks.models import Hometask


def hometasks_list(request):
    hometasks = Hometask.objects.all()
    return render(request, "hometasks/tasks/list.html", {"hometasks": hometasks})


def hometask_retrieve(request, id):
    hometask = get_object_or_404(Hometask, id=id)

    return render(request, "hometasks/tasks/retrieve.html", {"hometask": hometask})
