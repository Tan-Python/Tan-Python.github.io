___=lambda *____:____[0]
____=lambda ______:___.__code__.co_consts
_____=(lambda:None)
_______=lambda:_____(_____)

I=__import__
R=I('random')
B=I('base64')
Z=I('zlib')

o0=lambda x:((x^13)&255)
o1=lambda x:((x*7+3)%256)
o2=lambda a,b:(a^b)^(a&b)
o3=lambda s:sum(map(ord,s))%997
N=(o2(o0(231),o1(77))^o3("void"))&0xFFFF

S=((N<<1)^0x1337)^(0xDEAD&0xBEEF)
S=(S%1000000)

PAYLOAD=b'eJxLzs8tKEotLlHQS8xNVdBRCM8oKMgvyC8tSk2tVdBTKskvTi0oVrJQ8CkDAwC1TQkYw=='

def d(x):
    try:
        return Z.decompress(B.b64decode(x)).decode('utf-8','ignore')
    except:
        return ''

p=(lambda *x:print(*x))
g=(lambda a,b: R.randint(a,b))

A=g(0, 499999)
B0=g(500000, 999999)
C=g(0, 9)
J=(A^B0^C) & 0xFFFFFF

M=[A,B0,C,J,S]
R.shuffle(M)
T=M[-1]

F=lambda u,v:(((u^13)^((v<<1)&0xFFFFFF))^((u&v)|((~v)&u)))&0xFFFFFF
K=F(C,0)^F(A,0)^F(B0,0)

if (K%1000000)==(T%1000000):
    p(d(PAYLOAD))
else:
    p("Misstep. Try again.")
