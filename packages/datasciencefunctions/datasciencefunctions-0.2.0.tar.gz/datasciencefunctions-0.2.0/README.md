# DataScienceFunctions

This repo contains common functions and code snippets to be reused on all projects in DataSentics. Some functionality is available
built into a Python package to be installed from notebooks or on clusters, the rest is available as examples to be copy-pasted as
needed. **Please note that everything in this repo can be shipped to customers, do not insert any sensitive data!**


### Quickstart
* Have a look at our
  [documentation](https://github.com/DataSentics/DataScienceFunctions/releases) (single archive, unzip it on your computer and open
  `index.html` in your browser).
* Download packaged [wheel file](https://github.com/DataSentics/DataScienceFunctions/releases) to upload into your workspace and
  `import datasciencefunctions`!
* Look at [example notebooks](https://dbc-8c8038b8-0e28.cloud.databricks.com/#notebook/3427/) to understand library functionality
  and to copy-paste some useful code snippets.
* Have some awesome piece of code? Learn [how to contribute](#how-to-contribute) to the project.

[//]: #  (## Getting started)


## Structure of the repository
This repository has multiple subdirectories, each serving a different purpose and thus containing different files. For library code,
there is the directory `datasciencefunctions/` which is built into a package using `setup.py`.  The files therein should be Python
source files with good code quality. Then there are example notebooks intended for showing the library functions on
simple-to-understand inputs and to store code snippets to be copied to your project and adjusted to your needs.  These are
Databricks notebooks exported as "Python". Here clarity is most important, some code quality rules can be ignored.  Finally, the
source files for building documentation and the resulting doc is in `docs`.


## Sub-modules
Here is a list of current submodules of the library (one submodule is one file in
`datasciencefunctions/`) along with their intended use. Note that this structure may
change over time depending on whether such change is needed and/or makes sense. Function
signatures should be (almost) set in stone once included in a release, where the function
is located within the library doesn't really need to. Keep in mind that the only reason
for us having submodules in the first place is to make it easier for people to orient
themselves in the library (i.e. not have everything in one giant file). That goes both for
developers and more importantly for users as well. In other words, functions should be
placed in such a submodule where a person would most likely look for them.

### classification
Contains functions to train and test classification models from start to finish,
and also log them into MLflow. Supports PySpark with the ability to add other frameworks
(e.g. Sci-kit learn) easily enough. Most functionality around AI/ML models goes here.

### common
Place for common, utility functions and types that can be used by other modules as well as
the end user's. Currently contains definition of an ML model type which simplifies
parametrization of classification pipelines by providing default values and information in
one place.

### data\_exploration
Intended for functionality useful when someone encounters a data set for the first time
and wants to do preliminary analysis. Has functions for automatically distinguishing
between categorical and continuous variables and for visualizing correlation between
the target variable and individual features.

### data\_processing
Once data is explored, it needs to be processed so that we can train models. Related
functionality, such as useful feature and dataframe ransformations, belongs here. Currently
has implementation of JLH score.

### modelling
Currently this module is somewhat of a duplicate of `classification` and might be merged
going forward. Contains LIFT curve calculation.

### online\_marketing
Because of online marketing being a distinct enough category, functionality specific for
it is here in its own submodule. Currently has transformation of URLs to format used by
AdForm.


## How to contribute
This section describes the general process of contributing to the repo. It is intended to be an overview, in case of any questions,
contact any of the repository admins or just ask on Slack. You will be prompted for credentials to our [company
GitHub](https://github.com/DataSentics/) when doing these steps. On Windows you will have to install some Git client such as [git
bash](https://git-scm.com/downloads), [GUI client](https://git-scm.com/download/gui/windows), or use [Windows Subsystem for
Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).


### Downloading local copy of the repository
1. Clone the repository to your local machine.

  ```shell
  cd /path/to/empty/project/directory
  git clone https://github.com/DataSentics/DataScienceFunctions.git ./
  ```
2. Verify by running `git status` command. The result should look something like the following:

  ```text
  On branch master
  Your branch is up to date with 'origin/master'.
  nothing to commit, working tree clean
  ```


### Contributing a piece of code
1. Make sure you are working with the latest version of code (expects you have already [cloned the
   repo](#downloading-local-copy-of-the-repository)).

  ```shell
  git pull
  ```

2. Switch to `master` branch. If in doubts, `git status` will tell you the current branch you are on.

  ```shell
  git checkout master
  ```

3. Create a new branch from `master`. Use a name that describes the new functionality (e.g. `feature-correlation-visualizations`).

  ```shell
  git checkout -b new-branch-name
  ```

4. Create changes by putting your awesome new functions to some files (see [repo structure](#structure-of-the-repository)).

5. (Optional but welcome): [Format the code](#code-formatting) to be compliant with our guidelines.

6. Create a new commit (snapshot of the current state of repository). You can see which files were changed by running `git status`.
   Your default text editor will open to write commit message (if unsure, consult [resources on git](#git-tutorials)).

   ```shell
   git add changed-file-1 changed-file-2 ...
   git commit
   ```
7. Upload your changes to the GitHub so that others can see them.

   ```shell
   git push
   ```

8. Let people on Slack know that you contributed to the awesomeness, ideally
   some repo maintainer or in `#data-science-functions-library`.


## Useful resources


### Git tutorials
* **Intro:** an [interactive tutorial](https://learngitbranching.js.org/) to get you sorted out and ready to git in a simple,
  beginner-friendly way.
* **Workflow:** this project currently follows [GitHub flow](https://guides.github.com/introduction/flow/) as a simple, lightweight
  git workflow. In summary, when adding new functionality, create new feature branch from master, make changes and create pull
  request to merge them back to master.
* **Commit messages:** [good commit message](https://chris.beams.io/posts/git-commit/) enables orienting yourself quickly in what
  has been done. Bad commit message means wild goose chase through the history trying to find out what the hell those changes even
  were.
* **beautiful pythonic code:** please follow [PEP8](https://www.python.org/dev/peps/pep-0008/), more on code formatting in [relevant
  section](#code-formatting).


### Code formatting
This section provides information on some of the DOs and DON'Ts for writing code in a beautiful, pythonic way. Writing nice code
pays the effort back in frustration you didn't have to feel and bugs you didn't have to solve. The basis for beautiful in Python is
[PEP8](https://www.python.org/dev/peps/pep-0008/), feel free to keep it under your pillow. Our repo has configuration files for
*Flake8* so syntax and formatting checks can be done automatically if you have it installed.

The best method of documentation is **self-documenting code**, i.e. using descriptive variable and function names so that their
meaning is immediately obvious!

```python
# DON'T
l = [(1, 5, 17), (209, 87, 15)]
for i in len(l):
    print(l[i][0])

# DO
rgbs = [(1, 5, 17), (209, 87, 15)]
for red, _, _ in rgbs:
    print(red)
```

When writing functions, please follow these guidelines as illustrated in the example: good naming conventions and correctly
formatted docstrings (we also use them for building documentation). The target user should know what the function does just by
looking at its name, parameters names, and short description. If not, they have to waste time reading the implementation.

```python
def short_descriptive_name(par_1 : type, par_2 : type = default_value):
    '''short description of the function

    Longer description, can include links to further reading on the subject.
    Shouln't be just restating how the function was implemented. Remember, the
    goal here is for the user to orient themselves quickly, not read a treatise
    on the subject.

    :param par_1: parameter description
    :param par_2: another parameter description

    :return: return value description
    '''

    # function code...
```

Use correct line wrapping. Maximum 132 characters on a line, [PEP8 compliant continuation
indentation](https://www.python.org/dev/peps/pep-0008/#indentation) (aligning vertically is preferred). Good line-wrapping makes the
code much more readable.

```python
# DON'T
result = spark.table('tablename').select('foo', 'bar', 'baz').groupBy('foo').agg(F.count('*').alias('count'), F.avg('bar').alias('avg_bar'), F.max('baz').alias('max_baz'))

# DO
result = (spark
          .table('tablename')
          .select('foo', 'bar', 'baz')
          .groupBy('foo')
          .agg(F.count('*').alias('count'),
               F.avg('bar').alias('avg_bar'),
               F.max('baz').alias('max_baz')
               )
          )
```


## For developers and maintainers
This section contains more technical information not needed by the general user.


### Documentation building
Currently we are using *Sphinx*, to build the documentation, run
```shell
make build_doc
```
If you add new files, please make sure to add them to the index file in docs (aka table of contents). Automatic detection of files
(or that they are missing from docs) is not implemented yet.

### Package building
There is Makefile for building packages, just run
```shell
make build_wheel
```

### Syntax check and static code analysis
We have a linter set up, run
```shell
make run_linter
```
to have *flake8* perform check. It's done in CI/CD but if you don't want to get spammed and have everything set up on your local
machine, run it before pushing the code to GitHub.


## TODOs and wishlist
* update this wishlist, or preferably move it to Jira...
* more functionality!
* more tests
* automatic builds on GitHub (automatically for each new commit in master branch)
  * deploy all built items to GitHub Packages / elsewhere (currently done manually)
  * deploy example notebooks to Databricks and run them (through databricks-cli?)
* license??

