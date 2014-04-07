DEBUG = True
try:        
    import json
    if DEBUG:
        grade_result['correct'] = False
        grade_result['comment'] = executor_result
    else:
        from_submit_code = eval(executor_result['stdout'])
        grade_result['correct'] = from_submit_code['is_correct']
        comment_list = from_submit_code['comment_list']
        comment_string = ''
        for comment in comment_list:
            comment_string += str(comment) + '\n'
        grade_result['comment'] = comment_string
except Exception as e:
    if DEBUG:
        grade_result['comment'] = str(e)
        grade_result['correct'] = False
    else:
        grade_result['correct'] = False
        grade_result['comment'] = ("There was an error while grading your code. "
        "This may be our fault. If you'd like, you may email your code to "
        "support@udacity and let us know there's a problem.")


#try:
#   import json
#   from_submit_code = json.loads(executor_result['stdout'])
#   grade_result['correct'] = from_submit_code['is_correct']
#   comment_list = from_submit_code['comment_list']
#   comment_string = ''
#   for comment in comment_list:
#       comment_string += str(comment) + '\n'
#   grade_result['comment'] = comment_string
#except:
#   grade_result['correct'] = False
#   grade_result['comment'] = "There was an error while grading your code. \
#This may be our fault. If you'd like, you may email your code to \
#support@udacity and let us know there's a problem."
#	if DEBUG:
#        grade_result['comment'] = executor_result

# try:
# 	import json
# 	from_submit_code = json.loads(executor_result['stdout'])     
# 	grade_result['correct'] = from_submit_code['is_correct']
# 	result = executor_result['stdout']

# 	if len(executor_result['stderr']) > 0:
# 	    grade_result['comment'] = executor_result['stderr']
# 	    grade_result['correct'] = False
# 	else:
# 	    grade_result['comment'] = response
# 	    if result == "OK":
# 	        grade_result['correct'] = True
# 	    else:
# 	            grade_result['correct'] = False

