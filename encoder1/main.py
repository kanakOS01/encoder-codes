def _____________(str):
    _=""
    for __ in str:
        _=__+_
    return _
def ____________(str):
    _=""
    for __ in str:
        if "A" <= __ <= "Z":
            _+=chr(ord(__)+32)
        else:
            _+=chr(ord(__)-32)
            _+=chr(ord(__)+64)
            _+=chr(ord(__)-32)
            _+=__
    return _
def ___________(str):
    _=_____________(str)
    ____=____________(_)
    _______ = ""
    for __ in range(min(5, len(____))):
        _______+=____[__]
    _______+=____
    return _______
_____ = input()
_______ = ___________(_____)
print(_______)