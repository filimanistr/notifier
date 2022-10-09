from app import views

def setup_routes(app):
   app.router.add_get("/", views.index)
   app.router.add_get("/notify", views.notify)
   app.router.add_post("/notify/certain_users", views.notify_certain_users)
   app.router.add_post("/auth/callback", views.onTelegramAuth)
   app.router.add_static('/static', path='static')

