# 0x17. Web Stack Debugging #3

## Project Overview

This project focuses on debugging a Wordpress website running on a LAMP stack. The goal is to identify and resolve a specific issue causing Apache to return a 500 Internal Server Error. The resolution should be automated using Puppet.

## Background Context

When dealing with web stack issues, logs may not always provide sufficient information. In such cases, tools like `strace` can be used to trace system calls and signals, which can help identify issues beyond standard logs. This project involves using `strace` to diagnose an Apache server error and then using Puppet to automate the fix.

Wordpress, a widely used content management system, is often run on a LAMP stack (Linux, Apache, MySQL, PHP). This project requires you to debug an issue in such an environment.

## Requirements

- All files must be interpreted on Ubuntu 14.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests must run without errors.
- Puppet manifests must start with a comment explaining their purpose.
- Puppet manifest files must end with the `.pp` extension.
- Files will be checked with Puppet v3.4.

## Tasks

### 0. Strace is your friend

**Mandatory**

Using `strace`, determine why Apache is returning a 500 error. Once the issue is identified, fix it and automate the solution using Puppet instead of Bash.

**Hint:**

- `strace` can attach to a currently running process.
- You can use `tmux` to run `strace` in one window and `curl` in another.

**Requirements:**

- Your `0-strace_is_your_friend.pp` file must contain Puppet code.
- You can use any Puppet resource type for your fix.

**Example Output:**

```bash
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#
