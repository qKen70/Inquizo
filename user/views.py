from django.shortcuts import render
from .models import User
from .form import RegistrationForm

def registration(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                exist_user = User.objects.get(email=email)
                if not exist_user.is_active:
                    exist_user.delete()
                else:
                    return render(request, 'auth/registration.html', {
                        'form': form,
                        'error': 'Данный пользователь уже существует'
                    })
            except User.DoesNotExist:
                pass

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # Подтверждение через почту (пока не реализовано)

            return render(request, 'auth/regisrt_email_message.html', {'email': email})

    return render(request, 'auth/registration.html', {'form': form})