The purpose of this task is to realize a function which runs handlers for different file types, with an ability to run these handlers in separate threads.
Implemented module recognizes the type of file from the file name and then generates the file size for this extension. For each file name in list corresponding handler function runs in separate threads. The number of threads is defined as a global variable in the program.

