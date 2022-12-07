print('Владик легенда ')
print('Программа by Vladik ')

print('Нагрев - a, плавление - b,конденсация - c,кипеник - d, охлождение = e,сгорания - g , отвердивание - h, y - ток , Напряжение  t ')
r = input('Ваша буква: ')

if r == 'a':
    h = float(input('C ='))
    v = int(input('M ='))
    c = int(input('T1 = '))
    y = int(input('T2 ='))
    print('Решение по формуле:''c * m * (T1 - T2)''Решение:''Q =',h,'*',v,'*''(',c,'-',y,')')
    print(h * v * (c - y))
if r != 'b':
    pass
else:
    t = float(input('λ = '))
    q = int(input('M = '))
    print('Дано:')
    ta = t * q
    print('λ =',t, '|' 'q = ',t,'*',q)
    print('M =',q, '|' 'q =',ta )
    print('--------------')
    print('Q = ?')
    print('Решение по формуле: λ * m')
    n = t * q
    print('Решение:',n)
if r == 'c':
    g = float(input('L = '))
    f = int(input('M = '))
    print('Данo:')
    u = g * f
    print('L =',g,'  |  '' Q =' 'L * M')
    print('            Q =' ,g,'*',f)
    print('M = ', f, ' |  '' Q = ', u)
    print('--------------')
    print('Q = ?')
    print('Решение по формуле: L * M')
    u = g*f
    print('Ответ',u)
if r == 'd':
    i = int(input('L = '))
    Na = int(input('M = '))
    ba = i * Na
    print('L =', i, '  |  '' Q =' 'L * M')
    print('          |   Q =', i, '*', Na)
    print('M = ', Na, ' |  '' Q = ', ba)
    print('--------------')
    print('Q = ?')
    print('Решение по формуле: L * M')
    print(i*Na)
if r == 'e':
    ha = int(input('C ='))
    vs = int(input('M ='))
    cd = int(input('T1 = '))
    yx = int(input('T2 ='))
    print('Дано:')
    ran = ha * vs * (cd - yx)
    print('C = ', ha, '|''q = ',ha,'*',vs,'*''(',cd,'-',yx,')')
    print('m = ',vs, '|''q = ',ran)
    print('t1 =',cd,'|''q = ',ran)
    print('t2 =',yx)
    print(ha * vs * (cd-yx))
if r == 'g':
    ba = int(input('Q ='))
    fa = int(input('M ='))
    print('Дано:')
    print('q = ',ba,'|''q = q * m ')
    print('m = ',fa,'|''q =',ba,'*',fa)
    print(ba*fa)
if r == 'h':
    td = float(input('λ = '))
    qd = float(input('M = '))
    nf = td * qd
    print('Дано:')
    print('λ =',td,'|''q = λ * m')
    print('m = ',qd,' |''q = ',td,'*',qd)
    print('----------''|''q = ',nf)
    print('q = ?')
    nf = td * qd
    print(nf)
if r == 'y':
    rab =  float(input('q ='))
    fara = int(input('t = '))
    tara = rab * fara
    print('Дано')
    print('q = ',rab)
    print('t = ',fara)
    print('Решение по формуле q*t =',tara)
    print(tara)
if r == 't':
    tok = int(input('A = '))
    to = int(input('q = '))
    era = tok // to
    print('Дано')
    print('A =', tok)
    print('q = ',to)
    print('Решение по формуле A/q = ',era)
    print('Ответ:',era)
