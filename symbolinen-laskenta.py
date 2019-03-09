
# coding: utf-8

# # Symbolinen laskenta sympy-kirjastoa käyttäen
# 
# Tässä muistikirjassa käydään läpi Pythonin symbolisen laskennan sympy-kirjaston perusulottuvuuksia.

# In[1]:


import sympy


# In[2]:


z**2


# In[3]:


sympy.var('z') # esitellään muuttuja ensin


# In[4]:


z**2 # nyt sillä voidaan laskea


# In[5]:


True^True # ^ on varattu Pythonissa XOR-operaatiolle


# In[6]:


True^False


# In[7]:


z**(1/2) 


# Yllä Python laskee suluissa olevan jakolaskun ensin
# ja siitä tulee Python-objekti ennen kuin SymPy ehtii muuttaa sen SymPyn olioksi.

# Ratkaisu on käyttää sympify() tai Rational-luokkaa.

# In[8]:


z**(sympy.sympify(1)/2)


# In[9]:


z**sympy.Rational(1/2)


# Esitellään muuttujia:

# In[10]:


from sympy import symbols
x, y, z = symbols('x y z')
u, v, w = symbols('u v w')
symbols('j0:7')


# In[11]:


g, h = symbols('h g')


# In[12]:


g


# In[13]:


h


# Variables Assignment does not Create a Relation Between Expressions

# In[14]:


from sympy import Symbol
a=Symbol('a') # muuttujan a arvo a


# In[15]:


b=a+1 # muuttujan b arvo lauseke a+1


# In[16]:


print(b)


# In[17]:


a=4 # nyt a osoittaa kokonaislukuun 4, ei symboliin a


# In[18]:


print(a)


# In[19]:


print(b) # b osoittaa lausekkeeseen, jonka arvo a+1


# In[24]:


from sympy.abc import p


# In[25]:


sympy.sqrt(p**2) # SymPy ei yksinkertaista tätä, koska vastauksena voi olla 1- tai 1


# In[26]:


p=Symbol('p', positive=True) # nyt ratkaisu on yksikäsitteinen


# In[27]:


sympy.sqrt(p**2)


# Yhtäsuuruuden testausta, Eq, ==

# In[28]:


from sympy import symbols
x, y = symbols('x y')
sympy.Eq(x,y) # symbolinen yhtäsuuruus ilmaistaan Eq:lla


# In[29]:


(x-1)**2 == x**2-2*x+1 # == testaa symbolista samankaltaisuutta


# In[30]:


(x-1)**2 == (x-1)**2 # == testaa symbolista samankaltaisuutta


# Semanttisen samankaltaisuuden testaamiseen vähennä lausekkeet toisistaan ja käytä expand, simplify. Muista myös trigsimp, powsimp, trigsimp, logcombine, radsimp, together

# In[31]:


from sympy import simplify
simplify((x-1)**2-(x**2-2*x+1))


# In[32]:


from sympy import sin, cos, simplify, expand, powsimp, trigsimp, logcombine, radsimp, together
sinilauseke1 = sin(2*x)-2*sin(x)*cos(x)


# In[33]:


simplify(sinilauseke1)


# In[34]:


expand(sinilauseke1, trig=True)


# In[35]:


from sympy.abc import a,b
expand((a-b)**4) # lasketaan (a-b)^4


# In[36]:


expand(2*x+3*y, complex=True) # otetaan kompleksiluvut käyttöön


# In[37]:


expand(cos(x+y)**2, trig=True) # otetaan trigonometriset funktiot käyttöön


# In[38]:


expand(cos(x+2*y), trig=True)  # otetaan trigonometriset funktiot käyttöön


# In[40]:


simplify((x**3+y**2*x)/x) # lausekkeen sieventämistä


# In[48]:


from sympy import I
expand((4+3*I)**(4+3*I)) #lausekkeen sieventämistä


