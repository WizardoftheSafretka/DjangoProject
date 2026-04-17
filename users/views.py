import secrets
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{user.token}/'

        try:
            send_mail(
                subject='Подтверждение почты',
                message=f'Привет! Перейди по ссылке для подтверждения почты: {url}',
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Ошибка отправки письма: {e}")
            messages.error(self.request, "Ошибка при отправке письма. Попробуйте позже.")
            return redirect("users:register")

        messages.success(self.request, "Письмо с подтверждением отправлено на вашу почту.")
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)

    if user.is_active:
        messages.info(request, "Аккаунт уже активирован. Войдите в систему.")
        return redirect(reverse("users:login"))

    user.is_active = True
    user.token = None
    user.save()

    messages.success(request, "Почта подтверждена! Теперь вы можете войти.")
    return redirect(reverse("users:login"))