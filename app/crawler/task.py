# app/crawler/tasks.py
import time
import django_rq

def example_task(duration):
    print(f"Task starting for {duration} seconds...")
    time.sleep(duration)
    print("Task completed!")

# To enqueue the task, you can use the following line in your view or any other place in your code:
django_rq.enqueue(example_task, 10)  # This enqueues the task to run for 10 seconds