# Harjoittele: laske (x-y)^4 ja sievennä sin(x)/cos(x)

# In[49]:


powsimp(x**a*x**b) #lasketaan potensseja


# In[51]:


import pprint #pretty printing
pprint((3-x**(2*x)/(x+1)))


# In[52]:


together(x**6-17*x**4+8*x**2+5+3*x**5+22*x**3-8*x+6)


# In[53]:


together(1/a+1/b)


# Kuviot

# In[54]:


import matplotlib.pyplot
get_ipython().magic('matplotlib inline')


# In[55]:


sympy.plot(sympy.sin(x))


# In[56]:


sympy.plot(sympy.sin(x)/x)


# In[57]:


sympy.plot(sympy.exp(-x)*sympy.sin(x**2), (x, 0, 1)) #tässä rajoitettiin aluetta


# In[58]:


sympy.plot(sympy.exp(2*x))


# In[59]:


sympy.plot(sympy.log(2/x))


# Derivointi, differentiaalit ja integrointi

# In[64]:


from sympy import diff, exp
diff(cos(2*x),x)


# In[66]:


k = symbols('k', integer=True)
diff(exp(k*x),x)


# In[69]:


from sympy import log
diff(log(1/x),x)


# Korkeammat derivaatat

# In[70]:


diff(cos(2*x),x,3)


# In[72]:


diff(exp(k*x),x,2)


# In[74]:


from sympy import erf
diff(erf(x),x)


# Hyvä tapa on myös määritellä lausekkeita ja derivoida niitä:

# In[75]:


expr = x**2*sympy.sin(sympy.log(x))


# In[76]:


sympy.diff(expr,x)


# Osittaiderivointi:

# In[77]:


expr2 = x*sympy.cos(y**2 + x)


# In[78]:


sympy.diff(expr2, x, 2, y, 3)


# Määräämätön derivaatta:

# In[79]:


sympy.Derivative(expr2, x, 2, y, 3)


# In[80]:


sympy.Derivative(expr2, x, 2, y, 3).doit()


# Integrointi:

# In[82]:


from sympy import integrate
integrate(5*x**5,x)


# In[83]:


integrate(3*exp(3*x),x)


# In[84]:


integrate(cos(x),x)


# In[85]:


integrate(log(x),x)


# In[86]:


integrate(exp(-x**2)*erf(x), x)


# In[88]:


sympy.integrate(sympy.exp(-(x+y))*sympy.cos(x)*sympy.sin(y), x, y)


# Määritetään lauseke ja operoidaan sillä:

# In[87]:


integrand=sympy.log(x)**2


# In[90]:


sympy.integrate(integrand, x)


# Sarjat:

# In[92]:


from sympy import series
series(cos(x), x)


# In[93]:


series(erf(x),x)


# In[94]:


series(exp(x),x)


# In[95]:


series(1/cos(x), x)


# Sympy laskimena

# In[120]:


v, w, u = sympy.symbols('v, w, u')
n = sympy.symbols('n', interger=True)
from sympy import Mul, Pow, Rational, pi, N, oo


# In[100]:


Mul(3, Rational(2,4))


# In[101]:


Mul(3, Rational(2,4), evaluate=False)


# In[102]:


Pow(x*y,2)


# In[103]:


Pow(x*y,2, evaluate=False)


# In[106]:


pi*2


# In[108]:


exp(1)


# In[109]:


pi.evalf()


# In[113]:


pi.evalf(5)


# In[117]:


N(pi)


# In[118]:


N(pi, 5)


# In[112]:


print(exp(1))


# In[122]:


oo>999999999


# In[123]:


oo/2


# Laske 
# - luvun kaksi neliöjuuri 50 desimaalilla,
# - mikä on piin 26. desimaali,
# - paljonko on luvun pi + e likiarvo.
# 

# Raja-arvot

# In[128]:


from sympy import limit, sin, exp, oo
limit(sin(x)/x,x,0)


