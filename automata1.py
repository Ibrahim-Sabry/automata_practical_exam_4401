transitions = {
    'S0': {'0': 'S0', '1': 'S1'},
    'S1': {'0': 'S1', '1': 'S2'},
    'S2': {'0': 'S2', '1': 'S0'}
}
start_state = 'S0'
accept_state = 'S0'

def accepts(string):
    current_state = start_state
    one_count = 0

    for char in string:
        if char not in ['0', '1']:
            return False  
        if char == '1':
            one_count += 1
        current_state = transitions[current_state][char]

    return current_state == accept_state and one_count > 0

test_cases = ['1', '11', '111', '1111', '000111000', '', '000', '101010', '110011']

for s in test_cases:
    result = accepts(s)
    print(f"'{s}' -> {'ACCEPTED' if result else 'REJECTED'}")