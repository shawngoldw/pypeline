class Pype:
    def __init__(self, raw):
        self.raw = raw
        self.transformed = self.raw.copy()
        self._transforms = []

    def add(self, func, params=None):
        if type(func) is _Container:
            params = func.params
            func = func.func
        self._transforms.append({'f': func, 'p': params})
        self.transformed = self._apply(self.transformed, self._transforms[-1])

    def transform(self, data):
        for t in self._transforms:
            data = self._apply(data, t)
        return data

    def _apply(self, data, transform):
        f = transform['f']
        p = transform['p']

        if p is None:
            return f(data)
        else:
            return f(data, **p)


class _Container:
    def __init__(self, func, params=None):
        self.func = func
        self.params = params