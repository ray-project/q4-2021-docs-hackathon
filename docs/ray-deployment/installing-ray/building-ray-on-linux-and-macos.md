# Building Ray on Linux and macOS

**Tip:** If you are only editing Tune/RLlib/Autoscaler files, follow instructions
for `python-develop` to avoid long build times.

To build Ray, first install the necessary dependencies by running the following commands:



For Ubuntu, run the following commands:

=== "Ubuntu"

    ``` bash
    sudo apt-get update
    sudo apt-get install -y build-essential curl unzip psmisc

    pip install cython==0.29.0 pytest
    ```

=== "RHELv8 (Redhat EL 8.0-64 Minimal)"

    ``` bash
    sudo yum groupinstall 'Development Tools'
    sudo yum install psmisc

    pip install cython==0.29.0 pytest
    ```

Install bazel manually from link:
<https://docs.bazel.build/versions/main/install-redhat.html>

=== "macOS"

    ``` bash
    brew update
    brew install wget

    pip install cython==0.29.0 pytest
    ```

**Tip:** Assuming you already have brew and bazel installed on your mac and you
also have grpc and protobuf installed on your mac consider removing
those (grpc and protobuf) for smooth build through commands
`brew uninstall grpc`, `brew uninstall protobuf`. If you have built the
source code earlier and it still fails with error as
`No such file or directory:`, try cleaning previous builds on your host
by running commands `brew uninstall binutils` and
`bazel clean --expunge`.

Ray can be built from the repository as follows.

``` bash
git clone https://github.com/ray-project/ray.git

# Install Bazel.
ray/ci/travis/install-bazel.sh
# (Windows users: please manually place Bazel in your PATH, and point
# BAZEL_SH to MSYS2's Bash: ``set BAZEL_SH=C:\Program Files\Git\bin\bash.exe``)

# Build the dashboard
# (requires Node.js, see https://nodejs.org/ for more information).
pushd ray/dashboard/client
npm install
npm run build
popd

# Install Ray.
cd ray/python
pip install -e . --verbose  # Add --user if you see a permission denied error.
```

The `-e` means "editable", so changes you make to files in the Ray
directory will take effect without reinstalling the package.

**Warning:** if you run `python setup.py install`, files will be copied from the Ray
directory to a directory of Python packages
(`/lib/python3.6/site-packages/ray`). This means that changes you make
to files in the Ray directory will not have any effect.

