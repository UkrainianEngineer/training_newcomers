#!/bin/bash

# This script searches for running processes key_word pattern passed from command line
# ps command in combination with -efl options creates a table with information for each processes.
# After that, grep finds lines containing 'Skey_word' pattern, whitch is passed from command line.
# Finally awk prints colomn which corresponds to PID's, excluding lines which conatains 'bash' or 
# 'grep' to display only python processes.

key_word=$1

ps -efl | grep "$key_word" | awk  '!/bash|grep/ {print $4}'



