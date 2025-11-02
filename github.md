### ⛵ Git
Git is a free, open source and distributed, cross-platform version control system designed to handle everything from small to very large projects with speed and efficiency which helps in controlling and tracking of changes over time by managing the code history. It is faster than any other tools offers better safeguards against data corruption.

### ⛵ Source Code Management (SCM)
Source Code Management (SCM) is the practice of tracking, organizing, and controlling changes to software code. It ensures that developers can work together without overwriting each other’s work, while keeping a full history of every change.

🗂️ Versioning: Maintains past versions so you can roll back if needed.

👥 Collaboration: Lets multiple developers contribute safely.

🌿 Branching & Merging: Enables experimenting with new features before merging them into the main codebase.

📜 History & Audit: Records who changed what, when, and why.

Think of SCM as a shared library with a time machine: everyone can borrow, edit, and return books (code), while the system remembers every edition ever published.

### History of Version Control
Source Code Control System (SCCM) first built by AT&T in 1972 and shipped with Unix for free. Revision Control System (RCS) was cross-platform and faster built Walter in 1982. Both SCCM and RCS were designed to track individual files only.

Concurrent Versions System (CVS) was built by Dick Grune to track multiple files, shared repositories in 1986.

Apache Subversion (SVN) was built in 2000 which was faster used to track non-text files and track edits in a project.

BitKeeper SCM was distributed, initially offered as free version in 2000 which was used for Linux kernel source code between 2002-2005 and controversial to use proprietary SCM for an open source projects.

### ⛵ History of Git
Linus Torvalds is the creator and main developer of Git and Linux. 

In 2005, while working on Linux, he became frustrated with the available version control systems (BitKeeper). The existing tools were slow, closed source and usually paid tools.

On April 2005, he launched the initial version of Git (The stupid content tracker -> Global Information Tracker). The first official release came a couple of months later. 15 years later in 2020, over 90% of developers worldwide use Git on a daily basis.

### ⛵ GitHub
GitHub launched in 2008 as a service that hosts Git repositories in the cloud and makes it easier to collaborate with other people. You do need to sign up for an account to use GitHub. It's an online social place to share work that is done using Git.


### ⛵ Version Control System (VCS)
A Version Control System (VCS) is software that helps developers track, manage, and organize changes to code. It allows teams to collaborate, experiment with new features, and roll back to earlier versions if something goes wrong.

#### **Centralized (CVCS):**
- A single server to store primary copy
- Collaboration depends on the availability of the central repository
- Developers can check out copies and submit changes, need same versions of all files
- Examples: SCCS, RCS, CVS and SVN.

#### **Distributed (DVCS):**
- Different users maintain their own repositories.
- Multiple people can have multiple copies with their own combination of change sets
- Many changes are stored as change sets - tracks changes, not versions
- Change sets can be exchanged between repositories.
- No need to communicate with central server which makes it faster, no network dependency, no single point of failure.
- Encourages participation and forking of projects so that developers can work independently, submit change sets for inclusion or rejection, take code in new direction, pick and choose from available change sets.
- Can still designate a primary repository for collaboration which is not a requirement of Git by default, All repositories have an equal level of authority, easy to designate a different repository for collaboration.

### ⛵  Git Repository
A git repository is a workspace which tracks and manages files within a folder. Before we can do anything with Git, we need to initialize or convert normal directory into git repository. Once in a lifetime of Git project.

It also creates a .git hidden directory which contains all the information about git repository including git objects, info, logs, tags, refs etc. By default, it creates <master< but can be customized to create any other branch like "main".

Do not initialize a Git repository inside another Git repository. Avoid Nesting.

### ⛵ Git Scope
Git has three main configuration scopes: system, global, and local. Each defines where settings are stored and how widely they apply. There’s also a worktree scope in newer Git versions.

#### System Scope (--system)
- Applies to: All users on the machine 
- Config file location: /etc/gitconfig (Linux/macOS) or C:\ProgramData\Git\config (Windows)
- Use case: Organization-wide defaults, like proxy settings or default line endings
```git config --system```

#### Global Scope (--global)
- Applies to: The current user across all repositories
- Config file location: ~/.gitconfig or ~/.config/git/config
- Use case: Personal identity (name, email), editor preference, aliases
```git config --global```

#### Local Scope (--local)
- Applies to: A single repository only 
- Config file location: .git/config inside the repo 
- Use case: Project-specific settings, like remotes, branch behaviors, or hooks 
```git config --local```

#### Worktree Scope (--worktree) (optional, newer Git versions)
- Applies to: A single linked worktree within a repository 
- Config file location: .git/worktrees/<name>/config 
- Use case: Different settings for multiple working directories tied to the same repo
```git config --worktree```

