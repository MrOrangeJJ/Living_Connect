from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from .models import AuthorizedEmail

# Create your views here.
class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        if not AuthorizedEmail.objects.filter(email=email, is_registered=False).exists():
            return Response({"detail": "Email is not authorized or already registered."},
                            status=status.HTTP_400_BAD_REQUEST)
        response = super().create(request, *args, **kwargs)
        
        # If registration is successful, update the AuthorizedEmail object
        if response.status_code == status.HTTP_201_CREATED:
            authorized_email = AuthorizedEmail.objects.get(email=email)
            authorized_email.is_registered = True
            authorized_email.save()
        return response