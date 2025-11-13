## Linux

`~` ⌘ Home directory of user

`<command> --help` OR `man <command>` OR `whatis <command>` ⌘ Gives quick information or help about command

`apropos <keyword>` ⌘ Search commands with keywords

`uptime` ⌘ The uptime command in Linux provides information about how long a system has been running, the number of users currently logged in, and the system's load average.

`type <command>` ⌘ To determine the type of command in Linux, the type command is used. `type echo OR type ls`

`history` ⌘ The history command in Linux displays a list of previously executed commands in the current shell session and from the history file. This allows users to review, reuse, and manipulate past commands without retyping them.

`echo $SHELL` ⌘ Displays the current shell

`chsh` ⌘ Change the default shell, change the shell option and save file

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

`echo <message>` ✅ Print message on screen like string or env variables `echo "Hi" OR echo -n "Hi" OR echo $HOME OR echo $PS1` 

`echo $?` ✅ Print the return value of previous command as 1 for success 0 for failure

`echo <text> >> <filename>` ✅ Write text to a file

`which <program>` ⌘ Display variable path for program Ex. `which bash`

`alias <shortform> <command>` ⌘ Create an alias shortform for a command

`env` ⌘ List all the environmental variables in system

`export <key> = <value>` ⌘ Configure environmental variable with key and set its value

`export PATH = $PATH:<path>`  ⌘ The PATH variable in Linux is an environment variable that informs the shell about the directories to search for executable files when a command is entered. Instead of requiring the user to specify the full path to an executable every time, the shell consults the directories listed in the PATH variable.

`echo 'export <key>:<value>' >> ~/.profile` then `source ~/.profile` ⌘ Add to profile and make it persistent [~/.profile = ~/.bashrc]

`ls` ✅ ⌘ The ls command in Linux is a fundamental utility used to list the contents of directories. When executed without any arguments, it displays the files and subdirectories within the current working directory. `ls <filename/directory>`

`ls -l` ⌘ The -l option provides a detailed "long listing" format, showing information such as file permissions, number of links, owner, group, file size, and modification date. `ls -l = ll`

`tree` ⌘ Shows directory structure

`ls -h` ⌘ Displays file sizes in a human-readable format

`ls -R` ⌘ The -R option lists the contents of directories and their subdirectories recursively.

`ls -a` ✅ Displays all files and directories, including hidden ones

`ls -la` ✅ Displays files and folders including hidden items with additional details

`ls -ltr` ⌘ -t for time based, -r for reverse order

`cd` ⌘ The cd command in Linux stands for "change directory." It is a fundamental shell command used to navigate the file system hierarchy by changing the current working directory in the terminal. `cd <directory>`

`cd ..` ⌘ The command in Linux is used to change the current working directory to its parent directory.

`pushd <directory-name>` & `popd` ⌘ These are shell built-in commands in Linux that provide a convenient way to navigate directories using a "directory stack" based on the Last-In, First-Out (LIFO) principle. They are particularly useful for quickly switching between frequently used directories or for managing directory changes within shell scripts.

`pwd` ✅ The pwd command in Linux stands for "Print Working Directory." Its primary function is to display the full, absolute path of your current location within the file system hierarchy to the standard output. This path starts from the root directory (/) and lists all the directories leading up to your current working directory, separated by slashes.

`Absolute vs Relative Path` ⌘ An absolute path is a full path from the root directory (/) to a file or directory, while a relative path is a path based on the current working directory.

`mkdir` ⌘ The mkdir command in Linux, short for "make directory," is a command-line utility used to create new directories (also known as folders) within the file system. `mkdir <directory-name>`

`mkdir -p <dir1>/<dir2>/.../<dir10>` ✅ Make a directory recursively

`rmdir` ✅ Remove empty directory `rmdir <direcotry-name>`

`rm <filename/s>` ✅ Remove a file from the system

`rm -r <directory/s>` ✅ Remove all the files including a directory

`cp <source-filepath> <target-filepath>` ⌘ The cp command in Linux is used to copy files and directories. It duplicates the content of a source file or directory to a specified destination.

`cp -r <source-dirpath> <target-dirpath>` ⌘ The -r or -R option is essential for copying directories, as it recursively copies all files and subdirectories within the source_directory to the destination_directory.

`mv <source-file/dir-path> <target-file/dir-path>` ⌘ The mv command in Linux is a utility used for two primary functions: moving files and directories, and renaming files and directories.

