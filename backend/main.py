from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.v1.endpoints import translate

app = FastAPI()

# 挂载静态文件
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# 模板引擎
templates = Jinja2Templates(directory="frontend")

# 包含API路由
app.include_router(translate.router, prefix="/api/v1")

# 更新
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
