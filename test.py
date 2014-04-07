from StringIO import StringIO
import sys
#import solution
import cs101_fp_solution_4 as solution # so I can use my solution to see if students are correct!

student_code_file = 'studentMain.py'
#student_code_file = 'solution.py'

DEBUG = False

# Checks to see if student defined function.
def function_check(f):
    """Used to see if student has defined function f."""
    if f is None:
        return False
    try:
        f
    except NameError:
        if DEBUG:
            print "function_check exception"
            raise
        return False
    # check if f is indeed a function
    if not hasattr(f, '__call__'):
        return False
    return True

def test(code_file):
    student_ns = {} # make a clean namespace
    f = open(code_file)
    code_string = f.read()
    exec(code_string, student_ns)

    global comment_list
    comment = ''
    is_correct = 'OK' # defaults to 'OK'. If I screw up the grading code, it 
                      # should be in the student's favor.

    try:
        create_data_structure = student_ns.get("create_data_structure")
        add_new_user = student_ns.get("add_new_user")
        add_connection = student_ns.get("add_connection")
        get_connections = student_ns.get("get_connections")
        get_secondary_connections = student_ns.get("get_secondary_connections")
        connections_in_common = student_ns.get("connections_in_common")
        path_to_friend = student_ns.get("path_to_friend")
        popularity_score = student_ns.get("popularity_score")
    except Exception as e:
        e = '\n' + str(e)
        e += '\nDid you change the name of one of the functions you were supposed to define?'
        comment += e 
        is_correct = "NO"
        return is_correct + comment

    s = solution.test_string_1
    try:
        stud_network = create_data_structure(s)
    except Exception as e:
        e = '\n' + str(e)
        comment += e
        if DEBUG:
            print "exception generating stud_network"
            raise
        is_correct = "NO"
        comment +='\nWe were unable to create a data structure using your ' + \
                  '\ncreate_data_structure procedure.'
        return is_correct + comment

    try:
        sol_network = solution.create_data_structure(s)
    except:
        if DEBUG:
            print "exception generating sol_network"
            raise
        is_correct = "NO"
        comment += "\nThere was an error during the grading. This may be " + \
                  "\nour fault though. If you'd like, you may email your " + \
                  "\ncode to support@udacity and let us know there's a problem."
        return is_correct + comment

    if not stud_network:
        if DEBUG:
            print 'no stud_network!'
        is_correct = "NO" 
        comment += '\nWe were unable to create a data structure using your ' + \
                  '\ncreate_data_structure procedure.'
        return is_correct + comment

    try:
        stud_out = get_connections(stud_network, 'A')
        stud_out = [name.lower() for name in stud_out]
    except Exception as e:
        e = '\n' + str(e)
        is_correct = "NO"
        comment += e
        comment += '\nWe tried calling your get_connections function with a ' + \
            '\nnetwork and a user name, but something went wrong.'
        return is_correct + comment

    try:
        sol_out = solution.get_connections(sol_network, 'A')
    except:
        is_correct = "NO"

        comment += "\nThere was an error during the grading. This may be " + \
                  "\nour fault though. If you'd like, you may email your " + \
                  "\ncode to support@udacity and let us know there's a problem."
        return is_correct + comment
    # DATA STRUCTURE CREATED


    try:
        if (set([x.upper() for x in stud_out]) != set(sol_out)):
            is_correct = "NO"
            comment += "\nYour get_connections function didn't behave as expected."
            return is_correct + comment
        if (len(stud_out) > len(sol_out)):
            is_correct = "NO"
            comment += "\nCalling get_connections seems to give duplicates. Make sure " + \
                "\neach connection is only listed once."
            return is_correct + comment
    
    except Exception as e:
        e = '\n' + str(e)
        is_correct = "NO"
        comment += e
        return is_correct + comment

        # GET CONNECTIONS WORKS
    try:
        print 'len ' + str(len(stud_network))
        if DEBUG: 
            for stud in stud_network:
                if stud:
                    if stud['name'] == 'a':
                        print stud
        stud_network = add_new_user(stud_network, 'A', ['X1', 'X2'])
        print stud_network
        if DEBUG: 
            print 'place 0'
        sol_network = solution.add_new_user(sol_network, 'A', ['X1', 'X2'])

        if DEBUG:
            print 'place 1'

        if set([x.upper() for x in get_connections(stud_network, 'A')]) != set(solution.get_connections(sol_network, 'A')):
            is_correct = 'NO'
            comment += "Your add_new_user function didn't behave as expected."
            return is_correct + comment
            

        stud_network = add_new_user(stud_network, 'G', [])
        sol_network = solution.add_new_user(sol_network, 'G', [])
        if DEBUG:
            print 'place 3'
        if len(get_connections(stud_network, 'G')) != 0:
            is_correct = 'NO'
            comment += "Your add_new_user function didn't behave as expected when adding a user with no game preferences OR your get_connections function doesn't return an empty list when called with the name of a user with no connections"
            return is_correct + comment
            
        if DEBUG:
            print 'hello'
        stud_network = add_new_user(stud_network, 'H', ['X1', 'X7'])
        sol_network = solution.add_new_user(sol_network, 'H', ['X1', 'X7'])

        if DEBUG:
            print 'i am here'
        if len(get_connections(stud_network, 'H')) != 0:
            is_correct = 'NO'
            comment += "Your add_new_user function didn't behave as expected when adding a user with no game preferences OR your get_connections function doesn't return an empty list when called with the name of a user with no connections"
            return is_correct + comment
    
    except Exception as e:
        if DEBUG:
            comment += '\n' + str(e)
        comment += "There was unexpected behavior in either your get_connections " + \
            "or add_new_user function."
        is_correct = "NO"
        return is_correct + comment    

        # ADD_NEW_USER WORKS

    # test get_secondary_connections(stud_network, user):
    try:
        stud_out1 = get_secondary_connections(stud_network, 'G') 
        sol_out1 = solution.get_secondary_connections(sol_network, 'G')
        if DEBUG:
            print sol_out1
        stud_out2 = get_secondary_connections(stud_network, 'J')
        sol_out2 = solution.get_secondary_connections(sol_network, 'J')
        if DEBUG:
            print sol_out2
    except:
        if DEBUG:
            print "get_secondary_connections exception" 
            raise
        is_correct = "NO"
        comment += "There was an error calling get_secondary_connections."
        return is_correct + comment

    if (len(stud_out2) != 1):
        is_correct = "NO"
        comment += "Your get_secondary_connections function didn't behave as expected"
        return is_correct + comment

    # GET SECONDARY CONNECTIONS WORKS

