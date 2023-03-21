from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse


from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def kontenjan(request):


    return render(request,"kontenjan.html")

# def ebe21(request):
#     items = Ebe.objects.all()
#     context = {
#         'items': items,
#         'header':'Ebelik Bölümü 2021',

#     }

#     return render(request,"kontenjan.html",context)

# def hemsire21(request):
#     items = Hemsire.objects.all()
#     context = {
#         'items': items,
#         'header':'Hemsire Bölümü 2021',

#     }

#     return render(request,"kontenjan.html",context)

# def ebe20(request):

#     items = Ebe.objects.all()
#     context = {
#         'items': items,
#         'header':'Ebelik Bölümü 2020',

#     }

#     return render(request,"kontenjan.html",context)

# def s2021(request):

#     items = S2021.objects.all()
#     context = {
#         'items': items,
#         'header':'Sınav Sonuçları 2021',

#     }

#     return render(request,"kontenjan.html",context)


# def ebe222(request):
    
#     items = S2021.objects.filter(punvani="EBE")
#     context = {
#             'items': items,
#             'header':'Ebelik Bölümü 2021',
    
#         }
    
#     return render(request,"kontenjan.html",context)

# def ebe(request):
#     unique_punvani = S2021.objects.values_list('punvani', flat=True).distinct()
#     context = {
#         'unique_punvani': unique_punvani,
#     }
#     return render(request,"kontenjan.html",context)

# def s2021(request,id):

#     items = S2021.objects.filter(punvani=id)
#     context = {
#             'items': items,
#             'header':id,
    
#         }
    
#     return render(request,"kontenjan.html",context)

def s2021(request):
    punvani = S2021.objects.values_list('punvani', flat=True).distinct()

    keyword = request.GET.get("keyword")
    
    
    if keyword :
        keyword=keyword.replace("i","İ").replace("ı","I").replace("ö","Ö").replace("ü","Ü").replace("ç","Ç").replace("ş","Ş").replace("ğ","Ğ").replace(" ","").upper()
        items   = S2021.objects.filter(sehir__contains = keyword)

        return render(request,"kontenjan.html",
                      {"items":items})
    
    items = S2021.objects.all()    
    context = {
        'items': items,
         'header':'Sınav Sonuçları 2021',
        'punvani': punvani,
        
     }

    return render(request,"kontenjan.html",context)

def s2021filter(request,id):
        # items = get_object_or_404(S2021, id=id)
        items = S2021.objects.filter(punvani=id)
        # id = id.replace("-"," ").lower().replace("o","ö").replace("u","ü").replace("c","ç").replace("s","ş").replace("g","ğ").replace("i","ı").title() 
        context = {
                'items': items,
                'header':id,
                # 'path': id.lower().replace(" ","-").replace("ö","o").replace("ü","u").replace("ç","c").replace("ş","s").replace("ğ","g").replace("ı","i"),

        
            }
        
        return render(request,"kontenjan.html",context)


