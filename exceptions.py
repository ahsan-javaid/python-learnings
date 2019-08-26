class InvalidPasswordLengthException(Exception):
    def __init__(self, msg):
        self.msg = msg


def validatePassword(p):
    if(len(p) < 8):
        raise InvalidPasswordLengthException('Password length is less than 8 characters')

print('Enter password:')
p = str(input())

try:
    validatePassword(p)
except InvalidPasswordLengthException as m:
    print(m.msg)
else:
    print('Good password')


