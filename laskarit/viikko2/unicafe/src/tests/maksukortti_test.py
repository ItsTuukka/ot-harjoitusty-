import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alku_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldon_lataaminen(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_ota_rahaa_kun_riittää(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_ota_rahaa_kun_ei_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
    
    def test_saldo_euroissa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    