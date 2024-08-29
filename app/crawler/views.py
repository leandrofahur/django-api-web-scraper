from django.http import HttpResponse
import django_rq
from task import example_task

def my_view(request):
    # Enqueue the example task
    queue = django_rq.get_queue('default')
    queue.enqueue(example_task, 10)  # Runs for 10 seconds
    return HttpResponse("Task has been enqueued!")