from django.shortcuts import render
from django.http import HttpResponse
from .models import Patents

def get_data(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        print(searched)
        patents = Patents.objects.raw("SELECT id, patent_id FROM patents WHERE MATCH(patent_name) AGAINST ('%s' IN NATURAL LANGUAGE MODE)" %searched)
        return render(request, 'search-patents.html', {'patents': patents})
    else:
        return render(request, 'search-patents.html')
