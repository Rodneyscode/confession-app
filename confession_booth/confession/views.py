from django.shortcuts import render, redirect
from .forms import WriteAConfessionForm
from .models import AllConfessions

def MainPage (requests):
	return render(requests, 'first_temp.html')

def WriteConfessions (requests):
	if requests.method == "POST":
		confession = WriteAConfessionForm(requests.POST)
		if confession.is_valid():
			confession.save()
			return redirect('confessionviewing')

	else:
		confession = WriteAConfessionForm()

	return render (requests, 'write_a_confession.html', {'confessform': confession})



def ViewConfessions (requests):

	allconfessions = AllConfessions.objects.order_by('-id')

	return render(requests, 'view_confessions.html' , {'allconfessions': allconfessions})

