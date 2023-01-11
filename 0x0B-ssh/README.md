## SSH
### Background Context
Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.
### Tasks
<table>
 <tr>
  <td><strong>0.Use a private key</strong></td>
 </tr>
 <tr>
  <td>
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase
```
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
``` 
__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `0-use_a_private_key`
  </td>
 </tr>
</table>
