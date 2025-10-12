### 🐯 Git
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
1. Home: https://git-scm.com
2. Download: https://git-scm.com/downloads
3. Learn: https://git-scm.com/
4. Tools: https://git-scm.com/tools
5. References: https://git-scm.com/docs

### 🐯 Version Control System
Version control system is a software that tracks and manages the changes in files and directories of source code project over time. Examples of version control systems are Git, Subversion, CVS and Mercurial.

Version control systems generally allows users to revisit earlier versions of the files, compare changes between versions, undo changes, and whole a lot more.

### 🐯 History of Git
Linus Torvalds is the creator and main developer of Git and Linux. 

In 2005, while working on Linux, he became frustrated with the available version control systems. The existing tools were slow, closed source and usually paid tools.

On April 2005, he launched the initial version of Git (The stupid content tracker -> Global Information Tracker). The first official release came a couple of months later. 15 years later in 2020, over 90% of developers worldwide use Git on a daily basis.

### 🐯 Git
Git is the version control software that runs locally on your machine. You don't need to register for an account. You don't need the internet to use it. You can use Git without ever touching GitHub. It is a primarily a Terminal based tool.

### 🐯 GitHub
GitHub is a service that hosts Git repositories in the cloud and makes it easier to collaborate with other people. You do need to sign up for an account to use GitHub. It's an online social place to share work that is done using Git.

### 🐯  Git Repository
A git repository is a workspace which tracks and manages files within a folder. Before we can do anything with Git, we need to initialize or convert normal directory into git repository. Once in a lifetime of Git project.

It also creates a .git hidden directory which contains all the information about git repository including git objects, info, logs, tags, refs etc. By default, it creates "master" but can be customized to create any other branch like "main".

Do not initialize a Git repository inside another Git repository. Avoid Nesting.

### 🐯 Basic Git Workflow
1. Working Directory (Work On Stuff) --> Make new files, edit files, delete files etc.
2. Staging Area (Add/Remove Stuff) --> Group specific changes together, in preparation of commiting.
3. Repository (Permanent Stuff) --> Commit everything that was previously added.

---

### 🦁 Basic Git Commands
```git --version``` OR ```git -v``` ✅ Check the installed git version

```git config --global --list``` OR ```git config --global list``` ✅ Check the list of all configured values for git

```git config --global user.name``` ✅ Check configured username in the system for git

```git config --global user.name "Shubham Sihasane"``` ✅ Configure username for git

```git config --global user.email``` ✅ Check configured email in the system for git
 
```git config --global user.email "shubhamsihasane101@gmail.com"``` ✅ Configure email for git

### 🦁 Basic GitHub Commands
git status ✅ Gives current status of git repository and its contents. 

```git init "ProjectName"``` ✅ Initialize or create a new git repository with "ProjectName"

```git init``` OR ```git init .``` ✅ Convert current working directory as git repository

```git status``` ✅ Check the current status of git repository

```git add "filename"``` OR ```git add "file1 file2 ... file10"``` OR ```git add .``` ✅ Add one or more or all files from working directory to staging area of git.

```git rm --cached "filename"``` OR ```git add "file1 file2 ... file10"``` ```git rm -r --cached .``` ✅ Remove untracked one or more files from staging area to working directory which is also known as unstaging.

```git commit -m "Change Summary Message``` ✅ Commit a change with message which moves one or more files from staging area to local git repository.

