from django.shortcuts import render, redirectfrom django.contrib.auth import login as loginSys, logout, authenticatefrom loginSys import functionsdef index (request):		return render(request, 'index.html')