from fastapi import FastAPI
from task import sample_task

app = FastAPI()


@app.get("/test")
def test():
    sample_task.apply_async()
    return {'MESSAGE': 'Task Submitted'}
