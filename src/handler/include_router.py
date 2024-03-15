from loader import dp
from .v1 import user_router


dp.include_router(user_router)