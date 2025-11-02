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

- **Atomic Commits**
  - You must decide how to group changes
  - Make small commits when possible
  - Focus commits on a single concept
  - Several commit messages will make sets of changes easier to understand
  - Each commit will contain exclusively a set of changes related to a single task or purpose
  - Improves collaboration and branch management
  - Easier to find bugs

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

```git diff --word-diff=color``` ✅ Show the difference of only changed words in simple format

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

```git branch <created-branch> <to-be-created-branch>``` ✅ Create "to-be-created-branch" from "created-branch"

```git branch --merged``` ✅ List the branches which are fully merged with current branch

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

### ⛵Git Merging
git merge is a Git command used to combine changes from one branch into another, creating a unified history. It’s how you bring together parallel lines of development in a project.

#### 🌻 **What git merge Does**
Combines branches: It takes the commits from a source branch (e.g., feature-branch) and integrates them into the target branch (e.g., main).

Preserves history: Unlike git rebase, merging doesn’t rewrite commit history—it keeps the original commits intact.

Creates a merge commit (in most cases): This special commit has two parent commits, representing the point where the branches joined.

```git merge <branch-name>``` ✅ Merge branch-name into current branch

- If there are no conflicts, Git will automatically create a merge commit. 
- If there are conflicts, Git will pause and ask you to resolve them manually.

#### 🌻 Types of Merges
**Fast-forward merge:** Happens when the target branch has no new commits since the source branch diverged. Git just moves the branch pointer forward.

**Three-way merge:** Happens when both branches have new commits. Git creates a new merge commit to tie them together.

#### 🌻 Resolving Merge Conflicts
1. Abort Merge ✅
2. Resolve conflicts manually ✅
3. Use a merge tool ✅ 

```git merge --abort``` ✅ Abort the ongoing merge

#### 🌻 Strategies to Reduce Conflicts
1. keep line lengths short
2. Make atomic commits, small and focused
3. Beware of edits to whitespace characters
4. Merge frequently

### ⛵Local and Remote Repositories
1. Local Git repositories do not require a network connection
2. Remote repositories (remotes) are hosted by servers over a network
3. Remotes allow easy collaboration
4. Push local repository changes to the remote
5. Fetch remote changes to the local repository
6. All repositories have qual authority
7. One remote is often designated as the primary repository for collaboration

```git remote add <origin> <URL>``` ✅ Configure remote URL to refer with origin

```git remote``` ✅ List the name of remote referencing URL

```git remote -v``` ✅ List the details about configured remote

```git branch -r``` ✅ List all remote branches

```git branch -a``` ✅ List all local and remote branches

```git remote rm <remote-name>``` ✅ Delete the remote

```git remote rename <old-remote-name> <new-remote-name>``` ✅ Rename old remote with new remote name

```git remote show <remote-name>``` ✅ Fetch details about remote repository

#### 🌻 Clone Remote Repository
1. Collaborators need access to the remote
2. owner must grant access to primate repositories
3. Collaborators must clone repository

```git clone <remote-url>``` ✅ Clone a remote project by keeping the same project name as directory

```git clone <remote-url> <direcotry-name>``` ✅ Clone a remote project from remote-url and create a project with directory-name

#### 🌻 Remote Repository Tracking
- Local branch follows a remote branch closely 
- Where to watch for new commits by default 
- Where to send your commits by default 
- Upstream branch and remote tracking branch are related 
- Upstream is set for local branches
  - When created from remote branches
  - When pushed to a remote if -u option is included
- Git can be configured to set upstream on push by default

```git log <remote-branch> -N``` ✅ List last N logs from the remote-branch like remote/main

```git config --global push.autoSetupRemote true``` ✅ Setup remote push automatically

```git push <remote-name> <local-branch>:<remote-branch>``` ✅ Push local <branch-name> to remotely hosted remote-branch

```git push -u <origin> <branch-name>``` ✅ Setup upstream for remote branch

```git push``` ✅ Once upstream is configured for specific local to remote branch then git push is enough to push changes

```git push -f``` ✅ Push forcefully but not recommended

#### 🌻 Git Fetching - Pulling
git fetch downloads the latest changes from a remote repository but does not merge them into your local branch, while git pull does the same fetch and immediately merges (or rebases) those changes into your current branch.

**git fetch**
- Contacts the remote repository (like origin)
- Downloads new commits, branches, and tags 
- Updates your local remote-tracking branches (e.g., origin/main)
- It doesn’t change your working files or current branch.
- Use case:
  - When you want to see what others have pushed before merging it into your work. 
  - Safe for inspection: you can review changes with git log origin/main or git diff main origin/main.

**git pull**
- Runs git fetch first 
- Then automatically merges (or rebases, if configured) the fetched changes into your current branch 
- git pull = git fetch + git merge
- Your working directory is updated immediately with remote changes. 
- Use case:
  - When you’re ready to integrate remote updates into your branch in one step.

**💡 Best Practices**
- Use git fetch if you want control: review changes first, then decide whether to merge or rebase. 
- Use git pull if you’re confident and want to stay up-to-date quickly. 
- Many teams prefer git fetch + git merge (or git rebase) for clarity and fewer surprises.

```git fetch <remote-name>``` ✅ Fetch changes from remote-name, remote-name is optional if already configured

```git pull <remote-name> <branch-name>``` ✅ Pull = fetch and merge changes from remote branch into local branch

#### 🌻 Delete a remote branch
- Deletes the branch from remote repository
- Deletes your remote-tracking branch
- Does not delete any other local branches
- Does not change collaborator repositories
- Useful when a feature branch is complete and merged

```git push -d <remote-name> <branch-name>``` ✅ Delete a remote branch

```git remote prune <remote-name>``` ✅ Prune locally available remote branches | optionally --dry-run option allows previewing the branches that will be pruned without making any changes.

#### 🌻 **Collaboration Types**
- Private Projects
  - Grant individual read and write access
- Open Source Projects
  - World has read access
  - project leaders have write access

### Git Tags
In Git, a tag is a reference that points to a specific commit, often used to mark important points in history like releases (v1.0, v2.0). 

- A tag is like a bookmark for a commit. 
- It doesn’t move (unlike branches) — once created, it always points to the same commit. 
- Commonly used for versioning software releases (e.g., v1.0.0, release-2025-11-03). 
- Helps developers and CI/CD pipelines identify stable points in the project’s history.

There are two main types of tags: lightweight and annotated.

#### 🌻 **Lightweight Tag**
- Acts like a simple pointer to a commit. 
- Contains only the commit checksum (no extra metadata). 
- Created quickly, often for temporary or local use.
- Think of it as a sticky note on a commit.

```git tag <tag-name>``` ✅

#### 🌻 **Annotated Tag**
- 