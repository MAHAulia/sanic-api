from sanic import Blueprint
from sanic.response import json, text

from app.utility.jsonapi import response

authController = Blueprint('auth')


@authController.get("/auth")
def auth(request):
  return json(response(status=200, size=1, message="Success", data=[], rc='00'))

@authController.get("/login")
def login(request):
  return json(response(status=200, size=1, message="Success", data=[], rc='00'))