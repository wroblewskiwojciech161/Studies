from inspect import getfullargspec

dictionary={}
class Function(object):
  """Function is a wrap over standard python function.
  """
  def __init__(self, fn):
    self.fn = fn

    def key(self, args=None):
        """Returns the key that will uniquely identify
        a function (even when it is overloaded).
        """
        # if args not specified, extract the arguments from the
        # function definition
        if args is None:
            args = getfullargspec(self.fn).args

        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
        ])

  def __call__(self, *args, **kwargs):
    """when invoked like a function it internally invokes
    the wrapped function and returns the returned value.
    """
    fn = dictionary.get()


    # invoking the wrapped function and returning the value.
    return fn(*args, **kwargs)


def overload(fn):
    func=Function(fn)
    dictionary[func.key]=func
    return

@overload
def area(l, b):
  return l * b
func = Function(area)
dictionary.get()
print(area(2,3))