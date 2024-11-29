import sympy as sp

u , a , t , b , x1 , x2 , y1 , y2  = sp.symbols('u, a, t, b, x1, x2, y1, y2')

u = (1/(2*a*(t*sp.pi)**(1./2))**2)*sp.exp(-(((x1-y1)**2 +(x2-y2)**2 )/(4*t*a**2)))
pr = sp.diff(u, t)
pr1 = sp.diff(u, x1, 2)
pr2 = sp.diff(u, x2, 2)
h = a**2*(pr1+pr2)
an=sp.simplify(h)
pran=sp.simplify(pr)
print(sp.simplify(an-pran))

