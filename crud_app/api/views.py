
from .models import UserAccount
from .serializers import UserAccountSerializer
from .models import ProductItem
from .serializers import ProductItemSerializer
from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core import validators


# Products

# GET PRODUCTS
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_products(request):
    products = ProductItem.objects.all()
    serializer = ProductItemSerializer(products, many=True)
    return JsonResponse({'products': serializer.data}, safe=False, status=status.HTTP_200_OK)

# GET PRODUCT by ID
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_product(request, product_id):
    try:
        product = ProductItem.objects.get(id=product_id)
        serializer = ProductItemSerializer(product, many=False)
        return JsonResponse({'product': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ADD PRODUCT
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_product(request):

    try:
        product = ProductItem.objects.create(
            name=request.data['name'],
            title=request.data['title'],
            price=request.data['price'],
            image=request.data['image']
        )
        serializer = ProductItemSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'Product': request.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# UPDATE PRODUCT
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_product(request, product_id):

    try:
        product_item = ProductItem.objects.filter(id=product_id)
        product_item.update(
            name=request.data['name'],
            title=request.data['title'],
            price=request.data['price'],
            image=request.data['image']
        )
        product = ProductItem.objects.get(id=product_id)
        serializer = ProductItemSerializer(data=product)
        if serializer.is_valid():
            serializer.save()

        return JsonResponse({'Product': request.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# DELETE PRODUCT
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):
    try:
        product = ProductItem.objects.get(id=product_id)
        product.delete()
        return JsonResponse({'Deleted': request.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Users

# GET USERS
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_users(request):
    users = UserAccount.objects.all()
    serializer = UserAccountSerializer(users, many=True)
    return JsonResponse({'user accounts': serializer.data}, safe=False, status=status.HTTP_200_OK)

# GET USER by ID
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    try:
        user = UserAccount.objects.get(id=user_id)
        serializer = UserAccountSerializer(user, many=False)
        return JsonResponse({'user account': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ADD USER
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_user(request):

    name = request.data['name']
    email = request.data["email"]
    try:
        validators.validate_email(email)
        if len(name) < 5:
            raise ValidationError("name is too short")
        user = UserAccount.objects.create(
            name=request.data['name'],
            email=request.data["email"]
        )
        serializer = UserAccountSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'user': request.data}, safe=False, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# UPDATE USER
@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_user(request, user_id):

    name = request.data['name']
    email = request.data["email"]

    try:
        if len(name) < 5:
            raise ValidationError("name is too short")
        validators.validate_email(email)
        user_account = UserAccount.objects.filter(id=user_id)
        user_account.update(
            name=request.data['name'],
            email=request.data['email']
        )
        user = UserAccount.objects.get(id=user_id)
        serializer = UserAccountSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'user': request.data}, safe=False, status=status.HTTP_200_OK)
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# DELETE USER
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    try:
        user = UserAccount.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'deleted': request.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
