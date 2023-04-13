0-iam_betty contains a script that switches the current user to the user betty.

1-who_am_i contains a script that prints the effective username of the current user.

2-groups contains a script that prints all the groups the current user is part of.

3-new_owner contains a script that changes the owner of the file /tmp/hello to the user betty.

4-empty contains a script that creates an empty file called hello.

5-execute contains a script that adds execute permission to the owner of the file hello (in the working directory).

6-multiple_permissions contains a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody contains a script that adds execution permission to the owner, the group owner and the other users, to the file hello (in the working directory). No commas allowed!

8-James_Bond contains a script that sets the permission to the file hello (in the working directory) as follows:
- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions.
No commas allowed!

9-John_Doe contains a script that sets the mode of the file hello (in the working directory) to '-rwxr-x-wx'.

10-mirror_permissions contains a script that sets the mode of the file 'hello' to the same as 'olleh's mode. Both files are in the working directory.

11-directories_permissions contains a script that adds execute permission to all subdirectories of the **current directory** for the owner, the group owner and all other users.

12-directory_permissions contains a script that creates a directory called 'my_dir' with permissions 751 in the working directory.

13-change_group contains a script that changes the group owner to 'school' for the file 'hello' in the working directory.

100-change_owner_and_group contains a script that changes the owner to 'vincent' and the group owner to 'staff' for all the files and directories in the working directory.

101-symbolic_link_permissions contains a script that changes the owner and the group owner of '\_hello' (a symbolic link in the working directory) to 'vincent' and 'staff' respectively.

102-if_only contains a script that changes the owner of the file 'hello' (in the working directory) to 'betty' only if it is owned by the user 'guillame'.

103-Star_Wars contains a script that will play the StarWars IV episode in the terminal.
