import numpy as np
def Simpson(function, a, b, N):
    '''
    Parameters
    ----------
    function : function of a single variable
    a, b     : interval of integration [a,b]
    N        : number of subintervals of [a,b]
    

    Returns
    ----------
    Approximation of the integral of f(x) from a to b using the
        Simpson rule with N subintervals of equal length.

    Examples
    ----------
    >>> Simpson(lambda x: x**4 - 2*x + 1, 0.0, 2.0, 10)
    4.50656
    >>> Simpson(lambda x: x**4 - 2*x + 1, 0.0, 2.0, 1000)
    4.40001066667
    >>> Simpson(lambda x: np.sin(x), 0.0, 2.0, 10)
    1.4161463644981664
    '''
    h = (b - a)/N
    s = 0.5*function(a) + 0.5*function(b)
    for k in range(1, N):
        s += function(a+k*h)
    return h*s



