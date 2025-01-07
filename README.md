# tableau-datasource-refresh

## main.py
This script is used to initiate Tableau extracts by passing the datasource LUID like tableau_datasource_refresh.py XXXXXXXXXXXXXX. The primary use for this in from SQL Server by calling from SQL Job Agent CmdExec step. 

This is sample of format needed for SQL Server Job Agent Step:

*C:\ProgramData\Anaconda3\python.exe C:\Python\tableau\tableau_datasource_refresh.py 972a702c-dfc3-44d6-a2d3-22f3dc4b9f6f*
