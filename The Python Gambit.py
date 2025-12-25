# hell
_ = __import__
R = _('\x72\x61\x6e\x64\x6f\x6d')
B = _('\x62\x61\x73\x65\x36\x34')
Z = _('\x7a\x6c\x69\x62')
C = (lambda a,b: getattr(a,b))
P = C(B,'b64decode')
Q = C(Z,'decompress')
Ξ = b'eJxLzs8tKEotLlHQS8xNVdBRCM8oKMgvyC8tSk2tVdBTKskvTi0oVrJQ8CkDAwC1TQkYw=='
σ = (lambda x: Q(P(x)).decode('utf-8','ignore'))
τ = (lambda: print('Misstep. Try again.'))
μ = (lambda s: (s, s[::-1], ''.join(chr((ord(c)^0x2F)) for c in s)))
δ = mu if False else None
ζ = (lambda: None)
α = R.getrandbits(32)
β = R.getrandbits(16)
γ = R.getrandbits(8)
ω = (((α<<5) ^ (β<<2) ^ γ) & 0xFFFFFFFF)
ω = ((ω >> 3) | (ω << 29)) & 0xFFFFFFFF
ω = (ω * 0x9E3779B1) & 0xFFFFFFFF
κ = (lambda v: ((v ^ (v>>7)) % 20) == 0)
class Θ:
    def __init__(self,f,g,h):
        self.__a=f; self.__b=g; self.__c=h
    def __call__(self):
        t = (self.__c() if (not (κ(ω))) else None)
        return (self.__a if (t is None) else self.__b)()
def ψ():
    return σ(Ξ)
def ρ():
    return τ()
χ = Θ(lambda: (print(ψ())), lambda: ρ(), lambda: (None if True else 0))
( (lambda z: (z()))(χ) )
