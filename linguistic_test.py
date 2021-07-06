import main_fuzzy as fuzzy


class LinguisticTests:
    """
    This class is used for testing linguistic functions.

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

        print('Tests: linguistic')

    def run_add_new_pattern_test(self, pattern, value):
        """
        This method runs single test for add_new_pattern function.

        Parameters
        ----------
        pattern
            Linguistic value which has to be added.
        value
            Dictionary which describes linguistic value.

        Example
        ----------
        run_add_new_pattern_test('wzrost', {'niski': {'function': 'triangle', 'a': 130, 'b': 155, 'c': 165},'wysoki': {'function': 'triangle', 'a': 160, 'b': 180, 'c': 190}})
        """

        self.count += 1
        fuzzy.add_new_pattern(pattern, value)
        result = fuzzy.get_patterns_names()

        print('{} test {} {}'.format(
            self.heading_line, self.count, self.heading_line))
        print('pattern: {}\nvalue: {}'.format(
            pattern, value))
        print('result: {}\n'.format(result))

    def run_one_to_lingustic_test(self, pattern, value):
        """
        This method runs single test for one_to_linguistic function.

        Parameters
        ----------
        pattern
            Linguistic value.
        value
            Numerical value which has to be converted to linguistic value.

        Example
        ----------
        run_one_to_lingustic_test('wzrost', 170)
        """

        self.count += 1
        result = fuzzy.one_to_lingustic(pattern, value)

        print('{} test {} {}'.format(
            self.heading_line, self.count, self.heading_line))
        print('pattern: {}\nvalue: {}'.format(
            pattern, value))
        print('result: {}\n'.format(result))

    def run_list_to_linguistic_test(self, pattern, values):
        """
        This method runs single test for list_to_linguistic function.

        Parameters
        ----------
        pattern
            Linguistic value.
        value
            List of numerical values which have to be converted to linguistic values.

        Example
        ----------
        run_list_to_linguistic_test('wzrost', [110, 170])
        """

        self.count += 1
        result = fuzzy.list_to_lingustic(pattern, values)

        print('{} test {} {}'.format(
            self.heading_line, self.count, self.heading_line))
        print('pattern: {}\nvalue: {}'.format(
            pattern, values))
        print('result: {}\n'.format(result))


linguistic_tests = LinguisticTests()
linguistic_tests.run_one_to_lingustic_test('wzrost', 130)
linguistic_tests.run_one_to_lingustic_test('wzrost', 155)
linguistic_tests.run_one_to_lingustic_test('wzrost', 170)
linguistic_tests.run_one_to_lingustic_test('wzrost', 185)
linguistic_tests.run_one_to_lingustic_test('wzrost', 200)
linguistic_tests.run_one_to_lingustic_test('wiek', 5)
linguistic_tests.run_one_to_lingustic_test('wiek', 20)
linguistic_tests.run_one_to_lingustic_test('wiek', 50)
linguistic_tests.run_one_to_lingustic_test('wiek', 75)

linguistic_tests.run_list_to_linguistic_test('wzrost', [110, 170])
linguistic_tests.run_list_to_linguistic_test('wzrost', [190, 200])
linguistic_tests.run_list_to_linguistic_test('wiek', [8, 16])
linguistic_tests.run_list_to_linguistic_test('wiek', [20, 70])

new_pattern = {
    'niski': {
        'function': 'triangle',
        'a': 130,
        'b': 155,
        'c': 165
    },
    'wysoki': {
        'function': 'triangle',
        'a': 160,
        'b': 180,
        'c': 190
    }
}

linguistic_tests.run_add_new_pattern_test('new_pattern', new_pattern)
