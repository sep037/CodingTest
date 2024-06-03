import sys
import math

input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

e = math.lcm(b,d)
f = e//b
g = e//d

molecule = a*f +c*g
denominator = e

gcd_moledeno = math.gcd(molecule, denominator)
answermole = int(molecule/gcd_moledeno)
answerdeno = int(denominator/gcd_moledeno)

print(str(answermole)+' '+str(answerdeno))