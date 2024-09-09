#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
                          
    

def analyze(request):
    ptext=request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps', 'off')
    newlineremover=request.GET.get('newlineremover', 'off')
    extraspaceremover=request.GET.get('extraspaceremover', 'off')
    charcount=request.GET.get('charcount', 'off')
    print(removepunc)
    print(ptext)
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in ptext:
            if char not in punctuations:
               analyzed=analyzed + char
        params= {'purpose':'removed punctuations', 'analyzed_text':analyzed}
        ptext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (fullcaps=="on"):
        analyzed=""
        for char in ptext:
            analyzed=analyzed+char.upper()
        params= {'purpose':'changed to uppercase ', 'analyzed_text':analyzed}
        ptext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (newlineremover=="on"):
        analyzed=""
        for char in ptext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        params= {'purpose':'removed newlines  ', 'analyzed_text':analyzed}
        ptext=analyzed
        # return render(request, 'analyze.html', params)        
    
    if (extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(ptext):
            if not (ptext[index]==" " and ptext[index+1]==" "): 
       
                analyzed=analyzed+char
        params= {'purpose':'extra space removed ', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)  

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on"):
        return HttpResponse("ERROR NO BUTTON HAS BEEN ON")
    
    return render(request, 'analyze.html', params)

    # elif (charcount=="on"):
    #     analyzed=""
    #     for index, char in enumerate(ptext):
    #         if  ptext[index] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #             totalcount=ptext.count(char)
    #             analyzed=f"total  {char} count is {totalcount}"

    #     # totalcount=len(ptext)
    #     # # analyzed=f"totalcount is:{totalcount}"      
    #     params= {'purpose':'character counting done ', 'analyzed_text':analyzed}
    #     return render(request, 'analyze.html', params)    


    
    
    

# def capfirst(request):
#     return HttpResponse("captitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remover")

# def spaceremover(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("can count character")


# def about(request):
#     return HttpResponse("hello jacob about me")