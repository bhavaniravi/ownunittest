import inspect
import pytest
from ownunittest import TestCase


class CustomTestCollector(pytest.Class):
    def collect(self):
        items = list(self.obj.__dict__.items())
        for fn_name, fn_obj in items:
            if callable(fn_obj) and fn_name.startswith("test_"):
                yield self.makeitem(name=fn_name, func=fn_obj)

    def makeitem(self, func, name):
        return pytest.Function.from_parent(parent=self, name=name, fobj=func)


@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector, name, obj):
    print(collector, name, obj)
    if inspect.isclass(obj) and issubclass(obj, TestCase):
        return CustomTestCollector.from_parent(collector, name=name, obj=obj)
