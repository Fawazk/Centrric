import json
from urllib import response

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase,APIClient

from ..models import Account, UserFollow
from ..serializers import (UserDetailsSerializer, UserFollowSerializer,
                           UserSerializer)


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('Register')
        self.login_url = reverse('token_obtain_pair')
        self.follow_url = reverse('follow')
        self.getfollowing_url = reverse('getfollowing')
        self.getfollowers_url = reverse('getfollowers')
        self.unfollow_url = reverse('unfollow',kwargs={"uid":1})
        self.userdetails_url = reverse('userdetails')
        self.token={
            'access':'',
            'refresh':'',
        }
        self.user_register_data = {"full_name": 'fawazK',
                    "email": 'fawazK@gmail.com',
                    "phone_number": 7777777777,
                    "place": 'kochi',
                    "date_of_birth": '2022-01-01',
                    "password":'1234',
                }

        return super().setUp()
