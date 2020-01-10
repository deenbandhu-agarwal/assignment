from django.shortcuts import render
from assignment.backend.decorator.authentication import authenticated
from assignment.backend.bl.user import *
from assignment.backend.bl.classbl import *
import json
from django.http import JsonResponse

# Create your views here.

@authenticated
def index(request):
	user = get_user_session(request)
	class_list = get_class_data(user)			
	return render(request, 'index.html', context={"class_list" : class_list})# Create your views here.


def sign_up(request):
	if request.method == 'GET':
		return render(request, 'Signup.html', context=None)# Create your views here.
	else:
		print(request.body)
		data = json.loads(request.body)
		results = singup_user(data["name"],data["dob"],data["email"],data["password"],data["school"],data["grade"],data["board"])
		return JsonResponse(results)# Create your views here.

	# json_data = json.loads(request.body)
	# print(json_data)
	# return JsonResponse(json_data)


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html', context=None)# Create your views here.
	else:
		print(request.body)
		json_data = json.loads(request.body)
		email = json_data["email"]
		password = json_data["password"]
		result = login_user(email,password)
		if result["status"]:
			request.session['email'] = result["query_results"][0]["email"]
			request.session.save()
			print(request.session.session_key)
			del result['query_results']
			result["message"] = "Logged in"
		return JsonResponse(result)


def sign_out(request):
	request.session.flush()
	return render(request, 'login.html', context=None)
# def login1(request):
	# result = login(id,password)
	# if result["status"]:
	# 	request.session['email'] = result["query_results"][0]["email"]
	# 	request.session.save()
	# 	print(request.session.session_key)
	# 	del result['query_results']
	# 	result["message"] = "Logged in"
	# return JsonResponse(result)