🔖 **Precedence Order**
- When Git looks up a configuration value, it checks in this order (from lowest to the highest priority): worktree --> local --> global --> system 
- If the same setting exists in multiple scopes, the closest scope wins (e.g. local overrides global).

### 🏵️ Configurational Commands

```git config --global user.name "<Firstname Lastname>"``` ✅ Configure username

```git config --global user.email "<example@email.com>"``` ✅ Configure user email

```git config --global color.ui true``` ✅ Configure color ui to tru for color highlighting

```git config --global init.defaultBranch <branchName>``` ✅ Set default branch name like main, master, trunk development

```git config --global core.editor "<code editor> --wait"``` ✅ Configure default code editor for commiting message like "code --wait" for vscode

```git config --global --list``` ✅ List all the configured values globally

```git config --global <config-key>``` ✅ List the value of config-key like user.name

```cat ~/.gitconfig``` ✅ List the content of global config file

### 🏵 Basic Git Commands

```git --version``` OR ```git -v``` ✅ Check installed git version

---

```git help``` ✅ List all the important git commands with short description

```git help git``` ✅ The complete git documentation

```git help -a``` ✅ List all git commands

```git help <git-command>``` ✅ Get help with 'git help commands'

```git help -g``` ✅ List all concept guides 

```'git help <git-concept-guide>``` ✅ Get help with 'git concept guides'
to read about a specific subcommand or concept guides.

---

```git init <repo-name>``` ✅ Create git repository with "repo-name" --> Navigate inside repository to work

```git init``` OR ```git init .``` ✅ Convert current directory into git repository

#### 🌻 Commiting
- A commit is the fundamental unit when working with Git
- You commit one or more changes grouped together represents a set
- A set represents single unit of work or feature as commit

```git status``` ✅ Get status of git repository

```git add <filename>``` ✅ Add filename into staging area

```git restore --staged <filename>``` ✅ Remove filename from staging area and put into working area

```git add <filename1> <filename2> ...``` ✅ Add or more files into staging area

```git restore --satged <filename1> <filename2> ...``` ✅ Remove one or more files from staging area and put into working area

```git add .``` ✅ Add all files from working area to staging area

```git restore --staged .``` ✅ Remove all files from staging area and put into working area

```git commit -m <"commit-message">``` ✅ Commit a single unit of work with "commit-message" | -m includes the commit-message without opening editor

```git commit``` ✅ It opens the editor for detailed commit message and description

```git commit -am <commit-message>``` ✅ Commit change including all tracked files without going through staging area [working area to directly repository]

```git commit --ammend -m <commit-message>``` ✅ Modify the commit message for only last commit

#### 🌻 Commit Message Best Practices
- A short single-line summary (less than 50 characters)
- Optionally followed by a blank line and a more complete description
- Keep each line less than 72 characters
- Write in present tense, not past tense (Fix a bug instead of Fixed a bug)
- Can add change request or bug report tracking number

#### 🌻 Git Logging
```git log``` ✅ Returns an overview of all commits in the current branch in reverse chronological order by default

```git log --oneline``` ✅ List history or logs in oneline

```git log <filename>``` ✅ Show logs only for filename

```git log -n <count>``` OR ```git log -<count>``` ✅ Show logs only for past N commits

```git log <SHA1>..<SHA2>``` ✅ Show logs between two commits ```git log HEAD~5..HEAD```

```git log --since=2025-01-30``` OR ```git log --until="3 days ago"``` OR ```git log --after=2.weeks --before=3.days``` OR ```git log --author="Shubham Sihasnae"``` OR ```git log -E --grep="bug"``` ✅ Variations to filter the logs

---

#### 🌻 Log Formatting

```git log --format=<parameter>``` ✅ Format the logs with parameter value = oneline, short, medium (default), full, fuller, email, raw

```git log --graph``` OR ```git log --graph --all --oneline --decorate``` OR ```git log -p``` ✅ Format the output of logs

---

```git show <commit-hash>``` ✅ List the contents of commit

```git show HEAD``` ✅ List the contents of last commit

```git show <branch-name>``` ✅ List the contents of HEAD pointing to branch-name

```git show <tag-name>``` ✅ List the tag-name content

```git show <blob-name>``` ✅ List the blog-name content

```git show <tree-name>``` ✅ List the tree-name content

### ⛵ Basic Git Workflow (Local)
Tree is a general computer science term for a hierarchical data structure . File System = Tree

The process involves making the changes, adding those changes to a set, and then committing the set of changes to the repository with a description.

1. Working Directory (Work On Stuff) --> Make new files, edit files, delete files etc.
2. Staging Area (Add/Remove Stuff) --> Group specific changes together, in preparation of commiting.
3. Repository (Permanent Stuff) --> Commit everything that was previously added.

