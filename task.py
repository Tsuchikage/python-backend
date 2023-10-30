from celeryconfig import app
import time


@app.task
def sample_task():
    for i in range(10):
        time.sleep(1)
    print("Task Completed")
