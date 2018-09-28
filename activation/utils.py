from .models import User, Nurse, Message, Coordinator, EscalationLevel
from django.db.models import Q


def load_user(request):
    if not request.user.is_authenticated:
        return redirect("/activation/login")

    print(request.user.username)
