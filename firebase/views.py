from django.shortcuts import render

# Create your views here.
def firebase_detail(request):
    # project = Project.objects.get(pk=pk)
    firebase = 0
    context = {
        'project': firebase
    }
    return render(request, 'firebase_detail.html', context)
