from fastapi import FastAPI

# from ring.config import get_config
# from ring.worker import hello_task

# ring_config = get_config()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/hello")
async def hello():
    # task = hello_task.delay()
    # return {"task_id": task.id}
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # type: ignore
