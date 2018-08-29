#!/bin/bash
# Search python processes

key_word=$1

ps -efl | grep "$key_word" | awk  '!/bash|grep/ {print $4}'



