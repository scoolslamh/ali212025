from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip().lower()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password')

        # التحقق من الحقول الفارغة
        if not username or not email or not phone or not password:
            messages.error(request, 'يرجى تعبئة جميع الحقول.')
            return render(request, 'accounts/register.html')

        # التحقق من وجود بيانات مكررة
        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم مستخدم مسبقًا.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'البريد الإلكتروني مستخدم مسبقًا.')
        elif Profile.objects.filter(phone=phone).exists():
            messages.error(request, 'رقم الجوال مستخدم مسبقًا.')
        else:
            # إنشاء المستخدم
            user = User.objects.create_user(username=username, email=email, password=password)

            # إنشاء الملف الشخصي
            Profile.objects.create(user=user, phone=phone, email=email)

            # إرسال بريد ترحيبي
            try:
                send_mail(
                    subject='مرحبًا بك في موقعنا!',
                    message=f'أهلًا {username}، نشكرك على تسجيلك معنا. نتمنى لك تجربة ممتعة.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                print("❌ فشل إرسال البريد:", e)

            messages.success(request, '✅ تم إنشاء الحساب بنجاح. يمكنك تسجيل الدخول الآن.')
            return redirect('accounts:login')  # ← تم التصحيح هنا

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'يرجى إدخال اسم المستخدم وكلمة المرور.')
            return render(request, 'accounts/login.html')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, f'مرحبًا {user.username} 👋')
            return redirect('home')  # ← عدل المسار حسب ما يناسب مشروعك
        else:
            messages.error(request, '❌ اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    auth_logout(request)
    messages.info(request, '🚪 تم تسجيل الخروج بنجاح.')
    return redirect('accounts:login')  # ← تم التصحيح هنا
