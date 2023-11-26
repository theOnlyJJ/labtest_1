1st git init (check if its inside folder)

2nd git add <file name>

EG.git add HelloWorld.py

3rd git status

check status

4th git commit -m "version"

5th git status

should state nothing to commit since commited

-----------------------------------------------------------------

Addtional:git diff
Show changes to the file

git branch 
Shows all branches and status

git branch <new branch name>
EG. git  branch "bug-fix1"
-Adds new branch

git checkout 
EG. git checkout "bug-fix1"

git merge <branch to be merged>
EG. git merge "bug-fix1"
overwrites the main branch with the sub branch

------------------------------------------------------------------
linking of github

git remote add origin <GitHub repository URL from Step 5.5>

Example:git remote add origin https://gitHub.com/kweetecktanichat/Lab1.git

git remote -v 
to check status of repo

git push --set-upstream origin master 
This will set the upstream and push the master branch. 

git push -u origin

*if cannot push use*
git push -f origin <branch-name> 
this force push the file
*if still cannot*
git pull origin master --allow-unrelated-histories

--------------------------------------------------------------------
Readme,Tagging,release and submodules

Readme - Create a Readme.md file in the chosen directory

1st git add Readme.md
git commit -m "Readme"
git push -u origin

Tagging - mark collection of files

git tag –a <tag> –m <comment>
EG. git tag -a v1.0 -m "Initial release v1.0"
git push origin v1.0
pushes tag to repository and tag symbol should be 1

Release- Click the “Create a new release” button. Click “Choose a tag”, and select “v1.0”. 
In the “Release title” field, enter “ET0735_Lab1_Code_v1.0” (or whatever text 
you prefer). In the “Describe this release” field, enter two lines of text: “Initial 
release v1.0”, and “Date: {today’s date}”.

submodule - 1st git submodule add <Git submodule repository URL> 
Example: git submodule add https://github.com/ET0735-DevOps-AIoT/Lab1_submodule.git
This will clone a submodule over to the chosen directory

2nd git add <submodule file name>
3rd git commit -m "s-module"
4th git push -u origin

----------------------------------------------------------------------
git clone <URL of repository to clone>
*Individual file*
1st git add <file name>
2nd git commit -m "line 2"
3rd git push -u origin
*multiple file*

1st git add .
2nd git commit -m "line 2"
3rd git push -u origin