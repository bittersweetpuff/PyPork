import main_fuzzy as fuzzy


class OperatorsTests:
    """
    This class is used for testing F_OR, F_AND, F_NOT operators.

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

        print('Tests: F_OR, F_AND, F_NOT operators')

    def run_test(self, values):
        """
        This method runs single test.

        Parameters
        ----------
        values
            List of numerical values which have to be tested. Value between 0 to 1 (both included).

        Example
        ----------
        run_test([1, 0.5])
        """

        self.count += 1
        result = {
            'F_OR': fuzzy.F_OR(*values),
            'F_AND': fuzzy.F_AND(*values),
            'F_NOT': {
                "values[0]": fuzzy.F_NOT(values[0]),
                "values[1]": fuzzy.F_NOT(values[1])
            }
        }

        print('{} test {} {}'.format(
            self.heading_line, self.count, self.heading_line))
        print('values[0]: {}\nvalues[1]: {}'.format(
            values[0], values[1]))
        print('result: {}\n'.format(result))


operators_tests = OperatorsTests()
operators_tests.run_test([1, 0.5])
operators_tests.run_test([0.75, 0.1])
operators_tests.run_test([0.1, 0.4])
operators_tests.run_test([0.6, 1])
operators_tests.run_test([0.2, 0.3])
