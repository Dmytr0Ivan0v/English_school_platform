from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from hometasks.models import Hometask


def hometasks_list(request):
    hometasks_list = Hometask.objects.all()
    paginator = Paginator(hometasks_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        hometasks = paginator.page(page_number)
    except PageNotAnInteger:
        hometasks = paginator.page(1)
    except EmptyPage:
        hometasks = paginator.page(paginator.num_pages)
    return render(request, "hometasks/tasks/list.html", {"hometasks": hometasks})


def hometask_retrieve(request, year, month, day, hometask):
    hometask = get_object_or_404(
        Hometask,
        slug=hometask,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )

    return render(request, "hometasks/tasks/retrieve.html", {"hometask": hometask})
