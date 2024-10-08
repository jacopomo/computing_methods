import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
import unittest

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):

    def __init__(self, x, y):
        spline = InterpolatedUnivariateSpline(x, y)
        norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / norm
        self._spline = InterpolatedUnivariateSpline(self._x, self._y)
        super().__init__(self._x, self._y)

    def plot(self, show=True):
        """Plots the given points and the spline, after normalizing to 1
        show: Boolean that defines whether to show the plot or not. Default = True
        """
        plt.plot(self._x, self._y, 'o')
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self._spline(x))
        if show:
            plt.show()
        else: pass

    def normalization(self):
        """Calculates the integral of the spline on the defined domain
        """
        return self._spline.integral(self._x.min(), self._x.max())


    def normtest(self):
        """Test that makes sure that the normalization of the pdf is equal to one
        """
        self._spline.assertAlmostEqual(self.normalization(), 1)

class CumulativeDensityFunction(ProbabilityDensityFunction):
    """
    Class for calculating and handling the CDF.
    Inherits methods from ProbabilityDensityFunction, such as integration, plotting, and normalization.
    """

    def __init__(self, x, y):
        super().__init__(x, y)  # Calls the __init__ method of ProbabilityDensityFunction (normalizes, assigns self._x, etc)
        """Method for calculating the cumulative density function from a PDF
        """
        self._y=np.zeros(len(self._x))
        for i in range(0,len(self._x)):
            self._y[i] = self.integral(0,self._x[i])
        self._spline = InterpolatedUnivariateSpline(self._x,self._y)

    def cdftest(self):
        """Test that makes sure that the max of the cdf is equal to one
        """
        self.assertAlmostEqual(self._y.max(),1)



class ProbabilityDensityDistribution(CumilitiveDensityFunction):


    def __init__(self,x,y):



    def ppf(self):
        """Calculates the percent point function as the inverse of
        the cumulative density function
        """
        ccddff = CumulativeDensityFunction(self._x,self._y)
        self._ppfx = ccddff._y
        self._ppfy = ccddff._x
        return self._ppfx






if __name__ == '__main__':
    #unittest.main()
    x = np.linspace(0., 1., 5)
    y = np.array([1,2,3,2,1])
    pdf = ProbabilityDensityFunction(x, y)
    cdf = CumulativeDensityFunction(x,y)
