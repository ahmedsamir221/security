
import sys
from struct import pack, unpack

def F(w):
	return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32

def encrypt(block):
	a, b, c, d = unpack("<4I", block)
	for rno in xrange(32):
                t = a
                d = d ^ 1337
                a = c ^ F(d | F(d) ^ d)
                b = b ^ F(d ^ F(a) ^ (d | a))
                c = t ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)
                t = a
                a = d ^ 31337
                d = c ^ F(a | F(a) ^ a)
                c = b ^ F(a ^ F(d) ^ (a | d))
                b = t ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
	return pack("<4I", a, b, c, d)
pt = open(sys.argv[1]).read()

ct = "".join(encrypt(pt[i:i+16]) for i in xrange(0, len(pt), 16))
open( "xxxxxxx.txt", "w").write(ct)