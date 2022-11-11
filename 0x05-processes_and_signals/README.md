### 0x05. Processes and signals
### About <span style="color:red">Bash</span> Project
Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

<table>
 <tr>
  <td>
#### Resources
##### Read or watch:

- [Linux PID]('http://www.linfo.org/pid.html')
- [Linux process]('https://www.thegeekstuff.com/2012/03/linux-processes-environment/')
- [Linux signal]('https://www.educative.io/answers/what-are-linux-signals')
- [Process management in linux]('https://www.digitalocean.com/community/tutorials/process-management-in-linux')
__man or help__:

- `ps`
- `pgrep`
- `pkill`
- `kill`
- `exit`
- `trap`
#### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

##### General
- What is a `PID`
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored
- Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.
##### Requirements
__General__

- Allowed editors: `vi, vim, emacs`
- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck (version 0.7.0 via apt-get)` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

__More Info__

For those who want to know more and learn about all signals, check out this article
  </td>
 </tr>
</table>

### Task
<table>
 <thead>
  <tr>
   <th> 0.What's my PID</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
Write a Bash script that displays its own PID.
```
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```

__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x05-processes_and_signals`
- File: `0-what-is-my-pid`
   </td>
  </tr>
 </tbody>
</table>

