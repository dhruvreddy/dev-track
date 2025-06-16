from fastapi import FastAPI, Response, status
import uvicorn

from dependency_injection import create_all_di
from routers import user_router, token_router, task_router, report_router
app = FastAPI()
app.include_router(user_router)
app.include_router(token_router)
app.include_router(task_router)
app.include_router(report_router)

@app.get("/")
def home():
    return Response(content="DevTrack", status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    create_all_di()
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
