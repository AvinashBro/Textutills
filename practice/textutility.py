from django.http import HttpResponse  #As view returns an http response so we have to use HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse( "Home")
    return render(request,'index.html')
def analyze(request):

    # check th echeck box value
    djtext = request.POST.get('text', 'default') # "TO INCREASE the security of data GET is replaced by POST"  djtext = request.GET.get('text', 'default')  # get the text # get the text
    removepunc = request.POST.get('removepunc', 'off')  # get the text
    capital=request.POST.get('capital', 'off')
    extraspaceremover =request.POST.get('extraspaceremover','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    chcount = request.POST.get('chcount', 'off')
    #print(newlineremover)
    '''print(djtext) #PRINTS IN TERMINAL ONLY
    print(removepunc)'''
    #analyzed=djtext

    #Check Which Check box is on
    if removepunc=='on':
        punctuations ='''!()-[]{};:'"\,<>./?%$@#^&*_~`'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i

        parameter={'purpose': 'Remove_Punctations' , 'analyzed_text': analyzed }
        return(render( request,'analyze.html',parameter))
    elif(capital=='on'):
        analyzed=djtext.upper()
        parameter = {'purpose': 'Capitalized statement', 'analyzed_text': analyzed}
        return (render(request, 'analyze.html', parameter))

    elif(extraspaceremover == 'on'):
        analyzed=""
        for index,i in enumerate(djtext):

            if (djtext[index]==" " and  djtext[index+1]==" "):
                pass
            else:
                analyzed= analyzed+i
        parameter = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        return(render(request,'analyze.html',parameter))

    elif (newlineremover == 'on'):
        analyzed = ""
        for i in (djtext):
            if (i !="\n" and i!="\r"):
                analyzed = analyzed + i
        print("hello",analyzed)
        parameter = {'purpose': 'Extra Line Removed', 'analyzed_text': analyzed}
        return (render(request, 'analyze.html', parameter))

    elif (chcount == 'on'):
        count = 0
        for i in djtext:
            count=count+1

        parameter = {'purpose': 'Extra Space Removed', 'analyzed_text': count}
        return (render(request, 'analyze.html', parameter))
    else:
        return HttpResponse("Error")

'''def removepunc(request):
   # print(request.GET.get('text','default')) #it will get the value of textaraea usng name "text" and if no text is given then default will be executed
    djtext=request.GET.get('text','default') #get the text
    print(djtext) #Analyse the text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnzz
    return HttpResponse("removepunc <a href='/'>back</a>")
def capitalfirst(request):
    return HttpResponse("capitalfirst <a href='/'>back</a>")
def newlineremove(request):
    return HttpResponse("newlineremov <a href='/'>back</a>")
def spaceremover(request):
    return HttpResponse("spaceremover <a href='/'>back</a>")
def charcount(request):
    return HttpResponse("charcount <a href='/'>back</a>")'''
