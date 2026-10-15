class PasswordChecker:
    def check(self, password):
        if len(password) < 8:
            return False
        return True

def Password_Check():
    checker = PasswordChecker()
    assert checker.check("cici") == False
    assert checker.check("IfjMuSUlo") == True
    assert checker.check("") == False

Password_Check()