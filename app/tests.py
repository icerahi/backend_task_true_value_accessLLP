from django.test import TestCase
from rest_framework.test import APITestCase
from .models import User 
from rest_framework.reverse import reverse 
from rest_framework import status
from .test_data import data 

class UserAPITestCase(APITestCase):
    def setUp(self):
        for user in data:
            User.objects.create(
                first_name=user['first_name'],
                last_name=user['last_name'],
                company_name=user['company_name'],
                state=user['state'],
                zip=user['zip'],
                email=user['email'],
                web=user['web'],
                age=user['age']
                )
    
    def test_users(self):
        self.assertEqual(User.objects.count(),10)
        
    def test_users_list(self):
        users = self.client.get('/api/users/')
        page = self.client.get('/api/users/',{'page':1})
        limit = self.client.get('/api/users/',{'limit':10})
        search_by_name = self.client.get('/api/users/',{'name':'james'})
        sort = self.client.get('/api/users/',{'sort':'-age'})
        
        self.assertEqual(users.status_code,status.HTTP_200_OK)
        self.assertEqual(page.status_code,status.HTTP_200_OK)
        self.assertEqual(limit.status_code,status.HTTP_200_OK)
        self.assertEqual(search_by_name.status_code,status.HTTP_200_OK)
        self.assertEqual(sort.status_code,status.HTTP_200_OK)
        
    def test_user_create(self):
        data={
                "id": 2,
                "first_name": "Josephine",
                "last_name": "Darakjy",
                "company_name": "Chanay, Jeffrey A Esq",
                "city": "Brighton",
                "state": "MI",
                "zip": 48116,
                "email": "josephine_darakjy@darakjy.org",
                "web": "http://www.chanayjeffreyaesq.com",
                "age": 48
                }
        response=self.client.post('/api/users/',data,foramt="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_user_detail(self):
        response=self.client.get('/api/users/',kwargs={'pk':1})
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_user(self):
        
        data={"first_name": "Josephine","last_name": "Darakjy","age": 48}
        put_response = self.client.put('/api/users/1/',data,format='json')        
        self.assertEqual(put_response.status_code,status.HTTP_200_OK)
        put_response_data = put_response.data 
        self.assertEqual(put_response_data['first_name'],data['first_name'])
        
    def test_delete_user(self):
        response =self.client.get('/api/users/',kwargs={'pk':1})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        