from django.test import TestCase, Client

class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_acccess(self):
        res = self.c.get('/')
        self.assertEqual(200, res.status_code)

    def test_fail_acccess(self):
        res = self.c.get('/unkwoun')
        self.assertEqual(404, res.status_code)
    