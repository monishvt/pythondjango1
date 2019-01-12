from django.shortcuts import render

# Create your views here.


def index(request):
	context={'text':'hello baabtra', 'number':'100'}
	return render(request, 'index.html', context)


def other(request):
	return render(request, 'other.html')


def relative(request):
	return render(request, 'relative_url_template.html')
