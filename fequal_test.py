import main_fuzzy as fuzzy


class FequalTests:
    """
    This class is used for testing fequal function.

    Attributes
    ----------
    count
        Number of created tests, it is incremented each time when new test was completed. 
    heading_line
        String which contains character repeated 10 times.
    """

    count = 0
    heading_line = '=' * 10

    def __init__(self):
        """
        This method creates new instance of class.
        """

        print('Tests: fequal')

    def run_test(self, value1, fuzzy_level1, value2, fuzzy_level2):
        """
        This method runs single test.

        Parameters
        ----------
        value1
            First numerical value.
        value2
            Second numerical value.
        fuzzy_level1
            Fuzzy level for the first numerical value.
        fuzzy_level2
            Fuzzy level for the second numerical value.

        Example
        ----------
        run_test(3, 2, 10, 2)
        """

        self.count += 1
        result = fuzzy.fequal(value1, fuzzy_level1, value2, fuzzy_level2)

        print('{} test {} {}'.format(
            self.heading_line, self.count, self.heading_line))
        print('value1: {}\nfuzzy_level1: {}\nvalue2: {}\nfuzzy_level2: {}'.format(
            value1, fuzzy_level1, value2, fuzzy_level2))
        print('result: {}\n'.format(result))


fequal_tests = FequalTests()
fequal_tests.run_test(3, 2, 10, 2)
fequal_tests.run_test(2, 2, 5, 2)
fequal_tests.run_test(10, 6, 12, 1)
fequal_tests.run_test(10, 5, 10, 2)
fequal_tests.run_test(10, 5, 7, 2)
fequal_tests.run_test(5, 2, 2, 2)
fequal_tests.run_test(10, 2, 2, 2)
fequal_tests.run_test(5, 5, 6, 2)
fequal_tests.run_test(6, 2, 5, 5)
