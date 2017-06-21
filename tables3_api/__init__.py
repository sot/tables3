import tables
from distutils.version import LooseVersion

__version__ = 0.1


def test(*args, **kwargs):
    """
    Run py.test unit tests.
    """
    import testr
    return testr.test(*args, **kwargs)


if LooseVersion(tables.__version__) < LooseVersion('3.0'):
    # alias some methods to their pytables3 names
    tables.open_file = tables.openFile

    tables.table.Table.read_where = tables.table.Table.readWhere
    tables.table.Table.get_where_list = tables.table.Table.getWhereList
    tables.table.Table.read_coordinates = tables.table.Table.readCoordinates
    tables.table.Table.modify_coordinates = tables.table.Table.modifyCoordinates
    tables.table.Table.remove_rows = tables.table.Table.removeRows

    tables.table.Column.create_csindex = tables.table.Column.createCSIndex
    tables.table.Column.create_index = tables.table.Column.createIndex

    tables.file.File.get_node = tables.file.File.getNode
    tables.file.File.create_table = tables.file.File.createTable
    tables.file.File.create_earray = tables.file.File.createEArray
    tables.file.File.copy_file = tables.file.File.copyFile
