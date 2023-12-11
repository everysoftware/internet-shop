from app.api.auth.router import router as auth_router
from app.api.goods.router import router as goods_router

routers = (
    auth_router,
    goods_router,
)
