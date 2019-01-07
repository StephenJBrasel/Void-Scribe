from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["data/*"]

setup(name = "void_scribe",
    version = "0.1",
    description = "Stephans Stuff",
    author = "Stphan Brasel",
    author_email = "machinelearningmadlads@gmail.com",
    url = "whatever",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['void_scribe'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'void_scribe' : files }
    #'runner' is in the root.
    #scripts = ["runner"],
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 