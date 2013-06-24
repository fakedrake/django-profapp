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

    def reverse_sort(self, arg):
        """
        True if reverse sorting.
        """
        return arg[0] == "-"


    def order_col(self, arg):
        """
        Return something order_by understands.
        """
        if self.reverse_sort(arg):
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
