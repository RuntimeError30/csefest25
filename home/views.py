from django.shortcuts import render, get_object_or_404
from django.core import signing
from django.http import HttpResponse
from django.http import FileResponse
from .models import events, announcements, timeLine, prizeMoney, contactInfos, guidelines

def home(request):
    all_events = events.objects.all()
    for event in all_events:
        event.signed_id = signing.dumps(event.id)
    
    all_announcements = announcements.objects.all()
    return render(request, "index.html", {
        'events': all_events,
        'announcements': all_announcements
    })

def eventdetails(request, signed_event_id):
    try:
        event_id = signing.loads(signed_event_id)
        event = get_object_or_404(events, id=event_id)
    except signing.BadSignature:
        return render(request, "error.html", {"message": "Invalid event link"})
    
    # Retrieve related models
    timelines = timeLine.objects.filter(event=event).first()
    prizes = prizeMoney.objects.filter(event=event).first()
    contacts = contactInfos.objects.filter(event=event)
    guidelines_list = guidelines.objects.filter(event=event)

    # Pass individual timeline fields
    context = {
        'event': event,
        'timelines': timelines,
        'prizes': prizes,
        'contacts': contacts,
        'guidelines': guidelines_list,
        'timeline_fields': [
            timelines.timeline_01, timelines.timeline_02, timelines.timeline_03, 
            timelines.timeline_04, timelines.timeline_05, timelines.timeline_06,
            timelines.timeline_07, timelines.timeline_08, timelines.timeline_09,
            timelines.timeline_10
        ] if timelines else []
    }

    return render(request, "eventdetails.html", context)

def view_guideline(request, guideline_id):
    guideline = get_object_or_404(guidelines, id=guideline_id)
    return FileResponse(guideline.guideline_pdf, content_type='application/pdf')

def eventcredits(request):
    return render(request, "credits.html")
