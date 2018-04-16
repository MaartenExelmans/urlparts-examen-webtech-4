from django.shortcuts import render


def urlparts(request, URLText):
    links = URLText.strip('/').split('/')
    urls = []
    total = links.length -1
    for i, link in links:
        if not link == '':
            urls.append(link)
            if not i == total:
                urls.append(" -- ")


    return render(request, 'urlparts.html', {'URLText': URLText})

def get_current_path(request):
    return {
        'current_path': request.path()
    }


