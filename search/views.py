from django.shortcuts import render
from .documents import PostDocumnet


# Create your views here.
def search(request):
    q = request.GET.get('q')
    if q:
        feedback = PostDocumnet.search().query('match', check=q)
    else:
        feedback = ''
    return render(request, 'search/search.html', {
        'feedback': feedback
    })