# IMPORTING FROM MODULE
from mymodule import my_func
my_func()

# IMPORTING FROM A PACKAGE
from MyMainPackage import some_main_script

# IMPORTING FROM A SUBPACKAGE
from MyMainPackage.SubPackage import mysubscript

# SPECIFIC FUNCTIONS
# RUNNING THE FUNCTION FROM SOME_MAIN_SCRIPT
some_main_script.report_main()

# RUNNING FROM MYSUBSCRIPT
mysubscript.sub_report()
