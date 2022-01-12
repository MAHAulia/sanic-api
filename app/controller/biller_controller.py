from sanic import Blueprint
from sanic import response
from sanic.response import json, text

billerController = Blueprint('biller')

@billerController.get("/biller/inquiry")
def inquiry(request):
  return json(response(status=200, size=1, message="Success", data=[], rc='00'))

@billerController.get("/biller/payment")
def inquiry(request):
  return json(response(status=200, size=1, message="Success", data=[], rc='00'))

@billerController.get("/biller/advice")
def advice(request):
  return json(response(status=200, size=1, message="Success", data=[], rc='00'))