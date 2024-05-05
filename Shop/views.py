from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,order,updateorder
import math
import json
from django.views.decorators.csrf import csrf_exempt
import razorpay


def index(request):
    allprods=[]
    catprods=product.objects.values('category')
    cats={item['category'] for item in catprods}

    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        slides=n//4+math.ceil(n/4-n//4)
        allprods.append([prod,range(1,slides),slides])
    params={'allprods':allprods,'active_tab':'home'}
    return render(request,'shop/index.html',params)

def matchSearch(query,item):
    if(query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower()):
        return True
    else:
        return False

def search(request):
    allprods=[]
    query=request.POST.get('search')
    catprods=product.objects.values('category')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=product.objects.filter(category=cat)
        prod=[item for item in prodtemp if matchSearch(query,item)]
        n=len(prod)
        slides=n//4+math.ceil(n/4-n//4)
        if(len(prod)!=0):
            allprods.append([prod,range(1,slides),slides])
    if(len(allprods)==0 or len(query)<4):
        params={'msg':'Please enter relevent search query'}
    else:
        params={'allprods':allprods,'msg':''}
    return render(request,'shop/search.html',params)

def about(request):
    return render(request,'shop/about.html',{'active_tab':'about'})

def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        con=contact(name=name,email=email,query=query)
        con.save()
        temp=True
        return render(request,'shop/contact.html',{'temp':temp,'active_tab':'contact'})

    return render(request,'shop/contact.html',{'active_tab':'contact'})

def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid')
        email=request.POST.get('email')
        try:
            ord=order.objects.filter(order_id=orderid,email=email)
            if(len(ord)>0):
                update=updateorder.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps({'status':'success','updates':updates,'itemjson':ord[0].itemsjson},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse({'status':'noitem'})
        except Exception as e:
            return HttpResponse({'status':'error'})
    return render(request,'shop/tracker.html',{'active_tab':'tracker'})

def productview(request,myid):
    productss=product.objects.filter(id=myid)
    return render(request,'shop/prodview.html',{'product':productss[0]})

def checkout(request):
    return render(request,'shop/checkout.html')

def buyproduct(request):
    if request.method=="POST":
        itemsjson=request.POST.get("itemsjson","")
        name=request.POST.get("name","")
        amount=request.POST.get("amount","")
        email=request.POST.get("email","")
        address=request.POST.get("address1","")+" "+request.POST.get("address2","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zipcode=request.POST.get("zipcode","")
        phone=request.POST.get("phone","")
        ord=order(itemsjson=itemsjson,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,phone=phone,amount=amount)
        ord.save()
        update=updateorder(order_id=ord.order_id,update_desc='Your order has been placed')
        update.save()
        order_id=ord.order_id
        order_currency='INR'

    client=razorpay.Client(auth=('rzp_test_mLZnn2lKgLr1ZV','DI9eJtgM893xgmyVUWy1o2bR'))
    payment=client.order.create({'amount':int(amount)*100,'currency':order_currency,'payment_capture':'1'})

    return render(request,'shop/buyproduct.html',{'id':order_id,'payment':payment})

@csrf_exempt
def success(request):
    return render(request,'shop/payment-success.html')
    
    

