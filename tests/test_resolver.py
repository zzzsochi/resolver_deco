from os.path import isdir
from sys import exit

import pytest

from resolver_deco import resolver


def test_resolver():
    @resolver('obj1', 'obj2')
    def func(obj1, ar, obj2=2, kw=3):
        return (obj1, ar, obj2, kw)

    res = func('os.path.isdir', 'str', obj2='sys.exit')
    assert res == (isdir, 'str', exit, 3)

    res = func(isdir, 'str', obj2=exit)
    assert res == (isdir, 'str', exit, 3)


def test_resolver_method():
    class Obj:
        @resolver('obj1', 'obj2')
        def meth(self, obj1, ar, obj2=2, kw=3):
            return (self, obj1, ar, obj2, kw)

    obj = Obj()

    res = obj.meth('os.path.isdir', 'str', obj2='sys.exit')
    assert res == (obj, isdir, 'str', exit, 3)

    res = obj.meth(isdir, 'str', obj2=exit)
    assert res == (obj, isdir, 'str', exit, 3)


def test_resolver__import_error():
    @resolver('obj')
    def func(obj):
        return (obj)

    with pytest.raises(ImportError):
        func('os.not_found')


def test_resolver__declare_error():
    with pytest.raises(ValueError):
        @resolver('not_exist')
        def func(app, obj):
            return (app, obj)
