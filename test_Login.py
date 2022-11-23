import unittest
from common.requests_handler import RequestsHandler
class LoginTest(unittest.TestCase):
    def setUp(self):
        # request class instantiation
        self.req = RequestsHandler()

    def tearDown(self):
        self.req.close_session()

    def test_login_success(self):
        login_url = 'http://192.168.56.104:5000/login/'
        payload = {
            "username": "test1",
            "password": "1234567890"
        }
        res = self.req.visit('post', login_url, data=payload)
        self.assertEqual(200, res['code'])
    def test_get_summary(self):
        url='http://192.168.56.104:5000/api/park/summary'
        payload={}
        res=self.req.visit('post', url,data=payload)
        self.assertIn('rows',res)
    def test_get_avail(self):
        url='http://192.168.56.104:5000/api/park/avail'
        payload={}
        res=self.req.visit('post', url,data=payload)
        self.assertIn('rows',res)
    def test_get_use(self):
        url='http://192.168.56.104:5000/api/park/use'
        payload={}
        res=self.req.visit('post', url,data=payload)
        self.assertIn('rows',res)
    def test_park_release(self):
        url = 'http://192.168.56.104:5000/park/release'
        payload = {'id':1,'areacode1':'a01'}
        res = self.req.visit('post', url, data=payload)
        self.assertEqual(200, res['code'])
    def test_park_bus(self):
        url = 'http://192.168.56.104:5000/park/bus'
        payload = {'id':5,'ccode2':'100005','areacode2':'a01'}
        res = self.req.visit('post', url, data=payload)
        self.assertEqual(200, res['code'])
    def test_park_reload(self):
        url = 'http://192.168.56.104:5000/park/reload'
        payload = {'id':4,'ccode3':'100004','opcode3':'000004','npcode3':'000003','areacode3':'a01'}
        res = self.req.visit('post', url, data=payload)
        self.assertEqual(200, res['code'])

if __name__ == '__main__':
    unittest.main()