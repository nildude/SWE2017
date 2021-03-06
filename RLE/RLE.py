# Runlength encoder: onvert 'kkkbbbb' til [(3,'k'),(4,'b')]

def encode(mess):
    if not mess:
        return ''
    old = mess[0]
    i = 1
    res = []

    for c in mess[1:]:
        if c != old:
            res.append((i,old))
            i = 1
            old = c
        else:
            i += 1
    res.append((i,old))

    return res

def decode(mess):
    num = 0
    res = []
    for c in mess:
        if c.isdigit():
            num = 10*num+int(c)
        else:
            res.append(num*c)
            num = 0
    return ''.join(res)
