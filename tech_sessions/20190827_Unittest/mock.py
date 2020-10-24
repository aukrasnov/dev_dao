from unittest import mock
import unittest
import pymysql
import os
import funcs
import statistics


def mock_isfile_se(filename):
    if filename.split('.')[-1] == 'txt':
        return True


class MyTestCase(unittest.TestCase):
    # @mock.patch('funcs.os.path.isfile', side_effect=mock_isfile_se)
    # def testB(self, mock_isfile):
    #     # m = mock.Mock()
    #     # funcs.os.path.isfile = m
    #     mock_isfile.side_effect = mock_isfile_se
    #     result = funcs.os.path.isfile(self)
    #     print(result)
        # self.assertEqual(1, funcs.exists('a.ext'))
    #
    #     self.assertEqual(1, mock_isfile('a.txt'))
    #     self.assertEqual(1, mock_isfile('b.txt'))
    #     self.assertNotEqual(1, mock_isfile('c.png'))
    #     self.assertNotEqual(1, mock_isfile('file.xls'))
    #
    # def testA(self):
    #     m = mock.Mock()
    #     funcs.os.path.isfile = m
    #     funcs.os.path.isfile.return_value = True
    #     self.assertEqual(1, funcs.B('a.txt'))
    #     funcs.os.path.isfile.return_value = False
    #     self.assertEqual(-1, funcs.B('a.txt'))

            # def se_isfile

    # @mock.patch('funcs.pymysql')
    # def testMedian(self, mock_connect):
    #     mock_connect.connect.cursor.execute.fetchall.return_value = [1, 2, 3, 4, 5]
    #     result = funcs.pymysql.connect.cursor.execute.fetchall()
    #     print(result)


#cursor
#fetchall

    # @mock.patch('funcs.pymysql.connect')
    # def testMedian(self, mock_pymysql):
    #
    #     mock_cursor = mock.Mock()
    #     mock_connect = mock.Mock()
    #     mock_cursor.fetchall.return_value = [{'kf': 1}, {'kf': 2}, {'kf': 3}, {'kf': 4}, {'kf': 5}]
    #     mock_pymysql.connect.return_value = mock_connect
    #     mock_pymysql.connect.return_value.cursor.return_value = mock_cursor
    #
    #     self.assertEqual(3, funcs.median('ri_cities', 'kf'))

    @mock.patch('funcs.pymysql.connect')
    # @mock.patch('funcs.pymysql.connect.return_value.cursor.return_value.fetchall')
    def testMedian(self, mock_connect):
        # mock_pymysql.return_value = mock.Mock()
        # mock_pymysql.return_value.cursor.return_value = mock.Mock()
        mock_fetchall.return_value = [{'kf': 1}, {'kf': 2}, {'kf': 3}, {'kf': 4}, {'kf': 5}]

        self.assertEqual(3, funcs.median('ri_cities', 'kf'))


if __name__ == "__main__":
    unittest.main()


# MyTestCase.testMedian()
