class Stvar(object):

    brStvari = 0

    def __init__(self):
        Stvar.brStvari += 1

    def __del__(self):
        Stvar.brStvari -= 1

  
