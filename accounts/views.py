from django.shortcuts import redirect, render
from accounts.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts import forms

# Create your views here.

# SignUp
def signup(request):
	msg=None
	if request.method=='POST':
		form=forms.SignUp(request.POST)
		if form.is_valid():
			form.save()
			msg='Thank you for register.'
	form=forms.SignUp
	return render(request, 'registration/signup.html',{'form':form,'msg':msg})


def signin(request):
	msg=''
	if request.method=='POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')
		# if trainer > 0:
		# 	trainer=models.Trainer.objects.filter(username=username,pwd=pwd).first()
		# 	request.session['trainerLogin']=True
		# 	request.session['trainerid']=trainer.id
		# 	return redirect('/trainer_dashboard')
		# else:
			# msg='Invalid!!'
	# form=forms.TrainerLoginForm
	return render(request, 'registration/login.html',{'msg':msg})


@unauthenticated_user
def registerPage(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/signup.html', context)   
	



@unauthenticated_user
def loginPage(request):	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'auth/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

