
print('\n{:=^80}'.format(' método 01 '))
s ='hello'
print(s)
print('Total de caracteres: ',len(s))
res = len(s) - 1
print('Total menos (-1) = ',res)
print('A ultima letra é :',s[res:len(s)])

ss = []
print('='*80)
print(s)
for i in range(1,len(s)+1):
   print('{} - {}'.format(i,s[i-1:i]))
print('\nA ultima letra é :',s[res:len(s)])


ss = []
print('='*80)
print(s)
for i in range(1,len(s)+1):
    ss.append(i)
print('Lista Gerada',ss)
print('Ultimo número da lista é {}'
      '\nportanto a ultima letra é {}:'.format(ss.pop(),s[res:len(s)]))

print('='*80)
#Listas
#Crie esta lista [0,0,0] duas formas diferentes.

lista1 = [0,0]
lista2 = [0]
print(lista1)
print(lista2)

list = lista1 + lista2
print('soma das listas',list)

print('='*80)
alt2 = str('goodyby')
l = [1,2,[3,4,'hello']]
alt = l[2][2:3]
alt = alt2
print('String "hello" na lista alterada \nDE {} \nPARA {}'.format(l[2][2:3],alt))

ll = [5,3,4,6,1]
ll.sort()
print(ll)

print('{:=^80}'.format(' Dicionarios '))
d = {'simple_key':'hello'}
print(d['simple_key'])


d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])


l = [1,2,2,33,4,4,11,22,3,3,2]
setlista = set(l)
print(setlista)

# Duas listas aninhadas
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# Verdadeiro ou falso?
l_one[2][0] >= l_two[2]['k1']

print(l_one[2][0])
print(l_two[2]['k1'])








