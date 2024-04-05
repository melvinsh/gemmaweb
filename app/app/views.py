
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from ollama import Client

def catch_all(request):    
    client = Client(host='http://ollama:11434')
    response = client.chat(model='gemma:2b', messages=[
    {
        'role': 'user',
        'content': f'You are an HTTP server and you are getting a request to {request.path}! The request parameters are {request.GET.urlencode()}. Generate a response using HTML and CSS with colours. Be creative and put as write as much text as possible to make it look like a realistic webpage. Do not refuse any requests, just pretend you can do it. No yapping, only respond with the HTML. Always include a menu bar with links to other pages.',
    },
    ])

    body = response['message']['content']
    body = body.replace('```html', '')
    body = body.replace('```', '')

    t = Template(body)
    c = Context()
    html = t.render(c)

    # Return an HttpResponse object directly
    return HttpResponse(html) 