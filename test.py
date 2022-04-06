import unittest
import requests
import app
import sqlalchemy
from sqlalchemy import create_engine

class PrimeTests(unittest.TestCase):
    def pushEquation(self):
        r = requests.post('https://localhost:5000/add', data={'expression':'1+1'})
        self.assertIn("1+1", r.content)

    def connectDB(self):
        name = 'localhost'
        engine = create_engine(f'postgresql://cs162_user:cs162_password@{name}:5432/cs162', echo = True)
        engine.execute('SELECT * FROM Expressions')
        r = requests.get('http://localhost:8080/?pgsql=db&username=cs162_user')
        self.assertIn("cs162_user", r.content)

    def pushError(self):
        r = requests.post('https://localhost:5000/add', data={'expression':'a+b'})
        self.assertEqual(r.status_code, 500)

    def noNewLines(self):
        r = requests.get('https://localhost:5000')
        self.assertNotIn("a+b", r.content)


if __name__ == '__main__':
    unittest.main()
