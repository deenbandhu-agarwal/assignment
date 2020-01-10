from django.db import connection
import logging
from django.conf import settings

# return list of rows (each row is a dictionary)
def execute_query(query):
	result = {}	
	logger = logging.getLogger(__name__)
	logger.info(query)
	print(query)
	try:
		with connection.cursor() as cursor:
			cursor.execute(query)
			columns = [col[0] for col in cursor.description]
			query_results =  [ dict(zip(columns, row)) for row in cursor.fetchall()]
			result["status"] = True
			result["query_results"] = query_results
	except:
		logger.error("Some issue is executing the query ", exc_info=True)
		result["status"] = False
		result["error_message"] = "Some Error Occured"
	return result



def execute_update_query(query):
	result = {}	
	logger = logging.getLogger(__name__)
	logger.info(query)
	print(query)	
	try:
		with connection.cursor() as cursor:
			cursor.execute(query)
			if cursor.rowcount > 0:
				result["status"] = True
	except:
		logger.error("Some issue is executing the query ", exc_info=True)
		result["status"] = False
		result["error_message"] = "Some Error Occured"	
	return result