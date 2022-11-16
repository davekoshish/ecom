from ast import Try
import json
from urllib import request
from webbrowser import get
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="xp56m82yjmbvnz29",
        public_key="565m7gqysn9kxcv5",
        private_key="07c58e1bcf21ab0959e66bd7a52d6161"
    )
)

def validate_user_id(id,token):
    UserModel=get_user_model()

    try:
        user=UserModel.objects.all(pk=id)
        if user.session_token==token:
            return True
        return False
    except:
        if UserModel.DoesNotExist:
            return False

@csrf_exempt
def generate_token(request,id,token):
    if not validate_user_id(id,token):
        return JsonResponse({"error":"user not found"})
    return JsonResponse({
        'token': gateway.client_token.generate(),
        'sucess':True

    })

@csrf_exempt
def process_payment(resquest,id,token):
    if not validate_user_id(id,token):
        return JsonResponse({"error":"user not found"})
    

    nonce_from_the_client=request.POST["paymentMethodNonce"]
    amount_from_the_client=request.POST["amount"]

    result=gateway.transaction.sale(
        {
            "amount":amount_from_the_client,
            "payment_method_nonce":nonce_from_the_client,
            "options":{
                "submit_for_settlement":True
            }
        }
    )

    if result.is_success:
        return JsonResponse({
            "success":result.is_success,
            "trasaction":{
                'id':result.transaction.id,'amount':result.transaction.amount
            }
        })

    else:
        return JsonResponse({'error':True,'sucess':False})