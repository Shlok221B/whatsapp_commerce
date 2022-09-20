from email import message
from logging import exception
from datetime import datetime
import requests, json
from . models import MasterProducts, product


#Birdvision
# ip = "https://13.233.94.160:9090"
# password = "Khairnar@123"
# base64_authentic = "YWRtaW46S2hhaXJuYXJAMTIz"

#Shopify
ip = "https://13.234.238.141:9090"
password = "Khairnar@123"
base64_authentic = "YWRtaW46S2hhaXJuYXJAMTIz"



class commcerce_bot:

    def __init__(self,cont_inst,msg_inst,data):
        self.cont_inst = cont_inst
        self.msg_inst = msg_inst
        self.data = data
        self.phone = cont_inst.wa_id

    def formatt(self):
        mess = self.data["messages"][0]
        formatted_msg = ":sparkles: We have added the following to your cart.\n"
        cart_total = 0
        if  mess["type"] == "order":
            product_items = mess["order"]["product_items"]
            for i in product_items:
                ######## Product Retailer ID ############
                product = i["product_retailer_id"] 
                ####### Price ######################
                price = i["item_price"]          
                ######quantity######
                quantityy = i["quantity"] 
                get_product_name = MasterProducts.objects.get(product_id=product)
                total_price = quantityy*get_product_name.price
                cart_total = cart_total + int(total_price)
                formatted_msg = formatted_msg + "\n" + "👉 " + str(quantityy) + " units of " + str(get_product_name.product_name) + " Total = " + str(total_price)
                formatted_msg = formatted_msg + "\n\n*Cart Total = *" + str(cart_total)
            print(formatted_msg)
            return str(formatted_msg)
        return ""
            

    def update_authkey(self):
        print("in auth")
        try:
            url = ip + "/v1/users/login"
            payload = {"new_password": password}
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Basic ' + base64_authentic
                        }
            response = requests.request("POST",url, headers=headers, data= json.dumps(payload), verify=False)
            rs = response.text
            json_data = json.loads(rs)
            jwt_token = json_data["users"][0]["token"]
            return jwt_token
        except exception as e:
            print("e")
            print("error in update authkey")
            return str(e)


    def send_message(self,msg):
        print("in send message")
        phone = self.msg_inst.wa_id
        text = self.msg_inst.msg
        name = self.cont_inst.name
        email = self.cont_inst.email
        address = self.cont_inst.address
        pincode = self.cont_inst.pincode 
        
        replies = {

            'greetings': {"to": phone,"recipient_type": "individual","type": "interactive","interactive": {"type": "button","body": {"text": "Hello User\n Welcome to Infinity Boom 😊.\n*What would you like to do ?*\n\n"},"action": {"buttons": [{"type": "reply","reply": {"id": "<ID 1.1>","title": "Shop Now"}},{"type": "reply","reply": {"id": "<ID 1.2>","title": "Track Order"}},{"type": "reply","reply": {"id": "<ID 1.3>","title": "Have a query?"}}]}}},
            'products' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "list","body": {"text": "*Please select from a category from below*\n\n*Select1* 👉 Ring\n*Select2* 👉 Necklace\n*Select3* 👉 Pendant\n*Select4* 👉 Earring\n\n👉 Type #️⃣ for main menu.\n\n⚡ Please select an option from below 👇"},"action": {"button": "Check Categoires","sections": [{"title": "Categories","rows": [{"id": "<ID 1.1>","title": "Ring"},{"id": "<ID 1.2>","title": "Necklace"},{"id": "<ID 1.3>","title": "Pendant"},{"id": "<ID 1.4>","title": "Earring"}]}]}}},
            #products
            'earrings' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "theinfinityboom"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "https://theinfinityboom.myshopify.com/collections/earring"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Earrings","product_items": [{"product_retailer_id": "41914695090355"},{"product_retailer_id": "41914692436147"}]}]}}},
            'pendants' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "Products"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Pendant","product_items": [{"product_retailer_id": "41914686341299"},{"product_retailer_id": "41914711081139"},{"product_retailer_id": "41883915976883"},{"product_retailer_id": "41914688471219"},{"product_retailer_id": "41914705477811"},{"product_retailer_id": "41883929346227"}]}]}}},
            'necklaces': {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "theinfinityboom"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Necklace","product_items": [{"product_retailer_id": "41914703511731"},{"product_retailer_id": "41914699579571"},{"product_retailer_id": "41914689913011"}]}]}}},
            'rings' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "theinfinityboom"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Rings","product_items": [{"product_retailer_id": "41914682474675"},{"product_retailer_id": "41883923644595"},{"product_retailer_id": "2123123"},{"product_retailer_id": "41883919745203"},{"product_retailer_id": "41914696892595"},{"product_retailer_id": "41883930886323"}]}]}}},

            'final' : {"to": phone,"type": "text","recipient_type": "individual","text": {"body": "Please Confirm your details\n\n" "Name:"+name+"\nEmail:"+email+"\nAddress:"+address+"\nPincode:"+pincode}},
            'name' : {"to": phone,"type": "text","recipient_type": "individual","text": {"body": "Please provide your name\n\n eg Jhon Doe"}},
            'email' : {"to": phone,"type": "text",  "recipient_type": "individual","text": {"body": "Please provide your email id ✉"}},
            'confirm' : {"to": phone,"recipient_type": "individual","type": "interactive","interactive": {"type": "button","body": {"text": self.formatt()},"footer": {"text": "Choose an option by clicking on any button below:"},"action": {"buttons": [{"type": "reply","reply": {"id": "Button 1 Text","title": "Proceed to checkout"}},{"type": "reply","reply": {"id": "Button 2 Text","title": "Exit"}}]}}},
            'pincode' : {"to": phone,"type": "text","recipient_type": "individual","text": {"body": "Please enter your pincode"}},
            'address' : {"to": phone,"type": "text","recipient_type": "individual","text": {"body": "Please enter your Shiping Address :round_drawing_pin:\n\n(House no. ,Street, Locality, City, State"}},
            'help' : {"to": phone,"recipient_type": "individual","type": "interactive","interactive": {"type": "button","header": {"type": "text","text": "Help"},"body": {"text": "For more information visit us at www.infinityboom.com\nContact us at 919762330859."},"action": {"buttons": [{"type": "reply","reply": {"id": "<Button 1>","title": "Exit"}}]}}}
            }
                ################################ AUTHKEY FUNCTION ########################
        url = ip + "/v1/messages"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.update_authkey()
        }
        payload = json.dumps(replies[msg])
        response = requests.post(
            url=url.rstrip(), data=payload, headers=headers, verify=False)
        rs = json.loads(response.text)
        print(rs)

        ################################ CHECK AND SEND ####################

    def check_and_send(self):
        print("check and send")
        cont = self.cont_inst
        msg_inst = self.msg_inst
        greetings = ("hi",)
        text = self.msg_inst.msg
        msg_type = msg_inst.msg_type
        interactive_id = self.msg_inst.interactive_id
        print(text)
        

        if text.lower() in greetings:
            self.send_message("greetings")
            self.cont_inst.flow = "home/grt"
            self.cont_inst.save()
            return None
            
        
        ########## Main Menu #############
        if cont.flow == "home/grt" and msg_inst.msg_type == "interactive":
            if self.msg_inst.interactive_id == "<ID 1.1>":
                self.send_message("products")
                self.cont_inst.flow = "home/grt/products"
            elif self.msg_inst.interactive_id == "<ID 1.2>":
                self.send_message("confirm")
                self.cont_inst.flow = "home/grt/track"
            elif self.msg_inst.interactive_id == "<ID 1.3>":
                self.send_message("help")
                self.cont_inst.flow = "home/grt/help"
            self.cont_inst.save()
            return None


        ########### Products Menu ################
        if cont.flow == "home/grt/products" and msg_inst.msg_type == "interactive":
            if self.msg_inst.interactive_id == "<ID 1.1>":
                self.send_message("rings")
                self.cont_inst.flow = "home/grt/products"
            elif self.msg_inst.interactive_id == "<ID 1.2>":
                self.send_message("necklaces")
                self.cont_inst.flow = "home/grt/products"
            elif self.msg_inst.interactive_id == "<ID 1.3>":
                self.send_message("pendants")
                self.cont_inst.flow = "home/grt/products"
            elif self.msg_inst.interactive_id == "<ID 1.4>":
                self.send_message("earrings")
                self.cont_inst.flow = "home/grt/products"
            self.cont_inst.save()
            return None
        if cont.flow == "home/grt/products" and msg_inst.msg_type == "text":
            self.send_message("greetings")
            self.cont_inst.flow = "home/grt" 
            self.cont_inst.save()
            return None


        if cont.flow == "home/grt/products" and msg_inst.msg_type == "order":
            self.send_message("confirm")
            self.cont_inst.flow = "confirm"
            self.cont_inst.save()
            return None


        if cont.flow == "confirm" and msg_inst.msg_type == "interactive":
            if self.msg_inst.interactive_id == "Button 1 Text":
                self.send_message("pincode")
                self.cont_inst.flow = "confirm/pincode"
            elif self.msg_inst.interactive_id == "Button 2 Text":
                self.send_message("products")
                self.cont_inst.flow = "home/grt/products"
            self.cont_inst.save()
            return None

        if cont.flow == "confirm/pincode" and msg_inst.msg_type == "text":
            self.cont_inst.pincode = text
            self.send_message("address")
            self.cont_inst.flow = "confirm/pincode/address" 
            self.cont_inst.save()
            return None

        if cont.flow == "confirm/pincode/address" and msg_inst.msg_type == "text":
            self.cont_inst.address = text
            self.send_message("email")
            self.cont_inst.flow = "confirm/pincode/address/email" 
            self.cont_inst.save()
            return None 
        
        if cont.flow == "confirm/pincode/address/email" and msg_inst.msg_type == "text":
            self.cont_inst.email = text
            self.send_message("name")
            self.cont_inst.flow = "confirm/pincode/address/email" 
            self.cont_inst.save()
            return None 

        if cont.flow == "confirm/pincode/address/email/name" and msg_inst.msg_type == "text":
            self.cont_inst.name = text
            self.send_message("final")
            self.cont_inst.flow = "confirm/final" 
            self.cont_inst.save()
            return None 