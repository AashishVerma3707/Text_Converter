import requests
from django.shortcuts import render
from . import linkss

def body(request):
    if request.POST.get("Input") is None:
        id = request.POST.get("Article_id")

        def get_token():
            url="http://127.0.0.1:7000/api/auth/"
            response= requests.post(url,data={'username':request.POST.get("Username"),
                                              'password':request.POST.get("Password")})
            return response.json()

        def get_body():

            url = f"http://127.0.0.1:7000/api/article_body/{id}/"
            header = {'Authorization': f'Token {get_token()}'}
            response = requests.get(url, headers=header)
            y = response.json()
            return y["body"]

        return render(request,"blog.html", {"Article_body":get_body(),"Token":get_token(),"id":id})
    else:
        id=request.POST.get("id")
        token = request.POST.get("Token")
        token=token
        body=request.POST.get("Input")
        body=linkss.spellcheck(body)
        data={"body":str(body)}
        print(body)
        Url=f"http://127.0.0.1:7000/api/article_body/{id}/"
        header = {'Authorization': f'Token {token}'}
        response = requests.put(Url,data=data, headers=header)
        print(body)
        u= response.json()["body"]
        return render(request, "blog.html",{"content":u})