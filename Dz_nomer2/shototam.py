import git

g = git.cmd.Git("D:\Lessons\Python")
g.pull()
print(g.status())
g.branch("tmp/123")