# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure
def create_data_structure(string_input):
    sentences = [sentence.strip() for sentence in string_input.split('.')]
    network = [parse_sentence(sentence) for sentence in sentences]
    return network

def parse_sentence(s):
    words = [word.strip().lower() for word in s.split()]
    if len(words) < 3:
        return None
    name = words[0]
    if words[1] == 'is': 
        s_type = 'conns'
    else:
        s_type = 'games'
    value_string = ' '.join(words[4:])
    values = value_string.split(', ')
    parsed = {'name': name,
              'conns': set([]),
              'games': set([])}
    parsed[s_type] = values
    return parsed


# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.  
def get_connections(network, user):
    name = user.lower()
    if not network:
        return False
    for user in network:
        if not user:
            continue
        if user['name'] == name:
            return user['conns']

network = create_data_structure(example_input)
# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.
def add_connection(network, user_A, user_B):
    user_A = user_A.lower()
    user_B = user_B.lower()
    A_in = False
    B_in = False
    for person in network:
        if not person:
            continue
        if person['name'] == user_B:
            B_in = True
        if person['name'] == user_A:
            A_in = True
    if not A_in and B_in:
        return False
    for user in network:
        if not user:
            continue
        if user['name'] == user_A:
            user['conns'].append(user_B)
            return network
        
	return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.
"""def add_new_user(network, user, games):
    user = user.lower()
    for person in network:
        if not person:
            continue
        if not person['name']:
            continue
        elif person['name'] == user:
            if person['games']:
                print person['games']
            print games
            if games:
                person['games'].add(games)
            return network

    user_dict = {'name': user.lower(),
                 'conns': set([]),
                 'games': set(games)}
    network.append(user_dict)
                
    return network"""
def add_new_user(network, user, games):
    games = set(games)
    print 'games: ' + str(games)
    user = user.lower()
    for person in network:
        #print '1'
        if person:
            #print '2'
            if person['name'] == user:
                print '3'
                if games:
                    print '4'
                    person['games'] = person['games'].intersection(games)
                    print '5'
                return network
    print '6'
    user_dict = {'name':user,
                 'conns': set([]),
                 'games': set(games)}

    print '7'
    network.append(user_dict)
    print '8'
    return network





# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    to_return = []
    for person in network:
        if person:
            if person['name'] == user:
                return None
    for connection in get_connections(network, user):
        for secondary in get_connections(network, connection):
            to_return.append(secondary)


	return to_return

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.
def connections_in_common(network, user_A, user_B):
    A_conns = get_connections(network, user_A)
    B_conns = get_connections(network, user_B)
    ctr = 0
    for name in A_conns:
        if name in B_conns:
            ctr += 1
    return ctr

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user, connection): 
#   Finds the connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#                   Solve this problem using recursion. 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hint: 
#   Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
def path_to_friend(network, user, connection):
	return ["J", "I", "A"]
	return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun! 
"""
net = create_data_structure(example_input)
path_to_friend(net, 'John', 'Ollie')
get_connections(net, "Debra")
add_new_user(net, "Debra", []) # False - Debra is already in network
add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
get_connections(net, "Mercedes")
add_connection(net, "John", "Freda")
get_secondary_connections(net, "Mercedes")
connections_in_common(net, "Mercedes", "John")
"""




