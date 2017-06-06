import tables
from .. import __init__ as tables3_api
import pytest


def test_tables_hasattrs():
    assert hasattr(tables, 'open_file')


@pytest.mark.parametrize('attr', ['read_where', 'get_where_list',
                                  'read_coordinates', 'modify_coordinates',
                                  'remove_rows'])
def test_table_Table_hasattrs(attr):
    assert hasattr(tables.table.Table, attr)


@pytest.mark.parametrize('attr', ['get_node', 'create_table'])
def test_file_File_hasattrs(attr):
    assert hasattr(tables.file.File, attr)

