## 0x06. Regular expression
<span style="color:read">Regex</span> <span style="color:red">DevOps</span>
<table>
 <tr>
  <th style="aline:left">Concepts</th>
 </tr>
 <tr>
  <td>
For this project, we expect you to look at this concept:

- Regular Expression
  </td>
 </tr>
</table>
<br>
<table>
 <tr>
  <td>
### Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

#### Resources
##### Read or watch:

- [Regular expressions - basics]('https://www.regular-expressions.info/')
- [Regular expressions - advanced]('https://www.slideshare.net/neha_jain/introducing-regular-expressions')
- [Rubular is your best friend]('https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518')
- [Use a regular expression against a problem: now you have 2 problems]('https://rubular.com/')
- [Learn Regular Expressions with simple, interactive exercises]('https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/')
- [Leanring it]('https://regexone.com/lesson/letters_and_digits?')
#### Requirements
##### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- `A README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
- All your regex must be built for the Oniguruma library
  </td>
 </tr>
</table>
<br>
## Tasks

<table>
 <thead>
  <tr>
   <th> 0.Simply matching school</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
![alt-image]('https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221115T095229Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d727958930b4b14492dedd3b72d60a8b1db577e32e507496291a4d621f05b09c')

Requirements:

- The regular expression must match School
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:
```
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```
__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x06-regular_expressions`
- File: `0-simply_match_school.rb`
  </td>
  </tr>
 </tbody>
</table>

<table>
 <thead>
  <tr>
   <th> 1. Repetition token #0</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
![img](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221115T095229Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=791f17a06b8c9f5c7db220612999bd40b0eda075e4f05caac1ff32e6e6d24ce9)

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x06-regular_expressions`
- File: `1-repetition_token_0.rb`
   </td>
  </tr>
 </tbody>
</table>

<table>
 <thead>
  <tr>
   <th>2. Repetion token #1</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
![img](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221115T095229Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1ac56e482ad2ddf92c89d377618c25a01b39fbd164d8696c346ec8ed6683da5d)

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x06-regular_expressions`
- File: `2-repetition_token_1.rb`
   </td>
  </tr>
 </tbody>
</table>

<table>
 <thead>
  <tr>
   <th> 3. Repetition token #2</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
![img](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221115T095229Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3fcc51b903bd4eff6bcc949584d6fcfed7af0f4dcee59301e86094fed990b052)

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x06-regular_expressions`
- File: `3-repetition_token_2.rb`
   </td>
  </tr>
 </tbody>
</table>

<table>
 <thead>
  <tr>
   <th>4. Repetition token #3 </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Your regex should not contain square brackets
__Repo__:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x06-regular_expressions`
- File: `4-repetition_token_3.rb`
   </td>
  </tr>
 </tbody>
</table>