# test connections in common(stud_network, person_A, person_B):
    try:
        q1 = connections_in_common(stud_network, 'I', 'B') == solution.connections_in_common(sol_network, 'I', 'B')
        q2 = connections_in_common(stud_network, 'G', 'I') == solution.connections_in_common(sol_network, 'G', 'I')
        q3 = connections_in_common(stud_network, 'E', 'I') == solution.connections_in_common(sol_network, 'E', 'I')
        q4 = connections_in_common(stud_network, 'C', 'F') == solution.connections_in_common(sol_network, 'C', 'F')
        if DEBUG:
            print q1
            print q2
            print q3
            print q4
    except:
        if DEBUG:
            print 'connections_in_common exception' 
            raise
        is_correct = "NO"
        comment += "Your connections_in_common function didn't behave as expected."
        return is_correct + comment
        
    
    if not (q1 and q2 and q3 and q4):
        is_correct = "NO"
        comment += "\nYour connections_in_common function didn't behave as expected."
        return is_correct + comment

    try:
        a1 = path_to_friend(stud_network, 'J', 'A')
        if not solution.is_valid_path(sol_network, 'J', 'A', a1):
            is_correct = "NO"
            comment += "\nYour path_to_friend function didn't behave as  expected."
            return is_correct + comment
    except:
        if DEBUG:
            print 'path_to_friend exception'
            raise
        is_correct = "NO"
        comment += "\nThere was an error while calling your path_to_friend function."
    
    if is_correct == "OK":
        comment += '\nAll of your functions work as expected! Nice!'
    return is_correct + comment
        


# Run the test function "safely" (with stdout suppressed).
if DEBUG:
    print test(student_code_file)
else:
    try:
        output = StringIO()
        suppressed_stdout = sys.stdout
        sys.stdout = output
        results = test(student_code_file)
        sys.stdout = suppressed_stdout
        print results
    except Exception as e:
        sys.stdout = suppressed_stdout
        raise e
        print "NOThere was an error running your code."        


