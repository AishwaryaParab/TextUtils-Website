# I have created this file - Aishwarya
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Aishwarya', 'place': 'Goa'}
    return render(request, 'index.html', params)
    #            request  template name  dict

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    text_entered = request.POST.get('text', 'default')

    #Check the value of the checkbox
    remove_punctuations = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('caps', 'off') 
    remove_new_line = request.POST.get('newlineremover', 'off')
    space_remover = request.POST.get('spaceremover', 'off')
    char_count = request.POST.get('charcount', 'off')

    if remove_punctuations == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
        analyzed = ""
        for char in text_entered:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        text_entered = analyzed
        # return render(request, 'analyze.html', params)
    
    if capitalize == "on":
        analyzed = ""
        for char in text_entered:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text_entered = analyzed
        # return render(request, 'analyze.html', params)

    if remove_new_line == "on":
        analyzed = ""
        for char in text_entered:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        text_entered = analyzed
        # return render(request, 'analyze.html', params)

    if space_remover == "on":
        analyzed = ""
        for index, char in enumerate(text_entered):
            if not(text_entered[index] == " " and text_entered[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        text_entered = analyzed
        # return render(request, 'analyze.html', params)
    
    if char_count == "on":
        count = 0
        for char in text_entered:
            count = count + 1
        analyzed = "Total number of characters in your text: " + str(count)
        params = {'purpose': 'Counted Characters', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if remove_punctuations!="on" and capitalize!="on" and remove_new_line!="on" and space_remover!="on" and char_count!="on":
        return HttpResponse("Error. Please select an appropriate operation and try again.")

    return render(request, 'analyze.html', params)


# def removepunc(request):
#     print(request.GET.get('text', 'default'))
#     return HttpResponse("Remove Punctuation")

# def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlineremove(request):
#     return HttpResponse("Newline Remove")

# def spaceremove(request):
#     return HttpResponse("Space Remover")

# def charcount(request):
#     return HttpResponse("Character Count")