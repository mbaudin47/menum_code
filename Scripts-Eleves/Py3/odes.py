# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
A module to solve ordinary differential methods with simple methods.

Reference
---------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import sys


def euler(f, tspan, y0, h, *args):
    """
    Solves an ODE with Euler's method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    with Euler's method.

    The calling sequence of f must be

    ydot = f(t, y)

    where t is the current time, y is the current state
    and ydot is dy/dt.

    If the function f requires extra-arguments, the args input
    argument can be used.
    In this case, the calling sequence of f must be:

    ydot = f(t, y, *args)

    Parameters
    ----------
    f : function
        the right-hand side of the ODE
    tspan : np.array, shape(2)
        The initial tspan[0] and final tspan[1] times
    y0 : np.array
        The initial state
    h : float
        The time step.
    args : list
        Extra arguments of the function f.

    Returns
    -------
    tout : np.array(n)
        The times, where n is the number of steps
    yout : np.array(n, d)
        The solution at each time.
        The variable yout[i, j] contains the j-th component of the solution at the
        i-th time step, for i=0, 1, ..., n - 1 and j=0, 1, ..., d - 1,
        where n is the number of time steps and d is the dimension of the state.

    Examples
    --------
    >>> import numpy as np
    >>> def harmosc(y, t):
    >>>     ydot = np.array([y[1], -y[0]])
    >>>     return ydot
    >>>
    >>> y0 = [1.0, 00]
    >>> tspan = [0.0, 2 * pi]
    >>> h = 0.001
    >>> tout, yout = euler(harmosc, tspan, y0, h)

    The solution at t=tfinal is:

    >>> yfinal = yout[-1, :]

    """
    t0 = tspan[0]
    tfinal = tspan[1]
    t = t0
    y = y0
    tout = np.array(t0)
    yout = np.array(y0)
    while t < tfinal:
        h = min(h, tfinal - t)
        y = y + h * f(y, t, *args)
        t = t + h
        tout = np.vstack([tout, t])
        yout = np.vstack([yout, y])
    return tout, yout


def bogacki_shampine(f, tspan, y0, atol=1.0e-6, verbose=False, *args):
    """
    Solve differential equations with Bogacki and Shampine method.

    Solves the system of differential equations

        dy/dt = f(t,y)
        y(t0) = y0

    from t = t0 to tfinal.

    The calling sequence of f must be

    ydot = f(t, y)

    where t is the current time, y is the current state
    and ydot is dy/dt.

    If the function f requires extra-arguments, the args input
    argument can be used.
    In this case, the calling sequence of f must be:

    ydot = f(t, y, *args)

    This function uses the Runge-Kutta (2,3) method of Bogacki and Shampine.

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    tspan : np.array(2)
        The initial tspan[0] and final tspan[1] times
    y0 : np.array(d)
        The initial state
    atol : float
        The absolute tolerance (default = 1.e-6)
    verbose : bool
        Set to True to print intermediate messages.
    args : list
        Extra arguments of the function f.

    Returns
    -------
    tout : np.array(n)
        The times, where n is the number of steps.
    yout : np.array(n, d)
        The solution at each time.
        The variable yout[i, j] contains the j-th component of the solution at the
        i-th time step, for i=0, 1, ..., n - 1 and j=0, 1, ..., d - 1,
        where n is the number of time steps and d is the dimension of the state.

    Examples
    --------
    >>> import numpy as np
    >>> def harmosc(y, t):
    >>>     ydot = np.array([y[1], -y[0]])
    >>>     return ydot
    >>>
    >>> y0 = [1.0, 00]
    >>> tspan = [0.0, 2 * pi]
    >>> h = 0.001
    >>> tout, yout = bogacki_shampine(harmosc, tspan, y0)

    The solution at t=tfinal is:

    >>> yfinal = yout[-1, :]

    Bibliography
    ------------
    Przemyslaw Bogacki et Lawrence F. Shampine. « A 3(2) pair
    of Runge-Kutta formulas ». In : Applied Mathematics Letters
    2.4 (1989), p. 321-325.
    """

    # Initialize variables.
    t0 = tspan[0]
    tfinal = tspan[1]
    hmin = 16.0 * sys.float_info.epsilon * tfinal
    t = t0
    y = y0

    # Safeguards for the time step management
    step_safety_factor = 0.8
    step_maximum_factor = 4.0

    # Initialize output.
    tout = [t0]
    yout = y0

    # Initial slope
    s1 = f(y, t, *args)

    # Initialize step size to the largest possible step length
    h = 0.1 * (tfinal - t0)

    # Main loop.
    while t < tfinal:
        if verbose:
            print("t=%.4f, h=%.4e" % (t, h))

        h = min(h, tfinal - t)  # Change le dernier pas

        # Attempt a step.
        s2 = f(y + h / 2 * s1, t + h / 2, *args)
        s3 = f(y + 3 * h / 4 * s2, t + 3 * h / 4, *args)
        tnew = t + h
        ynew = y + h * (2 * s1 + 3 * s2 + 4 * s3) / 9
        s4 = f(ynew, tnew, *args)

        # Estimate the error.
        e = h * (-5 * s1 + 6 * s2 + 8 * s3 - 9 * s4) / 72
        err = np.linalg.norm(e, np.inf)

        # Accept the solution if the estimated error
        # is less than the tolerance.
        if err <= atol:
            if verbose:
                print("    Accept step")
            t = tnew
            y = ynew
            tout.append(t)
            yout = np.vstack([yout, y])
            # Reuse final function value to start new step.
            s1 = s4
        else:
            if verbose:
                print("    Reject step")

        # Compute a new step size.
        step_candidate_factor = (atol / err) ** (1.0 / 3.0)
        step_corrected_factor = min(
            step_maximum_factor, step_safety_factor * step_candidate_factor
        )
        if verbose:
            print("    h_factor = %.3f" % (step_corrected_factor))
        h = h * step_corrected_factor

        # If step size is too small, stop.
        if h <= hmin:
            raise ValueError(u"Step size %e too small at t = %e.\n" % (h, t))

    return tout, yout


