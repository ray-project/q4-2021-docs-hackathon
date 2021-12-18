# Building Ray on Windows

## Requirements

The following links were correct during the writing of this section. In
case the URLs changed, search at the organizations' sites.

-   bazel 4.2 (<https://github.com/bazelbuild/bazel/releases/tag/4.2.1>)
-   Microsoft Visual Studio 2019 (or Microsoft Build Tools 2019 -
    <https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019>)
-   JDK 15
    (<https://www.oracle.com/java/technologies/javase-jdk15-downloads.html>)
-   Miniconda 3 (<https://docs.conda.io/en/latest/miniconda.html>)
-   git for Windows, version 2.31.1 or later
    (<https://git-scm.com/download/win>)

## Steps

1.  Enable Developer mode on Windows 10 systems. This is necessary so
    git can create symlinks.
    1.  Open Settings app;
    2.  Go to "Update & Security";
    3.  Go to "For Developers" on the left pane;
    4.  Turn on "Developer mode".
2.  Add the following Miniconda subdirectories to PATH. If Miniconda was
    installed for all users, the following paths are correct. If
    Miniconda is installed for a single user, adjust the paths
    accordingly.
    -   `C:\ProgramData\Miniconda3`
    -   `C:\ProgramData\Miniconda3\Scripts`
    -   `C:\ProgramData\Miniconda3\Library\bin`
3.  Define an environment variable BAZEL_SH to point to bash.exe. If git
    for Windows was installed for all users, bash's path should be
    `C:\Program Files\Git\bin\bash.exe`. If git was installed for a
    single user, adjust the path accordingly.

4. Bazel 4.2 installation. Go to bazel 4.2 release web page and
download bazel-4.2.1-windows-x86_64.exe. Copy the exe into the directory
of your choice. Define an environment variable BAZEL_PATH to full exe
path (example: `set BAZEL_PATH=C:\bazel\bazel.exe`). Also add the bazel
directory to the `PATH` (example: `set PATH=%PATH%;C:\bazel`)

5.  Install cython and pytest:

``` shell
pip install cython==0.29.0 pytest
```

6.  Download ray source code and build it.

``` shell
# cd to the directory under which the ray source tree will be downloaded.
git clone -c core.symlinks=true https://github.com/ray-project/ray.git
cd ray\python
pip install -e . --verbose
```
