from django.core.exceptions import PermissionDenied
from assignment.backend.bl.user import check_user_exist
from django.contrib.sessions.models import Session
from django.shortcuts import redirect
# from simple_decorators.apps.models import Entry


USERS_TABLE = "user"

def authenticated(function):	
	def wrap(request, *args, **kwargs):
		print(request.headers)
		if request.COOKIES.get("sessionid"):
			print("session id is " + request.COOKIES.get("sessionid"))
			session = Session.objects.get(session_key=request.COOKIES.get("sessionid")).get_decoded()
			id = session.get("email",0)
			print(str(id) + " this is id")
			if check_user_exist(id):
				return function(request, *args, **kwargs)
			else:
				return redirect('/login')
				# raise PermissionDenied
		else:
			print("header not present")
			return redirect('/login')
			# raise PermissionDenied
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap




# def check_user_exist(id):
# 	print(id)
# 	query = "select count(*) as cnt from {} where (email = '{}') ".format(USERS_TABLE,id,id,id)
# 	print(query)
# 	result = execute_query(query)
# 	print(result)
# 	if result["status"] and result["query_results"][0]["cnt"] !=0:
# 		return True
# 	else:
# 		return False