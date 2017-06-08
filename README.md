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


