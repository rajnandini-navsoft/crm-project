# from django.shortcuts import render
import json
from unicodedata import category
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response


class CustomerCreate(generics.CreateAPIView):
    def post(self,request,format=None):
        data=request.data
        serializer=CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
  


class CustomerList(generics.ListAPIView):
    def get(self,request, format=None):
        print("hlllll")
        query=CustomerAdd.objects.all()
        return_array=[]
        for each_customer in query:
            each_array={
                "id":each_customer.id,
                "first_name": each_customer.first_name,
                "middle_name": each_customer.middle_name,
                "last_name": each_customer.last_name,
                "mobile": each_customer.mobile,
                "email": each_customer.email,
                "address": each_customer.address
            }
            return_array.append(each_array)
        return Response(return_array)



class CustomerSingle(generics.ListAPIView):
    def get(self,request,pk):
        query=CustomerAdd.objects.filter(id=pk).first()
        if query:
            return_array={
                "id":query.id,
                "first_name": query.first_name,
                "middle_name": query.middle_name,
                "last_name": query.last_name,
                "mobile": query.mobile,
                "email": query.email,
                "address": query.address
            }
        else:
            return_array={}
        return Response(return_array)

    
    

# class CustomerDetail(generics.RetrieveAPIView):
#     # API endpoint that returns a single customer by pk.
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

class CustomerUpdate(generics.UpdateAPIView):
    def put(self,request,pk,format=None):
        data = request.data
        first_name=data["first_name"]
        middle_name=data["middle_name"]
        last_name=data["last_name"]
        mobile=data["mobile"]
        email=data["email"]
        address=data["address"]
        CustomerAdd.objects.filter(id=pk).update(first_name=first_name,middle_name=middle_name,last_name=last_name,mobile=mobile,email=email,address=address)
        query = CustomerAdd.objects.filter(id=pk).values("first_name","middle_name","last_name","mobile","email","address").first()
        return_arr={
            'msg':"Updated Succesfully",
            "data":query

        }
        return Response(return_arr)

class CategoryInsert(generics.CreateAPIView):
    def post(self,request,format=None):
        data=request.data
        name = data['name']
        slug = data['slug']
        image = data['image']
        description =data['description']
        featured = data['featured']
        active =data['active']
        created = data['created']
        modified = data['modified']
        abc=Category.objects.create(name=name,slug=slug,image=image,description=description,featured=featured,active=active,created=created,modified=modified)
        query = Category.objects.filter(id=abc.id).values("name","slug","image","description","featured","active","created","modified").first()
        return_arr={
            'msg':'Category added successfully',
            'data': query
        }
        return Response(return_arr)

class ProductInsert(generics.CreateAPIView):
    def post(self,request,format=None):
        data=request.data
        name = data['name']
        slug = data['slug']
        image =data['image']
        brand =data['brand']
        shipping = data['shipping']
        description=data['description']
        price=data['price']
        category=data['category']
        featured = data['featured']
        active = data['active']
        created =data['created']
        modified =data['modified']
        query=Product.objects.create(name=name,slug=slug,image=image,brand=brand,shipping=shipping,description=description,price=price,category=category,featured=featured,active=active,created=created,modified=modified)
        return_arr={
            'msg':'Data Inserted Successfully',
            'data':query
        }
        return Response(return_arr)


class ProductUpdate(generics.UpdateAPIView):
    def put(self,request,pk,format=None):
        data=request.data
        name = data['name']
        slug = data['slug']
        image =data['image']
        brand =data['brand']
        shipping = data['shipping']
        description=data['description']
        price=data['price']
        category=data['category']
        featured = data['featured']
        active = data['active']
        created =data['created']
        modified =data['modified']
        query=Product.objects.filter(id=pk).update(name=name,slug=slug,image=image,brand=brand,shipping=shipping,description=description,price=price,category=category,featured=featured,active=active,created=created,modified=modified)
        return_arr={
            'msg':"Data Updated Successfully",
            'data':query
        }
        return Response(return_arr)

        



# class CustomerDelete(generics.RetrieveDestroyAPIView):
#     # API endpoint that allows a customer record to be deleted.
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer