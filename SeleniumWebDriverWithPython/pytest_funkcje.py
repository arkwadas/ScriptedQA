def dodawanie(a, b):
    return a + b

def mnozenie(a, b):
    return round(a * b, 10) #round to podnieś do 10 do pełnej kwoty

def fissbuzz(i):
    if i % 15 == 0:
        return 'fissbuzz'
    elif i % 3 == 0:
        return 'fiss'
    elif i % 5 == 0:
        return 'buzz'
    return i
