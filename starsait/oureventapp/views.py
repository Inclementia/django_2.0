from django.shortcuts import render

from oureventapp.models import OurEvent


def events(request):
    events = OurEvent.objects.all()
    context = {
        'events': events,
        'page_title': 'мероприятия'
    }
    return render(request, 'ourevent/event.html', context)
