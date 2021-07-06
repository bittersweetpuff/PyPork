import main_fuzzy as fuzzy
import matplotlib.pyplot as plt


class MembershipTests:
    """
    This class is used for testing membership functions.
    """

    def __init__(self):
        """
        This method creates new instance of class.
        """

        print('Tests: membership')

    def triangle_test(self):
        """
        This function is used for testing triangle_membership function.

        Example
        ----------
        triangle_test()
        """

        fset = [5, 10, 12]
        values = [0, 1, 0]

        points = [4, 5, 8, 10, 11.6, 12, 16]
        memberships = []
        for p in points:
            memberships.append(fuzzy.triangle_membership(p, 5, 10, 12))

        plt.plot(fset, values)
        plt.plot(points, memberships, 'o')
        plt.title('Triangle membership function')
        plt.show()

    def trapezoid_test(self):
        """
        This function is used for testing trapezoid_membership function.

        Example
        ----------
        trapezoid_test()
        """

        fset = [1, 11, 14, 15]
        values = [0, 1, 1, 0]

        points = [0.5, 1, 5, 11, 12.3, 14, 14.07, 15, 22]
        memberships = []
        for p in points:
            memberships.append(fuzzy.trapezoid_membership(p, 1, 11, 14, 15))

        plt.plot(fset, values)
        plt.plot(points, memberships, 'o')
        plt.title('Trapezoid membership function')
        plt.show()

    def left_test(self):
        """
        This function is used for testing l_class_membership function.

        Example
        ----------
        left_test()
        """

        fset = [24, 30]
        values = [1, 0]

        points = [5, 24, 26, 30, 32]
        memberships = []
        for p in points:
            memberships.append(fuzzy.l_class_membership(p, 24, 30))

        plt.plot(fset, values)
        plt.plot(points, memberships, 'o')
        plt.title('L class membership function')
        plt.show()

    def right_test(self):
        """
        This function is used for testing y_class_membership function.

        Example
        ----------
        right_test()
        """

        fset = [24, 30]
        values = [0, 1]

        points = [5, 24, 26, 30, 32]
        memberships = []
        for p in points:
            memberships.append(fuzzy.y_class_membership(p, 24, 30))

        plt.plot(fset, values)
        plt.plot(points, memberships, 'o')
        plt.title('Y class membership function')
        plt.show()


membershipTests = MembershipTests()
membershipTests.triangle_test()
membershipTests.trapezoid_test()
membershipTests.left_test()
membershipTests.right_test()
