
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




