# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pushd: "push" directory to a stack, saved for later use
popd: "pop" directory off said stack to recall saved folder
cat: streams out the contents of a file as text
less: view "less" of a long file or list of files/directories, so that it doesn't print out a huge stream of text and you can browse it at your leisure
grep: searches for a specific string in a file or list of files
man: manual for any function, will use this one a lot!
env: print out all environment variables
export: define a new environment variable or change an existing one
unset: the opposite of export - remove an environment variable
echo: print a certain string or variable text


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls: list all files in directory
ls -a: list all files in directory, including ones that start with . and ..
ls -l: List all files in directory in long list format, meaning there is more than just the file name: created by, modified by, last modified date, and more
ls -lh: List all files in long list format, and the "total" line will display a human-readable size total for all files listed.
ls -lah: List all files in directory in long list format, including ones that begin with . and .., with human-readable size totals
ls -t: List all files in directory sorted by when they were last modified, newest first
ls -Glp: Print a long list format of files in directory, with no group names and directories identified with a / at the end


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -1: Prints everything on a new line! Might be handy for iterating through a list to use in Python?
-m: displays as comma-separated list, equally useful for listing and iterating.
-R: Useful for seeing how a folder has many subfolders, can combine with -lh to see total directory size.
-q: Good for foreign characters (UTF-16, asian language, etc.) that might otherwise bog down or produce some squirrely results, or bomb out when dumped into a UTF-8 database.
-r: For iterating backwards? Not sure how this would be used but it's neat.


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs breaks commands up into a list separated by whatever the user specifies. It is used if you want to control the output of how you receive a list of items back to you, and seems to have a lot more custom usability than built-in subsets of commands. 

Ex: $ echo 1 2 3 4 5 6 | xargs -n 2

xargs splits the echo'd text into lines of 2 numbers each via this functionality, so the result looks like this:

1 2
3 4
5 6

 

