from itertools import product
from locale import currency
from django.http import JsonResponse
from rest_framework.decorators import api_view
from chatbot.models import Contacts, Messages, Products
from django.http import HttpResponse
from datetime import datetime
from . commerce_bot import commcerce_bot

url1= "https://13.234.238.141:9090"
admin_password = "Khairnar@123"

@api_view(['POST'])
def webhook(request):
    if request.method == 'GET':
        return JsonResponse({"error": "GET method not allowed"})

    if request.method == 'POST':
        print("IN Webhook Post")
        data = request.data
        print(data)
       
        
        
        if "messages" in data:
            contact = data["contacts"][0]
            mess = data["messages"][0]
            wa_id = contact["wa_id"]
            try:
                cont_inst = Contacts.objects.create(
                    wa_id=wa_id,
                    wa_name=contact["profile"]["name"],
                    flow="home"


                )
            except Exception as e:
                cont_inst = Contacts.objects.get(wa_id=wa_id)
            msg_time = int(mess["timestamp"])
            msg_time = datetime.fromtimestamp(msg_time)
            try:
                if mess["type"] == "text":
                    msg = Messages.objects.create(
                        wa_id=wa_id,
                        msg_id=mess["id"],
                        msg=mess["text"]["body"],
                        timestamp=msg_time,
                        msg_type=mess["type"]
                    )
                elif mess["type"] == "interactive":
                    if "button_reply" in mess["interactive"]:
                        interactive_msg = mess["interactive"]["button_reply"]["title"]
                        interactive_id = mess["interactive"]["button_reply"]["id"]
                    elif "list_reply" in mess["interactive"]:
                        interactive_msg = mess["interactive"]["list_reply"]["title"]
                        interactive_id = mess["interactive"]["list_reply"]["id"]
                                            
                    msg = Messages.objects.create(
                        wa_id=wa_id,
                        msg_id=mess["id"],
                        timestamp=msg_time,
                        msg_type=mess["type"],
                        msg=interactive_msg,
                        interactive_id=interactive_id
                    )
                elif mess["type"] == "order":
                    print("Start")
                    frm = mess["from"]
                    id = mess["id"]
                    order = mess["order"]
                    catalog_id = order["catalog_id"]
                    print("88Start88")
                    product_items = mess["order"]["product_items"]
                    products = []
                    prices = []
                    
                    

                    msg = Messages.objects.create(
                        wa_id=wa_id,
                        msg_id=mess["id"],
                        catalog_id = catalog_id,
                        

                    
                   
                    )
       
                     #inside
                    for i in product_items:
                        ######## Product Retailer ID ############
                        product = i["product_retailer_id"]
                        
                        ####### Price ######################
                        price = i["item_price"]
                          
                        ######quantity######
                        quantityy = i["quantity"] 
                        
                        itemprice = i["item_price"]
                        currency = i["currency"]
                        print(product_items)
                        
                        pro = Products.objects.create(
                        order_id = msg,
                        product_idd = product,
                        product_quantity = quantityy,
                        catalog_idd = catalog_id,
                        item_pricee = itemprice,
                        currency = currency
                        
                        
            
                        
                        
                        
                    )
                        
                    
                        




            except Exception as e:
                print(e)
            try:

                ca = commcerce_bot(cont_inst, msg)
                ca.check_and_send()
                pass
            except Exception as e:
                print(e)
        return JsonResponse({"success": "Cool"}, status=200)