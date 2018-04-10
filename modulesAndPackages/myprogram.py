"""
To import from package:
from MyMainPackage import some_main_script
"""

from mymodule import my_func

my_func()

from MyMainPackage import some_main_script
from MyMainPackage.subpackage import mysubscript

some_main_script.report_main()

mysubscript.sub_report()