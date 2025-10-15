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

### 🐯  Git Repository
A git repository is a workspace which tracks and manages files within a folder. Before we can do anything with Git, we need to initialize or convert normal directory into git repository. Once in a lifetime of Git project.

It also creates a .git hidden directory which contains all the information about git repository including git objects, info, logs, tags, refs etc. By default, it creates <master< but can be customized to create any other branch like <main>.

Do not initialize a Git repository inside another Git repository. Avoid Nesting.

👹 .gitignore file specifies intentionally untracked files that Git should ignore. Each line in a .gitignore file specifies a pattern. This is useful for files you know you NEVER want commit including Secrets, API Keys, credentials, OS files, log files, dependencies or packages. 

### 🐯 Basic Git Workflow
1. Working Directory (Work On Stuff) --> Make new files, edit files, delete files etc.
2. Staging Area (Add/Remove Stuff) --> Group specific changes together, in preparation of commiting.
3. Repository (Permanent Stuff) --> Commit everything that was previously added.

---

### 🦁 Basic Git Commands
```git --version``` OR ```git -v``` ✅ Check the installed git version

```git config --global --list``` OR ```git config --global list``` ✅ Check the list of all configured values for git

```git config --global user.name``` ✅ Check configured username in the system for git

```git config --global user.name <Shubham Sihasane>``` ✅ Configure username for git

```git config --global user.email``` ✅ Check configured email in the system for git
 
```git config --global user.email <shubhamsihasane101@gmail.com>``` ✅ Configure email for git

git status ✅ Gives current status of git repository and its contents. 

```git init <ProjectName>``` ✅ Initialize or create a new git repository with <ProjectName>

```git init``` OR ```git init .``` ✅ Convert current working directory as git repository

```git status``` ✅ Check the current status of git repository

```git add <filename>``` OR ```git add <file1 file2 ... file10>``` OR ```git add .``` ✅ Add one or more or all files from working directory to staging area of git.

```git rm --cached <filename>``` OR ```git add <file1 file2 ... file10>``` ```git rm -r --cached .``` ✅ Remove untracked one or more files from staging area to working directory which is also known as unstaging.

```git commit -m <Change Summary Message>``` ✅ Commit a change with message which moves one or more tracked or untracked files from staging area to local git repository. The first branch <master> or <mai>< only gets created after first commit. Practice Atomic Commits - Keep each commit focused on a single thing. Use present tense for commit messages.

```git commit -am <Change Summary Message>``` ✅ Commit a change with message which moves one or more tracked files from working directory to local git repository without explicitly going via staging.

```git commit --ammend``` ✅ Replace the tip of the current branch by creating a new commit. Helps in modifying the last commit including message.   

```git log``` ✅ Generate detailed git logs 

```git log --oneline``` ✅ Generate git logs in shorter version - one line

```git restore --staged <filename>``` OR ```git restore --staged <file1 file2 ... file10>``` OR ```git restore --staged .``` ✅ Move one or more files or all files from staging area to working directory.

### 🐯 GitHub Branching
Branches are the essential parts of the Git. They enable us to create separate contexts where we can try new things, or even work on multiple ideas in parallel. If we change on one branch, they do not impact the other branches (unless we merge the changes).

```git branch``` ✅ List all the branches in the repository. `*` represents the current branch.

```git branch <BranchName>``` ✅ Create a new branch with <BranchName> based on current HEAD

In Git, the HEAD is a pointer to the current branch or commit you are working on. Updating the HEAD can involve moving it to a different branch, commit, or even creating a detached HEAD state. Below are methods to update the HEAD effectively. [.git -> /ref/heads/ -> It contains the pointer to HEAD]

```git switch <BranchName>``` OR ```git checkout <BranchName>``` ✅ Switch from current branch to <BranchName>

```git switch -c <BranchName>``` OR ```git checkout -b <BranchName>``` ✅ Create and switch to new <BranchName>

```git branch -m <NewBranchName>``` OR ```git branch -m <OldBranchName> <NewBranchName>``` ✅ Rename current branch OR <OldBranchName> to <NewBranchName>

```git branch -d <BranchName>``` ✅ Delete a non-current branch

```git branch -D <BranchName>``` ✅ Delete a branch forcefully

### 🐯 Git Merging
Submitting a merge request in Git involves combining changes from one branch into another, typically as part of a collaborative development workflow. 
1. We merge branches not specific commits
2. We always merge to the current branch HEAD

To merge, follow these basic steps:
1. Switch to or checkout the branch you want to merge the changes into.
2. Use the git merge command to merge changes from a specific branch into the current branch. 

```git merge <BranchName>``` ✅ Merge <BranchName> with current branch
```git merge <SourceBranch> <DestinationBranch>``` ✅ # Merge SourceBranch into Destination Branch

### 🐯Types of Merging

There are two primary types of merging in Git:
1. **Fast-Forward Merging:** This occurs when the tip of the current branch is a direct ancestor of the target branch. Git simply moves the current branch tip up to the target branch tip.

2. **Three-Way Merging:** This occurs when the base branch has changed since the branch was first created. Git generates a fresh merging commit that incorporates the modifications from both branches.

### 🐯 GitHub
GitHub is a service that hosts Git repositories in the cloud and makes it easier to collaborate with other people. You do need to sign up for an account to use GitHub. It's an online social place to share work that is done using Git.

git clone is a command used to create a copy of a remote Git repository on your local machine. It downloads all the project files, history, and branches so you can start working with the code right away.

Anyone can clone a repository from GitHub, provided the repo is public. You do not need to be an owner or collaborator to clone the repo locally to your machine. You just need the URL from GitHub.

Pushing up your own changes to the GitHub repository may need the permission.

```git clone <repository-url>``` ✅ Copies the entire repository from a remote source (like GitHub) to your local computer.

```git remote add <remoteName> <remoteURL>``` ✅ Add remoteURL into local repository to refer it with remoteName (origin). A remoteName is just a fancy way to refer remoteURL from hosting platform like GitHub.

```git remote``` ✅ List the name of RemoteName

```git remote -v``` ✅ List the mapped remoteURL (fetch/push) for remoteName

```git remote rename <oldRemoteName> <newRemoteName>``` ✅ Rename a remoteName

```git remote remove <remoteName>``` ✅ Remove a remoteName

The git push command is used to upload local repository content to a remote repository. It updates the remote branch with local commits, making your changes accessible to others.

```git push <remoteName> <branchName>``` ✅ Push code from local branchName to remote branchName

```git push <remoteName> <localBranch>:<remoteBranch>``` ✅ Push localBranch to RemoteBranch

```git push -u <remoteName> <branchName>``` == ```git push``` ✅ ```-u = --set-upstream``` Upstream of localBranch pointing to remoteBranch

```git branch -r``` ✅ List all the remote branches

```git checkout <remoteName/branchName>``` ✅ Checkout remote branch then You are in 'detached HEAD' state. You can look around, make experimental changes and commit them, and you can discard any commits you make in this state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  ```git switch -c <new-branch-name>```

Or undo this operation with:

  ```git switch -```
