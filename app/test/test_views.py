from os import access
from urllib import response
from app.models import Account
from .test_setup import TestSetUp
from rest_framework.test import APIClient


accesstoken=''
class TestView(TestSetUp):
    def test_user_cannot_reigster_without_data(self):
        response=self.client.post(self.register_url)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code,400)
    
    def test_user_can_reigster_without_data(self):
        response=self.client.post(self.register_url,self.user_register_data,format='json')
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code,200)


    def test_user_can_login(self):
        regres=self.client.post(self.register_url,self.user_register_data,format='json')
        email= regres.data['email']
        
        login_data={
        'email':email,
        'password':regres.data['password']
        }
        res= self.client.post(self.login_url,login_data,format='json')
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,200)
        return 'Token '+res.data['access']

    def test_can_follow(self):
        accesstoken = self.test_user_can_login()
        print(accesstoken,'accesstokenaccesstokenaccesstokenaccesstoken')
        # { headers: { "Authorization": `Bearer  ${access}` } }
        res= self.client.post(self.follow_url,headers={'Authorization': accesstoken},)
        import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,200)

    # def test_can_getfollowing(self):
    #     accesstoken = self.test_user_can_login()
    #     self.client.credentials(HTTP_AUTHORIZATION="Token "+accesstoken)
    #     res= self.client.get(self.getfollowing_url)
    #     self.assertEqual(res.status_code,200)
    
    # def test_can_getfollowers(self):
    #     accesstoken = self.test_user_can_login()
    #     self.client.credentials(HTTP_AUTHORIZATION="Token "+accesstoken)
    #     res= self.client.get(self.getfollowers_url)
    #     self.assertEqual(res.status_code,200)
    
    # def test_unfollow(self):
    #     self.client.credentials(HTTP_AUTHORIZATION="Token "+accesstoken)
    #     res= self.client.delete(self.unfollow_url)
    #     self.assertEqual(res.status_code,200)

    # def test_can_get_user_details(self):
    #     accesstoken = self.test_user_can_login()
    #     self.client.credentials(HTTP_AUTHORIZATION="Token "+accesstoken)
    #     res= self.client.get(self.userdetails_url)
    #     self.assertEqual(res.status_code,200)
