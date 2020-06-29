import alpc
import unittest

class TestAlpc(unittest.TestCase):
    def test_A(self):
        self.assertEqual(alpc.encode('A'), 16777217)
    
    def test_FRED(self):
        self.assertEqual(alpc.encode('FRED'), 251792692)
    
    def test_special_chars(self):
        self.assertEqual(alpc.encode(' :^)'), 79094888)
        
    def test_foo(self):
        self.assertEqual(alpc.encode('foo'), 124807030)
        
    def test_spacefoo(self):
        self.assertEqual(alpc.encode(' foo'), 250662636)
        
    def test_foot(self):
        self.assertEqual(alpc.encode('foot'), 267939702)
        
    def test_BIRD(self):
        self.assertEqual(alpc.encode('BIRD'), 251930706)
        
    def test_dotdotdotdot(self):
        self.assertEqual(alpc.encode('....'), 15794160)
        
    def test_special_chars_2(self):
        self.assertEqual(alpc.encode('^^^^'), 252706800)
        
    def test_Woot(self):
        self.assertEqual(alpc.encode('Woot'), 266956663)
        
    def test_no(self):
        self.assertEqual(alpc.encode('no'), 53490482)

if __name__ == '__main__':
    unittest.main()
