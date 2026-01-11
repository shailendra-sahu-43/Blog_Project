from celery import shared_task

@shared_task
def test_task():
    print("Celery + Redis working")
    return "OK"
