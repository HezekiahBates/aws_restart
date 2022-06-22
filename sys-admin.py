import os 
import subprocess
#exercise 1 showing current directory files/folders
#os.system("ls");
#exercise 2 using subprocess.run
#subprocess.run(["ls"]);
#exercise 3 using subprocess.run with two arguments 
#subprocess.run(["ls", '-l']);
#exercise 4 using subprocess.run with three arguments 
#subprocess.run(["ls", "-l", "README.md"])
#exercise 5 retrieving system info
"""
command = "uname";
commandArguments = "-a";
print(f'Gathering system information with command: {command} {commandArguments}');
subprocess.run([command, commandArguments]);
"""
#exercise 6 Retrieving information about disk space
command = "ps";
commandArguments = "-x";
print(f'Gathering active process information with command: {command} {commandArguments}');
subprocess.run([command, commandArguments]);