def ode_plot(t, y, title="", mark="-+"):
    """
    Make a plot of the ODE.

    Create a matrix of ndim-by-1 plots.
    In the i-th plot, the first coordinate is the time and
    the second coordinate is y[:,i].

    Parameters
    ----------
    t : np.array(n)
        The times, where n is the number of time steps.
    y : np.array(n, d)
        The solution, where d is the number of dimensions.
    title : str
        The title of the plot (default title="").
    mark : str
        The mark for the plot (default mark="-o")

    Returns
    -------
    None

    Examples
    --------
    >>> import numpy as np
    >>> def harmosc(y, t):
    >>>     ydot = np.array([y[1], -y[0]])
    >>>     return ydot
    >>>
    >>> y0 = [1.0, 00]
    >>> tspan = [0.0, 2 * pi]
    >>> h = 0.001
    >>> tout, yout = bogacki_shampine(harmosc, tspan, y0)
    >>> ode_plot(tout, yout)

    """
    ndim = y.shape[1]
    pl.figure()
    for i in range(ndim):
        ax = pl.subplot(ndim, 1, i + 1)
        if i == ndim - 1:
            pl.xlabel(u"Temps (s)")
        pl.plot(t, y[:, i], mark)
        if i == 0:
            pl.title(title)
        if i < ndim - 1:
            ax.set_xticks([])
        pl.ylabel(u"y[%d]" % (i))
    return


