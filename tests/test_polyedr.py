import unittest
from unittest.mock import patch, mock_open
import ans  # переменная ans.ans будет проверяться
from shadow.polyedr import Polyedr  # используем shadow для всех классов
# import noshadow.polyedr  # больше не нужен


class TestPolyedr(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0 45.0 45.0 30.0
8 4 16
-0.5 -0.5 0.5
-0.5 0.5 0.5
0.5 0.5 0.5
0.5 -0.5 0.5
-0.5 -0.5 -0.5
-0.5 0.5 -0.5
0.5 0.5 -0.5
0.5 -0.5 -0.5
4 5 6 2 1
4 3 2 6 7
4 3 7 8 4
4 1 4 8 5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open', new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)


    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)


class TestPolyedrAnsValue1(unittest.TestCase):
    def setUp(self):
        ans.ans = 0
        self.fake_file_content = """200.0 45.0 45.0 30.0
8 4 16
-0.5 -0.5 0.5
-0.5 0.5 0.5
0.5 0.5 0.5
0.5 -0.5 0.5
-0.5 -0.5 -0.5
-0.5 0.5 -0.5
0.5 0.5 -0.5
0.5 -0.5 -0.5
4 5 6 2 1
4 3 2 6 7
4 3 7 8 4
4 1 4 8 5"""

    def test_ans_value(self):
        fake_path = 'data/fake_file.geom'
        with patch('shadow.polyedr.open', new=mock_open(read_data=self.fake_file_content)):
            Polyedr(fake_path)
        self.assertEqual(ans.ans, 0)


class TestPolyedrAnsValue2(unittest.TestCase):
    def setUp(self):
        ans.ans = 0
        self.fake_file_content = """40.0 45.0 -30.0 -60.0
8 2 8
0.0 0.0 0.0
5.0 0.0 0.0
5.0 5.0 0.0
0.0 5.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
6.0 6.0 3.0
1.0 6.0 3.0
4 1    2    3    4    
4 5    6    7    8"""

    def test_ans_value(self):
        fake_path = 'data/fake_file.geom'
        with patch('shadow.polyedr.open', new=mock_open(read_data=self.fake_file_content)):
            Polyedr(fake_path)
        self.assertEqual(ans.ans, 50)
