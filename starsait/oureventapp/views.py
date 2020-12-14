from django.shortcuts import render

from mainapp.models import OurEvent


def events(request):
    events = CategorySight.objects.all()
    context = {
        'events': events,
        'page_title': 'мероприятия'
    }
    return render(request, 'ourevent/event.html', context)
