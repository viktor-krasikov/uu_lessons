from pprint import pprint


def introspection_info(obj):
    return {"type": type(obj).__name__,
            'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
            'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
            'module': obj.__module__ if hasattr(obj, '__module__') else __name__
            }


number_info = introspection_info(42)
pprint(number_info, compact=True, sort_dicts=False)

pprint(introspection_info(introspection_info), compact=True, sort_dicts=False)


class MyClass:
    def __init__(self):
        self.my_attr = 0

    def my_method(self):
        self.my_attr = 99


pprint(introspection_info(MyClass()), compact=True, sort_dicts=False)
