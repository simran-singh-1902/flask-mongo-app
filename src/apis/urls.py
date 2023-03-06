from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/add-users", views.dummy_data, ["GET"], "Adding dummy data"),
    ("/login", views.login, ["POST"], "Login api for the app"),
]

other_urls = []

all_urls = api_urls + other_urls
