0-current_working_directory contains a script to print the absolute path name of the current working directory.

1-listit contains a script to display the conents list of the current directory.

2-bring_me_home contains a script that changes the working directory to the user's home directory.

3-listfiles contains a script to display current directory contents in a long format.

4-listmorefiles contains a script to display current directory contents, including hidden files (starting with .), while also using the long format.

5-listfilesdigitonly contains a script to display current directory contents:
- in long format
- with user and group IDs displayed numerically
- and hidden files (starting with .)

6-firstdirectory contains a script that creates a directory named my_first_directory in the /tmp/ directory.

7-movethatfile contains a script to move the file betty from /tmp/ to /tmp/my_first_directory.

8-firstdelete contains a script to delete the file betty from /tmp/my_first_directory/

9-firstdirdeletion contains a script to delete the my_first_directory that is in the /tmp directory

10-back contains a script to change the working directory to the previous one.

11-lists contains a script that lists all files (even ones with names beginning with a period) in the current directory and the parent working directory and the /boot directory (in this order), in long format.

12-file_type contains a script that prints the type of the file named 'iamafile' in the /tmp directory.

13-symbolic_link contains a script that creates a symbolic link to /bin/ls in the working directory.

14-copy_html contains a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

100-lets_move contains a script that moves all files beginning with an uppercase letter to the director /tmp/u.

101-clean_emacs contains a script that deletes all files in the current working directory that end with the character ~.

102-tree contains a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory. Only two spaces and lines allowed, not more.

103-commas contians a script that lists all the files and directories of the current directory, separated by commas:
- Directory names end with a slash /
- Files and directories starting with a . are listed
- The listing is alpha ordered, except for the directories . and .. which are listed at the very beginning
- Only digits  and letters are used to sort: Digits come first
- The listing ends with a new line

school.mgc is a magic file that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