# In[129]:


limit(exp(x)/x, x, oo)


# In[130]:


limit((1+1/x)**x,x,oo)


# Määrätty intergraali:

# In[131]:


integrand=sympy.log(x)**2


# In[133]:


sympy.integrate(integrand, (x, 1, 10))


# In[134]:


sympy.integrate(sympy.exp(-x), (x, 0, sympy.oo))


# Moninkertainen integraali:

# In[141]:


integrate(exp(-x**2-y**2),(x,-oo,oo),(y,-oo,oo))


# In[ ]:


Voidaan myös luoda määräämätön Integral-objekti. Sen arvo voidaan laskea myöhemmin.


# In[138]:


sympy.Integral(integrand, (x, 1, 10))


# In[142]:


sympy.Integral(integrand, (x, 1, 10)).doit()


# Yhtälönratkaisu

# In[143]:


a, b, c, x = sympy.symbols(('a', 'b', 'c', 'x'))


# In[144]:


quadr_eq = sympy.Eq(a*x**2+b*x+c, 0)


# In[145]:


sympy.solve(quadr_eq)


# In[146]:


sympy.solve(quadr_eq, x)


# Opetus: Jos ei muuta määritetä, sympy ratkaisee ensimmäisen symbolin suhteen.

# In[148]:


from sympy import solve
solve(x**4 - 1, x)


# In[150]:


solve(x**2+2*x-1,x)


# Yllä olevat vastaukset hakasuluissa [] ovat listoja. Listat voivat sisältää erilaisia objekteja ja niitä voi muuttaa.

# In[153]:


from sympy import roots
roots(x**2+2*x-1,x)


# In[156]:


solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])


# Edellä olevat vastaukset taas ovat sanakirjoja. Ne ovat järjestämättömiä listoja ilman toistoja.
# 
# Huom. solve -> list, roots -> dictionary.

# In[157]:


solve(exp(x) + 1, x) #Eulerin lause, Eulerin identiteetti


# Ratkaise yhtälö
# (x-1)^4=4^4

# Jatketaan yhtälön quadr_eq ratkaisemista:

# In[164]:


ratkaisut=sympy.solve(quadr_eq, x)


# In[165]:


xplus=ratkaisut[0]
xminus=ratkaisut[1]


# In[166]:


xplus_arvot=xplus.subs([(a,1),(b,2),(c,3)])


# In[167]:


xplus_arvot


# In[ ]:


Voidaan sijoittaa myös muita muuttujia:


# In[170]:


sympy.var('z0')
xminus_arvot=xminus.subs([(b,a), (c,a+z0)])


# In[171]:


xminus_arvot


# In[172]:


xminus_arvot.simplify()


# Solveset on suositeltavin yhtälöiden ratkaisuun. Solveset kertoo kunkin ratkaisun vain kerran, moninkertaisuuden selvittämiseksi on hyvä käyttää funktiota roots:

# In[175]:


from sympy import solveset, roots
solveset(x**3-6*x**2+9*x,x)


# In[176]:


roots(x**3-6*x**2+9*x,x)


# Huomaa vielä ero kahden seuraavan outputin kanssa.

# In[178]:


solveset(exp(x), x) # Yhtälöllä e^x = 0 ei ole ratkaisuja.


# In[183]:


solveset(cos(x)-x,x) # Tälle yhtälölle sympy ei löydä ratkaisua.


# Määritellään vielä funktioita:

# In[181]:


from sympy import Function
f, g = symbols('f g', cls=Function)


# In[182]:


f(x)


# In[185]:


f(x).diff(x)


# Tekijöihin jakoa:

# In[186]:


poly = x**4 - 3*x**2 + 1


# In[188]:


from sympy import factor
factor(poly)


# In[189]:


factor(poly,modulus=5)


# Boolean lausekkeita

# In[191]:


from sympy import satisfiable
satisfiable(x & y)

