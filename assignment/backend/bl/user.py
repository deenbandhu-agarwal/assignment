from assignment.backend.utilities.db_utilities import execute_query, execute_update_query
from datetime import datetime
from django.conf import settings
from django.contrib.sessions.models import Session


USER_TABLE = "user"

def singup_user(name,dob,email,password,school,grade,board):
	query = """insert into {}(name,dob,email,password,school,grade,board) values
	('{}','{}','{}',MD5('{}'),'{}',{},'{}')""".format(USER_TABLE,name,dob,email,password,school,grade,board)
	print(query)
	return execute_update_query(query)


def login_user(username,password):
	print(username)
	query = """select email from {} where email = '{}' 
	and password = MD5('{}')""".format(USER_TABLE,username,password)
	print(query)
	result = execute_query(query)
	if not result["status"]:
		return result
	if len(result["query_results"]) == 0:
		result = {}
		result["status"] = False
		result["error_message"] = "user don't exist"
		return result
	return result



def check_user_exist(email):
	query = """select count(*) as cnt from {USER_TABLE} 
	where email = '{email}'""".format(USER_TABLE = USER_TABLE,email= email)
	result = execute_query(query)
	if result["status"] and result["query_results"][0]["cnt"] !=0:
		return True
	else:
		return False	

def get_user_session(request):
	session = Session.objects.get(session_key=request.COOKIES.get("sessionid")).get_decoded()
	id = session.get("userid",0)
	return id	