def adams_bashforth(f, tspan, y0, h, *args):
    """
    Solves an ODE with Adams-Bashforth (2) method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    with Adams-Bashforth (2)'s method, except for the first
    and the last steps.

    * The first step cannot be implemented with AB2, since
    the previous slope is required.

    * The last step cannot be implemented with AB2, since
    the step size must be reduced to compute the
    solution at tfinal.

    The calling sequence of f must be

    ydot = f(t, y)

    where t is the current time, y is the current state
    and ydot is dy/dt.

    If the function f requires extra-arguments, the args input
    argument can be used.
    In this case, the calling sequence of f must be:

    ydot = f(t, y, *args)

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    tspan : np.array(2)
        The initial (tspan[0]) and final (tspan[1]) times
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    tout : np.array(n)
        The times, where n is the number of steps
    yout : np.array(n, d)
        The solution at each time.
        The variable yout[i, j] contains the j-th component of the solution at the
        i-th time step, for i=0, 1, ..., n - 1 and j=0, 1, ..., d - 1,
        where n is the number of time steps and d is the dimension of the state.

    Examples
    --------
    >>> import numpy as np
    >>> def harmosc(y, t):
    >>>     ydot = np.array([y[1], -y[0]])
    >>>     return ydot
    >>>
    >>> y0 = [1.0, 00]
    >>> tspan = [0.0, 2 * pi]
    >>> h = 0.001
    >>> tout, yout = adams_bashforth(harmosc, tspan, y0, h)

    The solution at t=tfinal is:

    >>> yfinal = yout[-1, :]

    Bibliography
    ------------
    Randall J. Leveque. Finite Difference Methods for Ordinary
    and Partial Differential Equations. SIAM, 2007.
    p.131.

    David F. Griffiths et Desmond J. Higham. Numerical Methods for ODEs.
    Springer, 2010. p.45

    Walter Gautschi. Numerical Analysis, Second Edition. Birkhäuser, 2012.
    p.405.
    """
    t0 = tspan[0]
    tfinal = tspan[1]
    t = t0
    y = y0
    tout = np.array(t0)
    yout = np.array(y0)
    # Initalize first step
    s1 = f(y, t, *args)
    s0 = f(y + h * s1, t + h, *args)  # Use Heun for first step
    y = y + 0.5 * h * (s0 + s1)
    t = t + h
    tout = np.vstack([tout, t])
    yout = np.vstack([yout, y])
    while t < tfinal:
        if t + h > tfinal:
            # Use Heun for last step
            h = tfinal - t
            s1 = f(y, t, *args)
            s0 = f(y + h * s1, t + h, *args)
            y = y + 0.5 * h * (s0 + s1)
            t = t + h
        else:
            # Use AB2
            s0 = f(y, t, *args)
            y = y + 0.5 * h * (3 * s0 - s1)
            t = t + h
            s1 = s0
        tout = np.vstack([tout, t])
        yout = np.vstack([yout, y])
    return tout, yout


def explicit_method(name, f, tspan, y0, h, *args):
    """
    Solves an ODE with an explicit numerical method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    with a numerical method.

    The calling sequence of f must be

    ydot = f(t, y)

    where t is the current time, y is the current state
    and ydot is dy/dt.

    If the function f requires extra-arguments, the args input
    argument can be used.
    In this case, the calling sequence of f must be:

    ydot = f(t, y, *args)

    Parameters
    ----------
    name : str
        The name of the algorithm : "euler", "heun", "rk2", "rk4", "ralston"
    f : function
        The right-hand side of the ODE
    tspan : np.array(2)
        The initial (tspan[0]) and final (tspan[1]) times
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    tout : np.array(n)
        The times, where n is the number of steps.
    yout : np.array(n, d)
        The solution at each time.
        The variable yout[i, j] contains the j-th component of the solution at the
        i-th time step, for i=0, 1, ..., n - 1 and j=0, 1, ..., d - 1,
        where n is the number of time steps and d is the dimension of the state.

    Examples
    --------
    >>> import numpy as np
    >>> def harmosc(y, t):
    >>>     ydot = np.array([y[1], -y[0]])
    >>>     return ydot
    >>>
    >>> y0 = [1.0, 00]
    >>> tspan = [0.0, 2 * pi]
    >>> h = 0.01
    >>> tout, yout = explicit_method("euler", harmosc, tspan, y0, h)

    This function can be used to compare several methods.

    >>> for name in ("euler", "heun", "rk2", "rk4", "ralston"):
    >>>     tout, yout = explicit_method(name, harmosc, tspan, y0, h)
    """
    options = {
        "euler": _euler_step,
        "rk2": _rk2_step,
        "rk4": _rk4_step,
        "ralston": _ralston_step,
        "heun": _heun_step,
    }
    t0 = tspan[0]
    tfinal = tspan[1]
    t = t0
    y = y0
    tout = np.array(t0)
    yout = np.array(y0)
    tout = np.vstack([tout, t])
    yout = np.vstack([yout, y])
    step = options[name]
    while t < tfinal:
        h = min(h, tfinal - t)
        y = step(f, t, y, h, *args)
        t = t + h
        tout = np.vstack([tout, t])
        yout = np.vstack([yout, y])
    return tout, yout


def _ralston_step(f, t0, y0, h, *args):
    """
    Performs a single step of Ralston method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    at t = t0 + h.

    Used by explicit_method.

    Ralston's method has order 3.

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    t0 : float
        The initial time.
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    y : np.array(d)
        The solution at time t + h.

    Bibliography
    ------------
    Ralston, Anthony (1965), A First Course in Numerical Analysis, New York: McGraw-Hill.
    """
    s1 = f(y0, t0, *args)
    s2 = f(y0 + 0.5 * h * s1, t0 + 0.5 * h, *args)
    s3 = f(y0 + 0.75 * h * s2, t0 + 0.75 * h, *args)
    y = y0 + h * (2 * s1 + 3 * s2 + 4 * s3) / 9.0
    return y


