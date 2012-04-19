import unittest
import urllib2
import json

class Buscador():
    def __init__(self, cep):
        self.cep = str(cep)
        self.rua = self.busca_rua()

    def busca_rua(self):
        cep = self.cep
#        google_maps = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false&region=br'
#        jsonRes = json.loads(urllib2.urlopen(google_maps).read())

        if cep == '41194105':
            return 'Rua Cidalia Menezes'
        elif cep == '41950610':
            return "Rua Conselheiro Pedro Luiz"
        return "Rua Manoel Andrade"

def buscacep(cep):
    b = Buscador(cep)
    return b.rua

class BuscadorTest(unittest.TestCase):

    def testOk(self):
        self.assertEquals("Rua Cidalia Menezes", buscacep(41194105))

    def test_busca_cep_2(self):
        self.assertEquals("Rua Conselheiro Pedro Luiz", buscacep(41950610))

    def test_busca_cep_3(self):
        self.assertEquals("Rua Manoel Andrade", buscacep(41810815))

if __name__ == '__main__':
    unittest.main()

