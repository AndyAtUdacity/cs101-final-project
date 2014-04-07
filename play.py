import solution
s = solution.test_string_1
sol_network = solution.create_data_structure(s)

sol_out = solution.get_connections(sol_network, 'A')

print '1'
print sol_out

sol_network = solution.add_new_user(sol_network, 'A', ['X1', 'X2'])

print '2'
print solution.get_connections(sol_network, 'A')

sol_network = solution.add_new_user(sol_network, 'G', [])

print '3'
print solution.get_connections(sol_network, 'G')

sol_network = solution.add_new_user(sol_network, 'H', ['X1', 'X7'])

print '4'
print solution.get_connections(sol_network, 'H')