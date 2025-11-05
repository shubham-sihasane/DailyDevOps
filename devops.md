## Daily DevOps

#### Linux

🌻 **VI Editor**
`vi OR vim <filename>` ✅ Create file and open in VI editor.

- Type `i` for insert mode, type `esc` for command mode, type `:` for last line mode
- Command Mode:
  - `x` to delete character, `dd` to delete line
  - `yy` to copy line, `p` to paste line
  - `Ctr+u` to scroll up, `Ctr+d` to scroll down
  - `:w` to save, `:q` to quit, `:q!` to quit without saving, `:wq` to save and quit
  - `/<word>` to find word in file, `n` for next occurrence of word

🌻 Multiple commands can be executed at once, each separated by ` ; `

`echo` ✅ Print something on screen like string or env variables `echo "Hi" OR echo  $SHELL`

`echo $?` ✅ Print the return value of previous command as 1 for success 0 for failure

`echo <text> >> <filename>` ✅ Write text to a file

`ls` ✅ List files and folders in the current directory or specific directory`ls <filename/directory>`

`ls -l` ✅ Print files and folders with details

`ls -a` ✅ Print files and folders including hidden items

`ls -la` ✅ Print files and folders including hidden items with additional details

`cd` ✅ Change the directory `cd <directory>`

`cd ..` ✅ Move to the parent directory

`pwd` ✅ Print present working directory

`mkdir` ✅ Make directory `mkdir <directory-name>`

`mkdir -p <dir1>/<dir2>/.../<dir10>` ✅ Make a directory recursively 

`rmdir` ✅ Remove empty directory `rmdir <direcotry-name>`

`rm <filename/s>` ✅ Remove a file from the system

`rm -r <directory/s>` ✅ Remove all the files including a directory

`cp <source-filepath> <target-filepath>` ✅ Copy file from source-path to target-path

`cp -r <source-dirpath> <target-dirpath>` ✅ Copy directory from source-path to target-path

`mv <source-file/dir-path> <target-file/dir-path>` ✅ Move file or directory from source to target

`mv <source-file/dir-path> <target-file/dir-path>` ✅ Rename a file or directory when source and target location is same

`touch <filename>` ✅ Create an empty file

`cat > <filename>` ✅ Create a file and wait for user input and save with Ctr+D

`cat <filename>` ✅ Print content of the filename

`whoami` ✅ Prints the username of the current effective user (you)

`who` ✅ Prints all users currently logged into the system

`id` OR `id <username>` ✅ Prints details about the user if specified

`su <username>` ✅ Switch user as another user (username), enter password when asked

`sudo su <username>` ✅ Switch user as superuser to perform high privileged task

`ssh <username>@<server-name>` ✅ Connect to remote server with username, enter password when asked

`wget <URL/filename> -o <filename>` ✅ Download the remote file from URL path | wget is best for downloading files recursively and mirroring websites

Use wget when:
- You want to download a file quickly with minimal fuss.
  - `wget https://example.com/file.zip`
- You need to mirror an entire website or recursively fetch directories.
  - `wget -r -np -k https://example.com/`

`curl <URL/filename> -o` ✅ Download the remote file from URL path | is more versatile for making API requests, handling multiple protocols, and fine-grained control over HTTP requests.

Use curl when:
- You’re working with APIs and need to send headers, tokens, or JSON payloads.
  - `curl -X POST https://api.example.com/data \
       -H "Content-Type: application/json" \
       -d '{"name":"Shubham","goal":"growth"}'
  `
- You want fine-grained control over HTTP requests (cookies, redirects, timeouts, etc.).
  - `curl -I https://example.com   # Fetch only headers`

`cat /etc/*release*` ✅ Print details about operating system

🌻 A Linux package manager is a tool that automates the process of installing, updating, configuring, and removing software on a Linux system. Instead of manually downloading and compiling programs, a package manager handles dependencies, versioning, and security updates for you.

- **Red Hat Package Manager (RPM)**
  - It does not install dependent packages
    - `rpm -i <package-name>` ✅ Install a package
    - `rpm -e <package-name>` ✅ Uninstall a package
    - `rpm -q <package-name>` ✅ Query a package, -qa for all packages
- **Yellowdog Updater Modified (YUM)**
  - It installs the dependent packages, it uses RPM under the hood
    - `yum repolist` ✅ List the repositories configured in the system
    - `ls /etc/yum.repos.d` ✅ Lists files where repositories are configured
    - `yum list <package-name>` ✅ List all installed package name
    - `yum --showduplicates  list <package-name>`
    - `yum install <package-name>-<version>` ✅ Install a package
    - `yum remove <package-name>-<version>` ✅ Uninstall a package

🌻 A Linux service is a background process (also called a daemon) that runs continuously to provide specific functionality, such as networking, logging, or web hosting, without direct user interaction.

`service <service-name> status/start/stop/enable/disable` ✅ Check status | start, stop service | enable, disable - configure service to run at startup

`systemctl status/start/stop/enable/disable/ <service-name>` ✅ Check status | start, stop service | enable, disable - configure service to run at startup

🌻 **Configure Service**
Every service get configured with a systemd unit file. `/etc/systemd/system` Once unit file is ready then `systemctl daemon-relaod` ✅ Reload the systemctl daemon to inform about new service 
 

#### Networking

`hostname` ✅ Prints the hostname of the system

`ping <hostname/URL/IP>` ✅ Tests connectivity to another network device. 

`/etc/hosts` ✅ Keeps records of mapping of IP and hostname or URL | Google Public DNS `8.8.8.8` | Cloudflare Public DNS `1.1.1.1` 

`/etc/resolv.conf` ✅ Keeps record of DNS server, and it's IP | hosts file gets precedence over resolv configuration (DNS) by default but this behaviour can be changed with `/etc/nsswitch.conf`

`tracert (or traceroute)` ✅ Traces the route packets take to a destination.

`ipconfig (Windows) / ifconfig (Linux)` ✅ Displays network configuration details.

`nslookup <hostname/URL/IP>` ✅ Queries DNS to obtain domain name or IP address mapping.

`dig <hostname/URL/IP>` ✅ Queries DNS to obtain domain name or IP address mapping with more details than nslookup.

`netstat` ✅ Displays active connections and listening ports.

`arp` ✅ Displays and modifies the ARP cache.

`route` ✅ Displays and modifies the IP routing table.

`telnet` ✅ Connects to remote devices for testing and management.

`nmap` ✅ Scans networks to discover hosts and services.

#### Application Basics

#### Web Servers

#### Database Basics

#### Security

#### General Pre-requisites