`mv <source-file/dir-path> <target-file/dir-path>` ✅ Rename a file or directory when source and target location is same

`touch <filename>` ✅ Create an empty file

`echo <filename> | less` OR `echo <filename> | more` ⌘ Displat information page by page

`head -N <filename>` ⌘ Display first N lines from file

`tail -N <filename>` ⌘ Display last N lines from file

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

`uname` ⌘ Display the kernal name `uname -r` ⌘ Display the kernal version

`lsblk` ⌘ Displays the list of block devices on the system `RAM=1 HARD DISK=3 PRINTERS=6 SCSI DISK=8`

`lscpu` ⌘ Displays the detailed information about cpu

`lsmem --summary` ⌘ Displays the system memory information

`lshw` ⌘ Displays the entire hardware information of the system

`free -g -h` ⌘ Display the total and used memory of the system `-k=KB, -m=MB, -g=GB, -h=human readable`

`df -h` ⌘ Displays the disk file details

### Linux Boot Process
1. BIOS POST (Basic Input-Output System Power On Self Test)
2. Boot Loader (GRUB2 - Grand Unified Boot Loader 2)
3. Kernel Initialization (Loads system into the memory)
4. INIT Process (Systemd) (Bring system in usable state)

Run levels in Linux define the operating state of the system, determining which services and processes are active. These levels, typically numbered 0-6, are a fundamental concept in traditional SysVinit systems, although modern Linux distributions often utilize systemd which uses "targets" that are conceptually similar to run levels.

- Runlevel 0: System halt (shutdown). 
- Runlevel 1 (Single-User Mode): Minimal services, primarily for maintenance or recovery.  (poweroff.target)
- Runlevel 2: Multi-user mode without network services (less common).  (rescue.target)
- Runlevel 3: Full multi-user mode with networking, command-line interface. (multi-user.target)
- Runlevel 4: User-definable (often unused). (multi-user.target)
- Runlevel 5: Full multi-user mode with networking and a graphical user interface (GUI). (graphical.target)
- Runlevel 6: System reboot. (reboot.target)

`runlevel` ⌘ Displays default runlevel

`systemctl get-default` ⌘ Displays default mode - CLI or GUI

`system set-default <graphical.target/multi-user.target>` ⌘ Change default OS mode

`hostname` ✅ Prints the hostname of the system

`hostnamectl` ⌘ Prints host details

`sudo hostnamectl set-hostname <new-hostname>` ⌘ Rename hostname of system

### File Types
1. Regular Files (-): These are standard data files, such as text documents, executable programs, images, or archives.
2. Directories (d): These are special files that contain references to other files and directories, forming the hierarchical structure of the file system.
3. Special Files
   - Symbolic Links (l): Also known as soft links, these files act as pointers to other files or directories, providing an alternative path to access the linked target. 
   - Character Device Files (c): These represent devices that handle data character by character, such as keyboards, mice, or serial ports. 
   - Block Device Files (b): These represent devices that handle data in fixed-size blocks, primarily storage devices like hard drives, SSDs, or CD-ROM drives. 
   - Named Pipes (FIFO) (p): These facilitate inter-process communication, allowing data to flow in a one-way, first-in, first-out manner between processes. 
   - Sockets (s): These are used for inter-process communication, enabling data exchange between processes on the same system or across a network.

`file <regular/direcotry>/special-file` ⌘ Displays the file type, Alternatively `ls -l` first character

![files.png](images/files.png)

### Package Managers

1. Debian Based Distro - Debian, Ubuntu, Kali Linux [DPKG -> APT-GET -> APT]
2. RPM Based Distro - RHEL, CentOs, Fedora [RPM -> YUM, DNF]

#### RPM - Red Hat Package Manager
RPM defines a specific file format (.rpm) for packaging software. These packages contain all the necessary files (executables, libraries, configuration files, documentation, etc.), along with metadata like dependencies, version information, and pre-post installation scripts.

While RPM itself can manage dependencies, higher-level package managers like yum (Yellowdog Updater, Modified) and dnf (Dandified YUM) build upon RPM to automate dependency resolution, making software installation and updates much smoother.

1. Install `rpm -ivh <package-name>`
2. Uninstall `rpm -e <package-name>`
3. Upgrade `rpm -uvh <package-name>`
4. Query `rpm -q <package-name>`
5. Verifying `rpm -vf <package-name>`

