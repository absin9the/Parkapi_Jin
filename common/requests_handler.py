import requests
class RequestsHandler:
    def __init__(self):
        """session manager"""
        self.session = requests.session()
    def visit(self, method, url, params = None, data= None, json= None, headers= None):
        result = self.session.request(method,url,params=params,data=data,json=json,headers=headers)
        try:
            # return json result
            print(result)
            return result.json()
        except Exception:
            return 'not json'
    def close_session(self):
        self.session.close()