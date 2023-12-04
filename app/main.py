from fastapi import FastAPI
from worker import create_task
import logging

app = FastAPI()

# 체험해보기 메인 : 로그인 안해도 접근가능
@app.get("/")
def root():
    return {"result": "hi"}

@app.get("/req")
def add_task():
    logging.warning(f"task start")
    task = create_task.apply_async()
    logging.warning(f"task id : {task.id}")
    return {"req": "hello"}