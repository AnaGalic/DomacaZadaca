from math import sqrt


class Trokut(object):

     def __init__(self, a, b, c):
          self.__stranice = [a, b, c]
          self.__a = a
          self.__b = b
          self.__c = c
          for stranica in self.__stranice:
            if stranica <= 0 or (self.__stranice[0] + self.__stranice[1]) <= self.__stranice[2]:
                raise ValueError("Nije trokut")
                
                
     def __str__(self):
          return "trokut %s %s %s " % (self.__stranice[0], self.__stranice[1],
               self.__stranice[2])

     def __repr__(self):
          return "Trokut (%s, %s, %s) " % (self.__stranice[0], self.__stranice[1],
               self.__stranice[2])

     def opseg(self):
          return self.__stranice[0] + self.__stranice[1] + self.__stranice[2]

     def povrsina(self):
          s = self.opseg()/2
          return sqrt((s - self.__stranice[0]) * (s - self.__stranice[1]) * (s - self.__stranice[2]))
          
 class JednakokracniTrokut(Trokut):

     def __init__(self, a, b):
          self.__a = a
          self.__b = b
          super(JednakokracniTrokut, self).__init__(a, b, b)

 class JednakostranicniTrokut(Trokut):

     def __init__(self, a):
          self.__a = a
          super(JednakostranicniTrokut, self).__init__(a, a, a)
                
               
           
print('*** test 1 ***')
lista_stranica = [(1,2,3),(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
     try:
          t = Trokut(*stranice)
          print(repr(t))
     except Exception as e:
          print(e, stranice)

print('*** test 2 ***')
lista_stranica = [(3,4,5),(3,4,4),(3,3,3)]
for stranice in lista_stranica:
     t = Trokut(*stranice)
     print('%r ima opseg %.3f i povrsinu %.3f' % (t, t.opseg(), t.povrsina()))

print('*** test 3 ***')
trokuti = [Trokut(3,4,5),JednakokracniTrokut(3,4),JednakostranicniTrokut(5)]
for t in trokuti:
     print(t)
          
