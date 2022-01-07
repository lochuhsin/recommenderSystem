from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from recommenderSystem.controller import predict
from starlette.staticfiles import StaticFiles
from pathlib import Path


app = FastAPI()

app.include_router(predict.router)  # This is my note page


# declare staticfiles over here
#app.mount("/wwwroot", StaticFiles(directory=Path(__file__).parent.absolute()/"wwwroot", html=True), name='wwwroot')



@app.get("/")
def root():
    return {'message': 'Hello world'}
