

import path
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from fastapi import Depends, FastAPI, Path, Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static',StaticFiles(directory="static"),name="static")
SECRET = "super-secret-key"
manager = LoginManager(SECRET, '/login',use_cookie=True)
manager.cookie_name = "some-name"


DB = {
    'users': {
        'youssef': {
            'name': 'youssef',
            'password': 'nari'
        }
    }
}

@manager.user_loader()
def query_user(user_id: str):
    return DB['users'].get(user_id)

@app.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = query_user(username)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data={"sub":username}
    )
    resp = RedirectResponse(url="/private",status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp,access_token)
    return resp

@app.get("/private")
def getPrivateendpoint(request:Request,_=Depends(manager)):
    return templates.TemplateResponse("counter.html",{'request': request})


#pth = path.dirname(__file__)

@app.get("/")
def loginwithCreds(request:Request):
        return templates.TemplateResponse("login.html",{'request': request})

@app.get("/index")
def Creds(request:Request):
        return templates.TemplateResponse("index.html",{'request': request})

# @app.get('/login')
# def login(request: Request):
#     return templates.TemplateResponse("login.html",{"request":request})





















# @app.get('/login')
# def login(request: Request):
#     return templates.TemplateResponse("login.html",{"request":request})



# @app.get("/")
# def index():
#     return {"name": "youssef I am here"}


# @app.get("/getstudents/{student_id}")
# def index(student_id: int = Path(None,description = "id of student",gt=1,lt=2)):
#     return Students[student_id]  