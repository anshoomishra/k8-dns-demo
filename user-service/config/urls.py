from django.http import JsonResponse
from django.urls import path


def users(request):
    return JsonResponse(
        {
            "service": "user-service",
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"},
            ],
        }
    )


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("api/users/", users),
    path("health/", health),
]
