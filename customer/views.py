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
        # print("hlllll")
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
        category_save=Category.objects.create(name=name,slug=slug,image=image,description=description,featured=featured,active=active,created=created,modified=modified)
        category_display = Category.objects.filter(id=category_save.id).values("name","slug","image","description","featured","active","created","modified").first()
        return_arr={
            'msg':'Category added successfully',
            'data': category_display
        }
        return Response(return_arr)

class CategoryUpdate(generics.UpdateAPIView):
    def put(self,request,pk,format=None):
        data=request.data
        name=data["name"]
        slug=data["slug"]
        image=data["image"]
        description=data["description"]
        featured=data["featured"]
        active=data["active"]
        # created=data["created"]

        Category.objects.filter(id=pk).values(name=name,slug=slug,image=image,description=description,featured=featured,active=active)
        category_update_display=Category.objects.flter(id=pk).values("name","slug","image","description","featured","active")

        return_arr={
            'msg':"Data Updated Successfully",
            'data':category_update_display
        }
        return Response(return_arr)



class ProductInsert(generics.CreateAPIView):
    def post(self,request,format=None):
        data=request.data
        name = data['name']
        slug = data['slug']
        image =data['image']
        brand =data['brand']
        url =data['url']
        shipping = data['shipping']
        description=data['description']
        price=data['price']
        category=data['category']
        featured = data['featured']
        active = data['active']
  
        product_save=Product.objects.create(name=name,slug=slug,image=image,brand=brand,url=url,shipping=shipping,description=description,price=price,category_id=category,featured=featured,active=active)
        product_display = Product.objects.filter(id=product_save.id).values("name","slug","image","brand","shipping","description","price","category","featured","active","created","modified").first()
        return_arr={
            'msg':'Data Inserted Successfully',
            'data':product_display
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
   
        #To update data
        Product.objects.filter(id=pk).update(name=name,slug=slug,image=image,brand=brand,shipping=shipping,description=description,price=price,category=category,featured=featured,active=active)
        #To display the updated data
        product_update_display = Product.objects.filter(id=pk).values("name","slug","image","brand","shipping","description","price","category","featured","active","created","modified").first()
        return_arr={
            'msg':"Data Updated Successfully",
            'data':product_update_display
        }
        return Response(return_arr)

        #-------------------DATA INSERT IN MULTIPLE TABLE AT ONCE-------------------------------
class MultiTabProCustInsert(generics.CreateAPIView):
    def post(self,request,format=None,):
        data=request.data
        # store=[]
        name = data['name']
        slug = data['slug']
        # image =data['image']
        brand =data['brand']
        url =data['url']
        shipping = data['shipping']
        description=data['description']
        price=data['price']
        category=data['category']
        featured = data['featured']
        active = data['active']

        first_name = data['first_name']
        middle_name = data["middle_name"]
        last_name = data["last_name"]
        mobile = data["mobile"]
        email = data["email"]
        address = data["address"]

        product_details=Product.objects.create(name=name,slug=slug,brand=brand,url=url,shipping=shipping,description=description,price=price,category_id=category,featured=featured,active=active)
        customer_details=CustomerAdd.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,mobile=mobile,email=email,address=address)
        product_insert_display=Product.objects.filter(id=product_details.id).values("name","slug","brand","url","shipping","description","price","category","featured","active").first()
        customer_insert_display=CustomerAdd.objects.filter(id=customer_details.id).values("first_name","middle_name","last_name","mobile","email","address").first()
        # store.append(product_insert_display)
        return_arr={
            "masg":"Both model data inserted successfully",
            "product_data":product_insert_display,
            "customer_data":customer_insert_display
            
        }
        return Response(return_arr)


class MultiDataFetch(generics.ListAPIView):
    def get(self,request,format=None):
        product_table_fetch=Product.objects.all()
        customer_table_fetch=CustomerAdd.objects.all()
        return_product_array=[]
        return_customer_array=[]

        for each_product in product_table_fetch:
            each_array={
                "name" : each_product.name,
                "slug" : each_product.slug,
                # image =each_product.image,
                "brand" :each_product.brand,
                "url" :each_product.url,
                "shipping" :each_product.shipping,
                "description":each_product.description,
                "price":each_product.price,
                "category":each_product.category_id,
                "featured" : each_product.featured,
                "active" : each_product.active
            }
            return_product_array.append(each_array)

            
                
            
        for each_customer in customer_table_fetch:
            each_cust_arr={
                "first_name":each_customer.first_name,
                "middle_name":each_customer.middle_name,
                "last_name":each_customer.last_name,
                'mobile':each_customer.mobile,
                "email":each_customer.email,
                "address":each_customer.address

,
            }
            return_customer_array.append(each_cust_arr)
        return_arr={
            "product_data":return_product_array,
            "customer_data":return_customer_array
        }
        return Response(return_arr)

            
        
    
        


        


        



# class CustomerDelete(generics.RetrieveDestroyAPIView):
#     # API endpoint that allows a customer record to be deleted.
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer