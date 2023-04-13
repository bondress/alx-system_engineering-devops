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

9-John_Doe contains a script that sets the mode of the file hello (in the working directory) to '-rwxr-x-wx'
