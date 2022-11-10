## 0x04. Loops, conditions and parsing
### About <span style = "text-color: red">Bash<span> projects
Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.
<table>
 <tr>
  <td>
### Background Context


#### Resources
#### Read or watch:

- [Loops sample]('https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html')
- [Variable assignment and arithmetic]('https://tldp.org/LDP/abs/html/ops.html')
- [Comparison operators]('https://tldp.org/LDP/abs/html/comparison-ops.html')
- [File test operators]('https://tldp.org/LDP/abs/html/fto.html')
- [Make your scripts portable]('https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html')

#### man or help:
- env
- cut
- for
- while
- until
- if
#### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, `without the help of Google`:

### General
- How to create SSH keys
- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
- How to use while, until and for loops
- How to use if, else, elif and case condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them
### Requirements
#### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use awk
- Your Bash script must pass `Shellcheck (version 0.7.0)` without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
#### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.
### More Info
__Shellcheck__

Shellcheck is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to install it.

Examples:

Not passing Shellcheck:
![alt_img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

Passing <span style = "text-color: red">Shellcheck</span>:
![alt_img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code SC2034, you can browse [https://github.com/koalaman/shellcheck/wiki/SC2034]('https://github.com/koalaman/shellcheck/wiki/SC2034').

  </td>
 </tr>
</table>
<hr>
<table>
 <thead>
  <tr>
   <th> 0. Create a SSH RSA key pair</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
Read for this task:

- [Linux and Mac OS users]('https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys')
- [Windows users]('https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/')
man: ssh-keygen

You will soon have to manage your own servers concept page hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:
- Share your public key in your answer file 0-RSA_public_key.pub
- Fill the SSH public key field of your intranet profile with the public key you just generated
- Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
SSH and RSA keys will be covered in depth in a later project.

__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x04-loops_conditions_and_parsing`
- File: `0-RSA_public_key.pub`
   </td>
  </tr>
 </tbody>
</table>
<hr>
<table>
 <thead>
  <tr>
   <th> 1. For Best School Loop</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
Write a Bash script that displays `Best School` __10 times__.

Requirement:

- You must use the for loop (while and until are forbidden)
```
sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```
Note that:

- The first line of my Bash script starts with #!/usr/bin/env bash
- The second line of my Bash scripts is a comment explaining what it is doing
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x04-loops_conditions_and_parsing
File: 1-for_best_school
  </td>
  </tr>
 </tbody>
</table>