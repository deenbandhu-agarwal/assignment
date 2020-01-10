from assignment.backend.utilities.db_utilities import execute_query, execute_update_query
from datetime import datetime
from django.conf import settings
from django.contrib.sessions.models import Session

CLASS_TABLE = "class"
QUESTION_TABLE = "question"
USER_CLASS_TABLE = "user_class"

def get_class_data(user):
	query = """select uc.class,c.name as class_name,question_content from {USER_CLASS_TABLE} 
	uc join {CLASS_TABLE} c on uc.class = c.id join {QUESTION_TABLE} q on c.id = q.class
	where user = {user};""".format(USER_CLASS_TABLE = USER_CLASS_TABLE,CLASS_TABLE = CLASS_TABLE,
		user = user,QUESTION_TABLE = QUESTION_TABLE)
	results = execute_query(query)
	print(results)
	class_data = {}
	for row in results["query_results"]:
		if not class_data.get(row["class_name"],0):
			class_data[row["class_name"]]	 = []
		class_data[row["class_name"]].append(row["question_content"])
	
	classes = []
	for k in class_data.keys():
		class_object = {}
		class_object['class_name'] = k
		class_object['questions'] = class_data[k]
		classes.append(class_object)
	print(classes)
	return classes