def _rk4_step(f, t0, y0, h, *args):
    """
    Performs a single step of Runge-Kutta 4 method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    at t = t0 + h.

    Used by explicit_method.

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    t0 : float
        The initial time.
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    y : np.array(d)
        The solution at time t + h.
    """
    s1 = f(y0, t0, *args)
    s2 = f(y0 + 0.5 * h * s1, t0 + 0.5 * h, *args)
    s3 = f(y0 + 0.5 * h * s2, t0 + 0.5 * h, *args)
    s4 = f(y0 + h * s3, t0 + h, *args)
    y = y0 + h * (s1 + 2 * s2 + 2 * s3 + s4) / 6.0
    return y


def _rk2_step(f, t0, y0, h, *args):
    """
    Performs a single step of Runge-Kutta 2 method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    at t = t0 + h.

    Used by explicit_method.

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    t0 : float
        The initial time.
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    y : np.array(d)
        The solution at time t + h.
    """
    s1 = f(y0, t0, *args)
    s2 = f(y0 + 0.5 * h * s1, t0 + 0.5 * h, *args)
    y = y0 + h * s2
    return y


def _heun_step(f, t0, y0, h, *args):
    """
    Performs a single step of Heun method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    at t = t0 + h.

    Used by explicit_method.

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    t0 : float
        The initial time.
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    y : np.array(d)
        The solution at time t + h.
    """
    s1 = f(y0, t0, *args)
    s2 = f(y0 + h * s1, t0 + h, *args)
    y = y0 + 0.5 * h * (s1 + s2)
    return y


def _euler_step(f, t0, y0, h, *args):
    """
    Performs a single step of Euler method.

    Solves the ODE :

        dy/dt = f(t, y(t))
        y(0) = y0

    at t = t0+h.

    Used by explicit_method.

    Parameters
    ----------
    f : function
        The right-hand side of the ODE
    t0 : float
        The initial time.
    y0 : np.array(d)
        The initial state
    h : float
        The time step

    Returns
    -------
    y : np.array(d)
        The solution at time t + h.
    """
    s1 = f(y0, t0, *args)
    y = y0 + h * s1
    return y


if __name__ == "__main__":

    def harmosc(y, t):
        ydot = np.array([y[1], -y[0]])
        return ydot

    # Exact solution
    y0 = [1.0, 0.0]
    tspan = [0.0, 2 * np.pi]
    t = tspan[1]
    yexact = np.array([np.cos(t), -np.sin(t)])
    print(u"Exact:", yexact)

    # 1. Check Euler
    print(u"1. Check Euler")
    h = 0.001
    tout, yout = euler(harmosc, tspan, y0, h)
    y = yout[-1, :]
    niter = tout.shape[0]
    np.testing.assert_allclose(tout[-1], tspan[1])
    print(u"Euler:", y, ", N iterations:", niter)
    np.testing.assert_allclose(y, yexact, atol=1.0e-2)

    # 2. Check bogacki_shampine
    print(u"")
    print(u"2. Check bogacki_shampine")
    tout, yout = bogacki_shampine(harmosc, tspan, y0)
    y = yout[-1, :]
    niter = len(tout)
    print(u"bogacki_shampine:", y, ", N iterations:", niter)
    # Exact solution
    np.testing.assert_allclose(tout[-1], tspan[1])
    np.testing.assert_allclose(y, yexact, atol=1.0e-2)

    ode_plot(tout, yout)

    # 3. Check adams_bashforth
    print(u"")
    print(u"3. Check adams_bashforth")
    h = 0.01
    tout, yout = adams_bashforth(harmosc, tspan, y0, h)
    y = yout[-1, :]
    niter = tout.shape[0]
    print(u"AB2:", y, ", N iterations:", niter)
    np.testing.assert_allclose(tout[-1], tspan[1])
    np.testing.assert_allclose(y, yexact, atol=1.0e-2)

    # 4. Check euler, heun, rk2, ralston, rk4
    print(u"")
    print(u"4. Check explicit_method:")
    h = 0.01
    for name in ("euler", "heun", "rk2", "ralston", "rk4"):
        tout, yout = explicit_method(name, harmosc, tspan, y0, h)
        y = yout[-1, :]
        niter = tout.shape[0]
        absolute_error = np.linalg.norm(y - yexact)
        print(name, ":", y, ", Abs.Err.:", absolute_error)
        assert absolute_error < 1.0e-1
