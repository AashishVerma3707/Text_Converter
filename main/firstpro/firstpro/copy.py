# import requests
# from django.shortcuts import render
#
#
# def body(request):
#     def get_token():
#         url="http://127.0.0.1:8000/api/auth/"
#         response= requests.post(url,data={'username':request.POST.get("Username"),
#                                           'password':request.POST.get("Password")})
#         return response.json()
#
#     def get_body():
#         id=request.POST.get("Article_id")
#         url = f"http://127.0.0.1:8000/api/article_body/{id}/"
#         header = {'Authorization': f'Token {get_token()}'}
#         response = requests.get(url, headers=header)
#         return response.text
#     return render(request,"blog.html", {"Article_body":get_body()})
#
# # def get_data():
# #     url="http://127.0.0.1:8000/api/article_body/"
# #     header={'Authorization':f'Token {get_token()}'}
# #     response= requests.get(url, headers=header)
# #     data1=response.json()
# #     for i in data1:
# #         print(i)
# # def get_body(id):
# #     url=f"http://127.0.0.1:8000/api/article_body/{id}/"
# #     header = {'Authorization': f'Token {get_token()}'}
# #     response=requests.get(url,headers=header)
# #     return response.json()
# #
# # def rectify(id):
# #     url=f"http://127.0.0.1:8000/api/article_body/{id}/"
# #     header = {'Authorization': f'Token {get_token()}'}
# #     data={"body":"uuuuuuuuuuuuuuuuu"}
# #     response = requests.put(url,data=data, headers=header)
# #     return response.json()
# #
# #
# # print(get_body(15))
#
#
#
# import requests
# def get_token():
#     url="http://127.0.0.1:7000/api/auth/"
#     response= requests.post(url,data={'username':'aashish3707a',
#                                       'password':"Creepyghost1"})
#     return response.json()
#
# def get_data():
#     url="http://127.0.0.1:7000/api/article_body/"
#     header={'Authorization':f'Token {get_token()}'}
#     response= requests.get(url, headers=header)
#     data1=response.json()
#     for i in data1:
#         print(i)
# def get_body(id):
#     url=f"http://127.0.0.1:7000/api/article_body/{id}/"
#     header = {'Authorization': f'Token {get_token()}'}
#     response=requests.get(url,headers=header)
#     return response.json()
#
# def rectify(id):
#     url=f"http://127.0.0.1:7000/api/article_body/{id}/"
#     header = {'Authorization': f'Token {get_token()}'}
#     data={"body":"uuuuuuuuuuuuuuuuu"}
#     response = requests.put(url,data=data, headers=header)
#     return response.json()
#
#
# # print(get_body(15))
# y="hello"
# print(type(y))
# u=y.encode()
# print(type(u))
