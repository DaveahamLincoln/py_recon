py_recon
========

.CSV Reconciliation tool
developed by Dave Nearing III, Temporary Agent, 06/14/13
source code hosted at https://github.com/DaveahamLincoln/py_recon
Use by parties other than FRCC employees is restricted without prior consent granted by the FRCC Controller

About
--------
py_recon is a tool which compares a pair of two-column .CSV files and returns a file containing a list of differences.

Prepping .CSVs For Use With py_recon
--------
1. Open up the Excel spreadsheet containing the data you wish to reconcile.

2. Copy the columns containing the names and amounts for the first set of data to a new sheet.\

3. Delete the header.

4. Delete all blank lines.  To do this, 
    >Press Ctl+A.
    > Press Ctl+G.
	> Click “Special…”
	> Select the “Blanks” radio button and click “OK.”
	> Right click a highlighted cell and select “Delete…”
	> Select “Entire Row” and click “OK.”

5. Save the sheet as a .CSV file.  To do this, 
    > Select “File,” then “Save As.”
	> Select “CSV (comma delimited)” from the “Save as type” drop-down menu.
	> Change the name of the file to something easy to remember and type, like “SetA.”
	> Click “Save.”
	> An error prompt should appear:
 	> Click “OK.”
	> An error prompt should appear:
 	> Click “OK.”

6. Repeat steps 2-5 for the second set of data.  Two things to look out for:
* It is very important that the names of the companies are in column A and the amounts to be reconciled are column B, so you might have to copy the columns one at a time to the second spreadsheet.
* It is very important that you save the second set of data with a different name than the first set.

7. Check to make sure your .CSVs are properly formatted.  To do this:
	> Open the folder where you saved your .CSVs
	> Right click the first one, select “Open with,” and pick “Notepad.”
    > Make sure that each pair is separated by one comma and that there aren’t any extra commas 
      on the end of each line.  If there are extra commas, it means that Excel exported empty columns to the .CSV.  To fix this, re-export the file after copying each column to the new sheet one at a time, rather than two at a time.
    > Make sure that there are no lines consisting of one comma.  If there are, that means a blank row was not deleted.  Re-export the file, paying special attention to step 4.
    > Check your other .CSV.  If both .CSVs are properly formatted, move on to step 8.

8.  Open the folder you’re working in in the command line.  To do this:
    > Press “Shift+Menu+W+Enter.”  “Menu” is the key next to the right-hand Windows button on 
      your keyboard.

9. Run py_recon on your .CSVs.  To do this:
    > Type “python3 pyrecon.py”
	> Type the name of your first CSV, i.e. “SetA.csv”
	> Type the name of your second CSV, i.e. “SetB.csv”
	> Type the name of the log file you’d like py_recon to create for you, e.x. “Output.txt”
    > Your cmd window should read "python3 pyrecon.py SetA.csv SetB.csv Output.txt"
    > Press “Enter.”
    > When py_recon has finished reconciling your .CSV files, a message will appear on the screen that says “Reconciliation has been logged to <your log name>.”  At this point it is safe to exit the cmd window.

10. At this point you can open/print your log file.
    This log contains all items whose names appear in both columns and whose amounts do not match.   Items which only exist in one column are not logged.

11. If the log is a jumbled mess, open it in WordPad instead of Notepad.