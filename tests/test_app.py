import unittest
from unittest.mock import patch
from io import StringIO
import app

class TestApp(unittest.TestCase):
    @patch('sys.argv', ['app.py', 'get_tpl', '--customer=John Smith', '--дата_заказа=27.05.2025'])
    @patch('app.FormTemplateDB')
    def test_find_template_success(self, mock_db):
        mock_db.return_value.find_template.return_value = "Форма заказа"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            app.main()
            self.assertEqual(fake_out.getvalue().strip(), "Форма заказа")
    
    @patch('sys.argv', ['app.py', 'get_tpl', '--tumba=27.05.2025', '--yumba=+7 903 123 45 78'])
    @patch('app.FormTemplateDB')
    def test_find_template_fail(self, mock_db):
        mock_db.return_value.find_template.return_value = None
        with patch('sys.stdout', new=StringIO()) as fake_out:
            app.main()
            self.assertEqual(fake_out.getvalue().strip(), "{'tumba': 'Date', 'yumba': 'Phone'}")