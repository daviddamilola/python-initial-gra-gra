import inspect
import itertools
import reprlib
from turtle import width

def dump(obj):
    print("Type")
    print("=======")
    print(type(obj))
    print()

    print("Documentation")
    print("===============")
    print(inspect.getdoc(obj))
    print()

    all_attr_names = set(dir(obj))
    method_names = set(filter(lambda attr_name: callable(getattr(obj, attr_name)), all_attr_names))
    assert method_names <= all_attr_names
    attr_names = all_attr_names - method_names
    print("Attributes")
    print("===============")
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name))) for name in attr_names]
    print_table(attr_names_and_values, "Name", "Values")
    print()
    print("Methods")
    print("===============")
    # TODO
    methods = (getattr(obj, method_name) for method_name in method_names)
    method_names_and_doc = sorted((full_sig(method), breif_doc(method)) for method in methods)
    print_table(method_names_and_doc, "Name", "Description")
    print()


def full_sig(method):
    try:
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + '(...)'

def breif_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            return lines[0]
    return ''

def print_table(rows_of_cloumns, *headers):
    num_columns = len(rows_of_cloumns[0])
    num_headers = len(headers)
    if len(headers) != num_columns:
        raise TypeError("Expected {} header arguments, "
        "got {}".format(num_columns, num_headers)
        )
    rows_of_cloumns_with_header = list(itertools.chain([headers], rows_of_cloumns))
    print(rows_of_cloumns_with_header)
    columns_of_rows=list(zip(*rows_of_cloumns_with_header))
    column_widths = [max(map(column, len)) for column in columns_of_rows]
    column_specs = ('{{:{w}}}'.format(w=width) for width in column_widths)
    format_spec = ' '.join(column_specs)
    print(format_spec.format(*headers))
    rules = ('-' * width for width in column_widths)
    print(format_spec.format(*rules))
    for row in rows_of_cloumns:
        print(format_spec.format(*row))


dump(dir)