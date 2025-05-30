import requests
from decouple import config
import constants.defs as defs 

class OandaApi:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {config("API_KEY")}",
            "Content-Type": "application/json"
        })

    def make_request(self, url, verb="get", code=200, params=None, data=None, headers=None):
        full_url = f"{config("OANDA_URL")}/{url}"
        try:
            response = None 
            if verb == "get":
                response = self.session.get(full_url, params=params, data=data, headers=headers)
            
            if response == None:
                return False, {"error": "verb not found"}
            
            if response.status_code == code:
                return True, response.json()
            else:
                return False, response.json()
            
        except Exception as error:
             return False, {"Exception": error}
        
    def get_accont_endpoint(self, ep, data_key):
        url = f"accounts/{config("ACCOUNT_ID")}/{ep}"
        ok, data = self.make_request(url)
        if ok == True and data_key in data:
            return data[data_key]
        else:
            print("ERROR get_account_endpoint()", data)
            return None 
    
    def get_account_summary(self):
        return self.get_accont_endpoint("summary", "account")
    
    def get_account_instruments(self):
        return self.get_accont_endpoint("instruments", "instruments")
    
    
