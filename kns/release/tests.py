"""
Test relaese app
"""

from django.test import TestCase,Client
from models import Release

class UpdateTest(TestCase):

    def setUp(self):
        Release.objects.create(name = 'quick-knowhow', 
            appid = 'gcnjbhfkdigacmabhfnijjjengiojnol',
            version = '0.1', url = 'https://github.ocm/ftao/pkm-tool/download/quick-knowhow-0.1.crx')
        
    def test_update(self):
        client = Client()
        response = client.get('/release/quick-knowhow/update.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '''<?xml version='1.0' encoding='UTF-8'?>
<gupdate xmlns='http://www.google.com/update2/response' protocol='2.0'>
  <app appid='gcnjbhfkdigacmabhfnijjjengiojnol'>
    <updatecheck codebase='https://github.ocm/ftao/pkm-tool/download/quick-knowhow-0.1.crx' version='0.1' />
  </app>
</gupdate>
''')