#### YUM - Yellowdog Updator Modified
YUM (Yellowdog Updater, Modified) is a command-line package manager for RPM-based Linux distributions like CentOS and Fedora, used to install, update, and remove software packages and their dependencies. It automatically handles dependencies and upgrades from online repositories, making it easier to manage software compared to the lower-level RPM tool.

1. Install `yum install <package-name>`
2. Uninstall `yum remove <package-name>`
3. Upgrade `yum update <package-name>` OR `yum update` for all packages 
4. Repolist `yum repolist` 

#### DPKG & APT
dpkg (Debian Package Manager) is a low-level tool for installing, removing, and managing individual Debian package files (.deb), while apt (Advanced Package Tool) is a higher-level package management system that handles dependencies and retrieves packages from online repositories. 

1. Install `dpkg -i <package-name>`
2. Uninstall `dpkg -r <package-name>`
3. List `dpkg -l <package-name>`
4. Status `dpkg -s <package-name>`
5. verify `dpkg -p <path-to-file>`

apt is a more user-friendly frontend that uses dpkg to perform the actual installation and manages the complexities of package relationships automatically.

1. Install `apt install <package-name>`
2. Uninstall `apt uninstall <package-name>`
3. Update repo `apt update`
4. Upgrade `apt upgrade`
5. Search `apt search <package-name>`
6. List `apt list | grep <package-name>`

The du command in Linux, short for "disk usage," is used to estimate and display the disk space used by files and directories. It recursively calculates and shows the size of directories and their contents. 

`du -lh <file/directory>`

The tar command in Linux is a powerful utility used for creating, viewing, and extracting files from archives, often referred to as "tarballs." It is commonly used for backups, software distribution, and transferring collections of files while preserving their directory structure, permissions, and other metadata.

**Creating an archive:**
`tar -cvf archive_name.tar file1 file2 dir1/` ⌘ Creates an uncompressed archive.

`tar -czvf archive_name.tar.gz file1 file2 dir1/` ⌘ Creates a gzipped (compressed) archive.

`gzip <archive_name.tar>` ⌘ Create gzip from tarball

`ungzip <archive_tar.gz>` ⌘ Unzip from gzip file

**Options used:**
- -c: Create a new archive. 
- -v: Verbosely list files processed. 
- -f: Specify the filename of the archive. 
- -z: Filter through gzip for compression/decompression.

**Extracting files from an archive:**
`tar -xvf archive_name.tar` ⌘ Extracts files from an uncompressed archive.

`tar -xvf archive_name.tar.gz` ⌘ Extracts files from a gzipped archive.

`tar -xvf archive_name.tar.bz2` ⌘ Extracts files from a bzip2 archive.

`tar -xvf archive_name.tar.xz` ⌘ Extracts files from xz archive.

`tar -xvf archive_name.tar.gz -C /path/to/destination` ⌘ Extracts to a specific directory.

**Options used:**
- -x: Extract files from an archive. 
- -C: Change to a specified directory before performing the operation.

**Listing the contents of an archive:**
`tar -tvf archive_name.tar` ⌘ Lists contents of an uncompressed archive.
`tar -tvf archive_name.tar.gz` ⌘ Lists contents of a gzipped archive.

**Options used:**
- -t: List the contents of an archive.

`locate <filenamec>` The locate command in Linux is a utility used to quickly find files and directories by name. It operates by searching a pre-built database of file paths, rather than scanning the entire filesystem in real-time.

`find <filename>` The find command in Linux is a powerful utility used to search for files and directories within a specified hierarchy based on various criteria. `find -name <pattern>`

`grep -i <pattern> <filename/dir>` The grep command in Linux is a powerful command-line utility used for searching plain-text data sets for lines that match a regular expression. 

The name grep stands for "global regular expression print. `-i for case insensitive` & `-r for recursively search` & `-v for everything except pattern` & `-w for exact word` & `-vw for first line for exact word`

`grep -A1 -B1 <pattern> <filename>` ⌘ Print #N of lines after (-AN) and before (-BN) pattern in filename

#### IO Redirection & Command Line Pipes
`command1 | command2` ⌘ Output of command1 as input to command2 `cat <filename> | less`

`cat <text> > <filename>` ⌘ Redirect text into file and overwrite

`echo <text> | tee <filename>` ⌘ Paste text into file and overwrite

`cat <text> >> <filename>` ⌘ Redirect text into file and append

`echo <text> | tee -a <filename>` ⌘ Paste text into file and append

### Networking

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

`nmap` ✅ Scans networks to discover hosts and services.r