#### 🌻 Hash Values (SHA-1)
- Unique identifier for data integrity
- Git generates a hash value for each change set
  - Hash algorithms reduce data into a unique alphanumeric string
  - Same algorithm + same data = same hash value
- Git uses SHA-1 hash algorithm
  - 40 character hexadecimal string (0-9, a-f)
- Sometimes referred to as "sha" value
- Git not unique provides data integrity for content but also commits

#### 🌻 Review files
```git diff``` OR ```git diff HEAD``` Show the difference between working directory and last commit

```git diff --staged``` OR ```git diff --staged HEAD``` ✅ Show the difference between staging area and last commit [--staged == --cached]

```git diff <commit-1> <commit-2>``` ✅ Show the difference between two different commits

```git diff <branch1>..<branch2>``` ✅ Show the difference between two branches | branch1 will be - changes | branch2 will be + changes

#### 🌻 Remove files
```git rm <filename/s>``` ✅ Remove the tracked file from repository, git does not care about untracked files if removed but tracked already then need to remove from git as well --> Remove file directly or ask git to remove file

#### 🌻 Move / Rename files
```git mv <filename>``` ✅ Rename filename in git --> Rename file directly or ask git to rename file

```git mv <old-filepath> <new-filepath>``` ✅ Move a file from old-filepath to new-filepath


#### 🌻 Ignore files for project
- ".gitignore" file specifies intentionally untracked files that Git should ignore.
- Each line in a .gitignore file specifies pattern that match the rules.
- This is useful for files you know you NEVER want commit including Secrets, API Keys, credentials, OS files, log files, dependencies or packages.
- Ignore exact file name
  - .DS_Store
  - database/backup.sql
- Ignore all files in a directory with a trailing slash
  - /assets/videos/
  - /plugins/
- File Pattern
  - / directory separator
  - ** all directories or files inside a directory
  - * any character besides /
  - ? any one character besides /
  - [aeiou] or [0-9] a character in a set of characters
  - ! negates a file pattern
- A collection of useful .gitignore templates https://github.com/github/gitignore
- ```git help gitignore``` ✅ Get help around gitignore

#### 🌻 Ignore Files Globally
- Ignore files in all repositories
- User level settings instead of project level settings
```git config --global core.excludesFile <filePath>```
- Settings are not stored in project repository
- Settings are not shared with collaborators

#### 🌻 Track Empty Directories
By default, git ignores directories with no files
- Add a file (.gitkeep) to any "empty" directory you want to track

#### 🌻 Commit References
- SHA Hash - A unique 40 character identifier
- HEAD pointer reference
  - A reference to the tip of the current branch in the repository
  - Most recently stored state of the current branch
  - Points to the parent of the next commit, where writing new commits will occur
  - In a way, the HEAD pointer represents your current location inside the repository
  - ```cat .git/HEAD``` --> ```cat .git/refs/heads``` stores the reference to tip of branch (HEAD) | heads == # of branches
- Branch reference
- Tag reference
- Ancestry
  - ^ --> The prior commit
  - ~n --> nth prior commit (default 1)
  - commitID^ | HEAD^ | HEAD~1
  - commitID^^ | HEAD^^ | HEAD~2
  - ```git show -s --oneline HEAD~2```
  - ```git log --oneline HEAD~6..HEAD~3```

### ⛵ Git Branching
- Branches are inexpensive
  - Try new ideas 
  - Develop features separate from other work
- One working directory
- Git replaces file versions when branch changes
- Fast context switching

```git branch``` ✅ List all available branches, * represents the current branch

```git branch <branch-name>``` ✅ Create a new branch - branch-name

```git switch <branch-name>``` ✅ Switch from current branch to branch-name

```git branch -c <branch-name>``` ✅ Create and switch to a new branch | ```-c == --create```

```git merge-base <branch1> <branch2>``` ✅ It helps to identify the most recent common commit where the branches diverged, useful for understanding changes in a branch.

#### 🌻 Switching with Uncommited Changes
- ✅ Can switch when changes in working directory can be applied to branch version
- ✅ Can switch when changes in working directory are untracked or ignored files
- 👹 Can not switch when changes in working directory conflict with branch version

**How to switch:**
- Commit the changes to the current branch
- Remove the changes or restore the changed files
- Switch branches while also discarding the changes
- Stash the changes temporarily

#### 🌻 Renaming branches
Rename a branch

```git branch -m <old-name> <new-name>``` ✅ Rename a branch from old-name t- new-name

```git branch -m <new-name>``` ✅ Rename current branch to new-name

#### 🌻 Deleting branches
Delete a branch
- You can not delete a current branch 
- You can not delete uncommited/unmerged branch by default, but forcefully it can be deleted

```git branch -d <branch-name>``` ✅ Delete a branch with branch-name | ```-d == --delete```

```git branch -D <branch-name>``` ✅ Forcefully deleting a branch which is not merged.


