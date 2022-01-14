from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from recommenderSystem.controller import predict
from recommenderSystem.config import appconfigs




app = FastAPI()
app.include_router(predict.router)  # This is my note page


# declare staticfiles over here
#app.mount("/wwwroot", StaticFiles(directory=Path(__file__).parent.absolute()/"wwwroot", html=True), name='wwwroot')



@app.get("/")
def root():
    settings=Settings()
    return {'message': 'Hello world',
            'env': settings.env}
