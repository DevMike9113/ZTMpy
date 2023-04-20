import unittest

from main import do_stuff


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to run')

    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asfdsafd'
        result = do_stuff(test_param)
        # self.assertTrue(isinstance(result, TypeError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''what the h'''
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print('clean up')


if __name__ == '__main__':
    unittest.main()
