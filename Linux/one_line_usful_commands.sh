# read last line in file (you can change the number after "-n" to see last x rows)
tail -n1 -f <FILE_PATH/FILE_NAME>

# truncate a file 
truncate -s 0 <FILE_PATH/FILE_NAME>

# watch "top" for specific command
#example for <COMMAND_NAME> = python3
top -c -p $(pgrep -d',' -f <COMMAND_NAME>)

# look for file in folder path with a name like

# look for file name that start with "abc" from the current path
find . -name abc*

find <PATH / . > -type d -name "*<FOLDER-YOU-ARE-LOOKING>*" -print

# Ububtu - search for only installed packages using apt
example: sudo apt list -a --installed <PART-OF-PACKAGE-NAME>*
example: sudo apt list -a --installed libstdc++*
