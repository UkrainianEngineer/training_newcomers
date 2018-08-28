The purpose of this task is to realize a function which runs handlers for different file types, with an ability to run it in separate processes.
Implemented module recognizes the type of file from the file name and then generates the random file size for the corresponding extension. For each file name in list corresponding handler function runs in separate processes. The number of processes is defined in the configuration file.

