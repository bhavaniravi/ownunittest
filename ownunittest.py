import inspect


class AssertContextManger:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self, **kwargs):
        pass

    def __exit__(self, exc_type, exc_value, traceback, **kwargs):
        if not exc_type == self.exception:
            raise AssertionError(f"Expected {self.exception} got {exc_type}")
        else:
            return True


class SubTestContextManager:
    def __init__(self, **kwargs):
        pass

    def __enter__(self, **kwargs):
        pass

    def __exit__(self, exc_type, exc_value, traceback, **kwargs):
        pass


class TestCase:
    def __init__(self):
        self.setUpClass()
        self.setUp()

    def setUp(self):
        pass

    def assertEqual(self, x, y):
        assert x == y

    def assertRaises(self, exception):
        return AssertContextManger(exception)

    def subTest(self, **kwargs):
        return SubTestContextManager(**kwargs)


def main():
    success = {}
    failures = {}
    for subclass in TestCase.__subclasses__():
        members = inspect.getmembers(subclass)
        for member_name, member in members:
            # print(member_name, member)
            # print(callable(member))
            if member_name.startswith("test_"):
                print(f"running test {member_name}")
                cls_obj = subclass()
                try:
                    function_obj = getattr(cls_obj, member_name)()
                    success[member_name] = None
                except AssertionError as e:
                    failures[member_name] = e

    print(f"\n\n{len(success)} Succeeded")
    print(f"{len(failures)} Failed")
