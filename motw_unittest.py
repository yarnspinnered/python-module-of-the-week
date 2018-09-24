import unittest

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))

# setUp takes precedence over setUpClass
class SimpleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In setUpClass()')
        cls.good_range = 'Class setup good_range'

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')
        del cls.good_range

    def setUp(self):
        self.good_range = 'Instance setup good_range'
    def test_simple(self):
        print(self.good_range)
        a = 1
        b = 2
        self.assertNotEqual(a,b, 'Failure message here')

    @unittest.skipIf(3 > 2, 'reasons')
    def test_passing_is_based_on_absence_of_exceptions(self):
        return

    def test_assert_boolean(self):
        self.assertTrue(True)

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(1.0, 1.01, places = 1) # refers to decimal places

    @unittest.expectedFailure
    def test_list(self):
        self.assertListEqual(
            [1, 2, 3],
            [1, 3, 2],
        )

    def testCount(self):
        for i in range(3):
            with self.subTest('subtest msg'):
                self.assertCountEqual(
                [1, 3, 2, 2],
                [1, 2, 3, 2],
            )

    def testDict(self):
        self.assertDictEqual(
            {'a': 1, 'b': 2},
            {'a': 1, 'b': 2},
        )



    def testTuple(self):
        self.assertTupleEqual(
            (1, 'a'),
            (1, 'a'),
        )


    def testSet(self):
        self.assertIn(3, set([1, 2, 3]))

    def testAssertRaises(self):
        self.assertRaises(
            ValueError,
            raises_error,
            'a',
            b='c',
        )