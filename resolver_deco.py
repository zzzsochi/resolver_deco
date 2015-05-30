import inspect

from zope.dottedname.resolve import resolve


def resolver(*for_resolve, attr_package='__package_for_resolve_deco__'):
    """ Resolve dotted names in function arguments

    Usage:

        >>> @resolver('obj')
        >>> def func(param, obj):
        >>>     assert isinstance(param, str)
        >>>     assert not isinstance(obj, str)
        >>>
        >>> func('os.path', 'sys.exit')
    """
    def decorator(func):
        spec = inspect.getargspec(func).args
        if set(for_resolve) - set(spec):
            raise ValueError('bad arguments')

        def wrapper(*args, **kwargs):
            args = list(args)

            if args and attr_package:
                package = getattr(args[0], attr_package, None)
            else:
                package = None

            for item in for_resolve:
                n = spec.index(item)
                if n >= len(args):
                    continue

                if n is not None and isinstance(args[n], str):
                    args[n] = resolve(args[n], package)

            for kw, value in kwargs.copy().items():
                if kw in for_resolve and isinstance(value, str):
                    kwargs[kw] = resolve(value, package)

            return func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__annotations__ = func.__annotations__

        return wrapper

    return decorator
