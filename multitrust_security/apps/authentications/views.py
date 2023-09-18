from django.shortcuts import render ,redirect


# Create your views here.


class Pages:

    def login(request):
        return render(request, 'authentications/login.html')

    def register(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            print(username, "   ", password)

            return redirect('/')

        return render(request, 'authentications/register.html')
