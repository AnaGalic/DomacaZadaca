class Stvar(object):

    brStvari = 0

    def __init__(self):
        Stvar.brStvari += 1

    def __del__(self):
        Stvar.brStvari -= 1

  
print('*** test 1 ***')
s1 = Stvar()
s2 = Stvar()
s3 = s2
print(Stvar.broj_stvari)
del(s2)
print(Stvar.broj_stvari)
del(s3)
print(Stvar.broj_stvari)
del(s1)
print(Stvar.broj_stvari)
