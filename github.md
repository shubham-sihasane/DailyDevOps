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

👹 .gitignore file specifies intentionally untracked files that Git should ignore. Each line in a .gitignore file specifies a pattern. This is useful for files you know you NEVER want commit including Secrets, API Keys, credentials, OS files, log files, dependencies or packages. 

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

### ⛵ Basic Git Workflow
1. Working Directory (Work On Stuff) --> Make new files, edit files, delete files etc.
2. Staging Area (Add/Remove Stuff) --> Group specific changes together, in preparation of commiting.
3. Repository (Permanent Stuff) --> Commit everything that was previously added.

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



