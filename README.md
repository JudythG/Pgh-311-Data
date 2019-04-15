# Pgh-311-Data
Code to process Pittsburgh 311 data from [City of Pittsburgh 311 Data](https://data.wprdc.org/dataset/311-data).
Written for Python2 class at CCAC

## Files
### Code Files
* pgh311.py - main file to look at data from one column
* pgh2cols.py - main file to process data across two columns
* prompter_311.py - support file that allows user to choose an input file

### Input Files
* any *.csv file in the current directory is considered to be a PGH 311 input data file

## Running the applications
# pgh311.py
Running pgh311.py using python3 from a Terminal will display a list of *.csv files from the current directory.
Pick one to process by typing in the index number of a file.<br />
A list of column headers will be displayed.<br />
Pick one by typing in that column header. Case doesn't count. Status works as well as STATUS.<br />
A list of calls to each unique field under that column header will print to the terminal. <br />
Note: output displayed in reverse sort order by number of calls (most calls at top)<br />
Sample output (with only first few results):<br />
WARD 19  has 24845 calls<br />
WARD 14  has 22379 calls<br />
WARD 20  has 15831 calls<br />
WARD 16  has 12839 calls<br />

# pgh2cols.py
Running pgh2cols.py using python3 from a Terminal will display a list of *.csv files from the current directory.
Pick one to process by typing in the index number of a file.<br />
A list of column headers will be dsiplayed.<br />
Pick the first field by typing in a column header. As in the previous application, case does not count.<br />
Pick the second field by typing in a column header. <br />
Calls will be grouped by unique values of the first field and then unique values of the second field. <br />
Note: output displayed in reverse sort order by number of calls (most calls at top)<br />
Sample output (with only first few results):<br />
Abandoned Vehicle (parked on street)<br />
	Brighton Heights: count is 1<br />
	Marshall-Shadeland: count is 1<br />
Bridge Maintenance<br />
	Troy Hill: count is 1<br />
Curb /Broken/Deteriorated<br />
	Mount Washington: count is 1<br />
	Perry North: count is 1<br />
