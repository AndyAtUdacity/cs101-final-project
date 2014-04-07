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

test_string_1 = "A is connected to B, E. A likes to play X1, X2, X3. " + \
	"B is connected to A, C, F. B likes to play X2, X3, X5. " + \
	"C is connected to D, E. C likes to play X1, X2, X5. " + \
	"D is connected to A, E. D likes to play X4, X6. " + \
	"E is connected to F. E likes to play X3, X6. " + \
	"F is connected to D. F likes to play X3, X5, X6, X7. " + \
	"I is connected to A. I likes to play X4, X7." + \
	"J is connected to I. J likes to play X2, X5." + \
	"K is connected to J, I. K likes to play X4, X6."

def parse_sentence(sentence):
	"""Takes a sentence and returns a dictionary. Dictionary looks something 
	like {'John': {'conn': ['Bryant', 'Debra', 'Walter']}}"""
	sentence = sentence.lstrip()
	conn_phrase = " is connected to "
	game_phrase = " likes to play "
	location = sentence.find(conn_phrase)
	if location == -1:
		location = sentence.find(game_phrase)
		offset = len(game_phrase)
		s_type = 'game'
	else:
		offset = len(conn_phrase)
		s_type = 'conn'
	name = sentence[:location]
	values_string = sentence[location + offset:]
	values = values_string.split(',')
	good_values = []
	for value in values:
		good_values.append(value.lstrip())
	return (s_type, name, good_values)

def create_data_structure(string_input):
	sentences = string_input.split(".")
	sentences = sentences[0:-1]
	structure = {}
	for sentence in sentences:
		s_type, name, values = parse_sentence(sentence)
		if name not in structure:
			structure[name] = {}
		if name in structure:
			structure[name][s_type]=values
	return structure

def get_connections(network, user):
	if user not in network:
		return []
	return network[user]['conn']

def add_connection(network, user_A, user_B):
	if (user_A not in network) or (user_B not in network):
		return False
	if user_B in network[user_A]['conn']:
		return network
	network[user_A]['conn'] = user_B
	return network

def add_new_user(network, user, games):
	"""Creates new user in network."""
	if user in network:
		if not games:
			return network
		for game in games:
			if game not in network[user]['game']:
				network[user]['game'].append(game)
		return network
	network[user] = {}
	network[user]['game'] = []
	network[user]['conn'] = []
	for game in games:
		if game not in network[user]['game']:
			network[user]['game'].append(game)
	return network

def get_secondary_connections(network, user):
	if user not in network:
		return None
	primary_connections = get_connections(network, user)
	if primary_connections == []:
		return []
	all_secondary_connections = []
	for user in primary_connections:
		sec_conns = get_connections(network, user)
		for sec_conn in sec_conns:
			all_secondary_connections.append(sec_conn)
	unique_secondary_connections = list(set(all_secondary_connections))
	return unique_secondary_connections

def connections_in_common(network, user_A, user_B):
	A_conns = set(get_connections(network, user_A))
	B_conns = set(get_connections(network, user_B))
	common_connections = A_conns.intersection(B_conns)
	return len(common_connections)

def path_to_friend(network, user_A, user_B, already_checked = []):
	already_checked.append(user_A)
	A_conns = get_connections(network, user_A)
	A_conns = list(set(A_conns) - set(already_checked))
	if user_B in A_conns:
		return [user_A, user_B]
	else:
		for user in get_connections(network, user_A):
			if user not in already_checked:
				ptf = path_to_friend(network, user, user_B, already_checked)
				if ptf:
					return [user_A] + ptf
			else: pass
		

def is_valid_path(network, user_A, user_B, student_path):
	if not student_path:
		if path_to_friend(network, user_A, user_B):
			return False
		else:
			return True
	stud_user_A = student_path[0]
	stud_user_B = student_path[-1]
	for i in range(len(student_path) - 1):
		new_A = student_path[i]
		new_B = student_path[i+1]
		if new_B in get_connections(network, new_A):
			continue
		else:
			return False
	return True
