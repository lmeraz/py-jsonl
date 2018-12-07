import unittest
from unittest.mock import patch, mock_open
from jsonl import write_jsonl, parse_jsonl


class TestJSONL(unittest.TestCase):

    def test_write_jsonl(self):
        with patch('builtins.open', mock_open()) as mock_file:
            with open('query', 'w') as outfile:
                write_jsonl(['object'], outfile)
        mock_file.assert_called_once_with('query', 'w')
        handle = mock_file()
        handle.write.assert_called_once_with('["object"]\n')

    def test_parse_jsonl(self):
        expected = [['a'], ['b']]
        text_file_data = '\n'.join(['["a"]', '["b"]'])
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.return_value.__iter__.return_value = text_file_data.splitlines()
            with open('filename', 'r') as f:
                actual = list(parse_jsonl(f))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
