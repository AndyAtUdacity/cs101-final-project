grade_result['comment'] = 'Stderr: \n\t' + executor_result['stderr'] + '\n Stdout: \n\t' + executor_result['stdout'] + '\n test_results: \n\t' +str(executor_result['test_results'])
#grade_result['comment'] = str(executor_result.keys())



grade_result['correct'] = True
grade_result['feedback'] = 'Passed.'

