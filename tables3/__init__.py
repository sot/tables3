__version__ = 0.1

def test(*args, **kwargs):
    """
    Run py.test unit tests.
    """
    import testr
    return testr.test(*args, **kwargs)


import tables
from distutils.version import LooseVersion

if LooseVersion(tables.__version__) < LooseVersion('3.0'):
    # alias some methods to their pytables3 names
    tables.open_file = tables.openFile

    tables.table.Table.read_where = tables.table.Table.readWhere
    tables.table.Table.get_where_list = tables.table.Table.getWhereList
    tables.table.Table.read_where = tables.table.Table.readWhere
    tables.table.Table.read_coordinates = tables.table.Table.readCoordinates
