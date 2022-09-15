from email import message
from logging import exception
from datetime import datetime
import requests, json

#Birdvision
# ip = "https://13.233.94.160:9090"
# password = "Khairnar@123"
# base64_authentic = "YWRtaW46S2hhaXJuYXJAMTIz"

#Shopify
ip = "https://13.234.238.141:9090"
password = "Khairnar@123"
base64_authentic = "YWRtaW46S2hhaXJuYXJAMTIz"


class commcerce_bot:

    def __init__(self,cont_inst,msg_inst):
        self.cont_inst = cont_inst
        self.msg_inst = msg_inst
        self.phone = cont_inst.wa_id

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
        replies = {

            'greetings': {"to": phone,"recipient_type": "individual","type": "interactive","interactive": {"type": "button","body": {"text": "Hello User\n Welcome to Infinity Boom 😊.\n*What would you like to do ?*"},"action": {"buttons": [{"type": "reply","reply": {"id": "<ID 1.1>","title": "Shop Now"}},{"type": "reply","reply": {"id": "<ID 1.2>","title": "Track Order"}},{"type": "reply","reply": {"id": "<ID 1.3>","title": "Have a query?"}}]}}},
            'products' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "list","body": {"text": "*Please select from a category from below*\n\n*Select1* 👉 Ring\n*Select2* 👉 Necklace\n*Select3* 👉 Pendant\n*Select4* 👉 Earring\n\n👉 Type #️⃣ for main menu.\n\n⚡ Please select an option from below 👇"},"action": {"button": "Check Categoires","sections": [{"title": "Categories","rows": [{"id": "<ID 1.1>","title": "Ring"},{"id": "<ID 1.2>","title": "Necklace"},{"id": "<ID 1.3>","title": "Pendant"},{"id": "<ID 1.4>","title": "Earring"}]}]}}},
            #products
            'earrings' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "theinfinityboom"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Earrings","product_items": [{"product_retailer_id": "41914695090355"},{"product_retailer_id": "41914692436147"}]}]}}},
            'pendants' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "Products"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Pendant","product_items": [{"product_retailer_id": "41914686341299"},{"product_retailer_id": "41914711081139"},{"product_retailer_id": "41883915976883"},{"product_retailer_id": "41914688471219"},{"product_retailer_id": "41914705477811"},{"product_retailer_id": "41883929346227"}]}]}}},
            'necklaces': {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "theinfinityboom"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Necklace","product_items": [{"product_retailer_id": "41914703511731"},{"product_retailer_id": "41914699579571"},{"product_retailer_id": "41914689913011"}]}]}}},
            'rings' : {"recipient_type": "individual","to": phone,"type": "interactive","interactive": {"type": "product_list","header": {"type": "text","text": "theinfinityboom"},"body": {"text": "Shop Latest Varities"},"footer": {"text": "click to view"},"action": {"catalog_id": "816282966199042","sections": [{"title": "Rings","product_items": [{"product_retailer_id": "41914682474675"},{"product_retailer_id": "41883923644595"},{"product_retailer_id": "2123123"},{"product_retailer_id": "41883919745203"},{"product_retailer_id": "41914696892595"},{"product_retailer_id": "41883930886323"}]}]}}},

            'pincode' : {"to": phone,"type": "text","recipient_type": "individual","text": {"body": "Please enter your pincode"}},
            'address' : {"to": phone,"type": "text","recipient_type": "individual","text": {"body": "Please enter your address 📍"}}
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
        greetings = ("hi")
        text = self.msg_inst.msg
        msg_type = msg_inst.msg_type
        interactive_id = self.msg_inst.interactive_id
        print(text)

        if text.lower() in greetings:
            self.send_message("greetings")
            self.cont_inst.flow = "home/grt/name"
            self.cont_inst.save()
            return None
        
        