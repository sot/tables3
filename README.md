tables3_api is a package to "monkey-patch" tables (pytables) versions before
version 3.  Importing tables3_api patches pytables < 3 in place to support the pytables
version 3 PEP8-compliant API.

The point of this package is to let users patch their code now to support the pytables3 API, and
provide this monkey-patch compatibility module with code that gets called *only* if the
code is being run with pytables2.  This lets the same code run in both pytables2 and
pytables3 environments, which is very helpful for testing and migrating code.

So the update process for a package is then to:

* Get in to an environment with pytables3 to have access to the pt2to3 script from
  pytables >= 3.0.
* Change into the git repository for a package that should be updated.
* Run the pt2to3_all script found in this project.
* For each source .py file that has changes due to pt2to3, also add "import tables3_api"
  after "import tables".
* Check in changes.
* Test in pytables2 and pytables3 environments.

To put this in context, if you had code that looked like this
```
import tables
def read_table(file):
    h5 = tables.openFile(file)  # openFile is pytables2 old method name
    return h5.root.data[:]
```
after running pt2to3_all, the file would look like this
```
import tables
def read_table(file):
    h5 = tables.open_file(file)  # new pytables3 API 
    return h5.root.data[:]
```
and the user should edit it to add the "import tables3_api" line:
```
import tables
import tables3_api
def read_table(file):
    h5 = tables.open_file(file)
    return h5.root.data[:]
```

Now, if the code is called from an environment with pytables3, tables.open_file is the correct name for that method and it just works.  If the code is called from an environment with pytables2, the "import tables3_api" method did this assignment behind the scenes:
```
tables.open_file = tables.openFile
```
so the native pytables2 method to open the file has been aliased to "open_file" so the code will run fine then as well.


