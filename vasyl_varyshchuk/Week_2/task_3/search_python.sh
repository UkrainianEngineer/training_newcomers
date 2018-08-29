#!/bin/bash

# This script searches for running processes key_word pattern passed from the command line
# 'ps' command in combination with '-efl' options creates a table with information for each process.
# After that, 'grep' finds lines containing 'Skey_word' pattern, which is passed from the command line.
# Finally, 'awk' prints column which corresponds to PID's, excluding lines which contain 'bash' or 
# 'grep' to display only python processes.

key_word=$1

ps -efl | grep "$key_word" | awk  '!/bash|grep/ {print $4}'



