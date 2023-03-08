## Application Server
<table>
 <tr>
  <td>
### Background Context

Your web infrastructure is already serving web pages via `Nginx` that you installed in your _first web stack project_. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

#### Resources
__Read or watch__:

- Application server vs web server
- How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
- Running Gunicorn
- Be careful with the way Flask manages slash in route - strict_slashes
- Upstart documentation

#### Requirements
__General__
- A `README.md` file, at the root of the folder of the project, __is mandatory__
- Everything Python-related must be done using `python3`
- All config files must have comments

__Bash Scripts__
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (`version 0.3.7-5~ubuntu16.04.1 via apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
  </td>
 <tr>
<table>
