from time import sleep

states = {
    # state_key: []
}
symbols = '0123456789qwertyuiopasdfghjklzxcvbnm'

def next_char(char):
    next_index = symbols.index(char) + 1
    if next_index < len(symbols):
        return symbols[next_index]

def increment_at_index(password, i):
    if len(password) <= i:
        password.append('0')
        return

    char = next_char(password[i])
    if char:
        password[i] = char
    else:
        password[i] = '0'
        increment_at_index(password, i+1)

def get_next_str(state_key):
    if state_key not in states:
        states[state_key] = []

    password = states[state_key]
    increment_at_index(password, 0)
    return ''.join(password)

if __name__ == '__main__':
    for step in range(1500000):
        print(get_next_str('1'))
        # sleep(.1)