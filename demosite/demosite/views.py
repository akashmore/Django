from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','default')
    is_remove_punctuation = request.POST.get('isRemovePunctuation','off')
    is_upper = request.POST.get('isUpper','off')
    char_count = request.POST.get('showcount','off')
    output = {}
    output["final_str"] =""
    if is_remove_punctuation=="on":
        punctuation = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
        for ele in text:
            if ele in punctuation:
                pass
            else:
                output["final_str"]=output["final_str"]+ele
    if is_upper=="on":
        output["final_str"] = output["final_str"].upper()
    
    if char_count == "on":
        if len(output["final_str"]) == 0:
            output["char_count"] = len(text)
        else:
            output["char_count"] = len(output["final_str"])

    return render(request,'output.html',output)
