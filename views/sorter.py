class Sorter(object):
    """
    Tell the query how to sort.
    """

    def __init__(self, *args, **kwargs):
        """
	Tell me what to match
	"""
        self.default = kwargs['default']
        self.columns = set(list(args) + kwargs.values())
        self.mapping = kwargs

    def order_col(self, arg):
        """
        Return something order_by understands.
        """
        if arg[0] == "-":
            col = arg[1:]
            tmpl = "-%s"
        else:
            col = arg
            tmpl = "%s"

        try:
            col = self.mapping[col]
        except KeyError:
            pass

        if col in self.columns:
            return tmpl % col
        else:
            return self.default
