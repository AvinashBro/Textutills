#I have created this file
#!st Page By using jango
from django.http import HttpResponse  #As view returns an http response so we have to use HttpResponse
def index(request):
    return HttpResponse('''<h1>Avinash_Ojha</h1>
    <a href ="https://www.geeksforgeeks.org/python-oops-concepts/" >Link : 1</a>
    <a href="https://www.w3schools.com/html/html_links.asp" target="blank"> Link : 2</a>
    <a href="https://www.udemy.com/course/python-django-the-practical-guide/" >
    <img src="Desktop\Avinash.jpg" style="width:72px;height:62px;"></a>
    ''')
def about(request):
    return HttpResponse("Hello About")