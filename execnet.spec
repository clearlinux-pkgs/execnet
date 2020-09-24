#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : execnet
Version  : 1.7.1
Release  : 49
URL      : https://files.pythonhosted.org/packages/5a/61/1b50e0891d9b934154637fdaac88c68a82fd8dc5648dfb04e65937fc6234/execnet-1.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/61/1b50e0891d9b934154637fdaac88c68a82fd8dc5648dfb04e65937fc6234/execnet-1.7.1.tar.gz
Summary  : execnet: rapid multi-Python deployment
Group    : Development/Tools
License  : MIT
Requires: execnet-license = %{version}-%{release}
Requires: execnet-python = %{version}-%{release}
Requires: execnet-python3 = %{version}-%{release}
Requires: apipkg
BuildRequires : apipkg
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
execnet: distributed Python deployment and communication
========================================================

Important
---------

**execnet currently is in maintenance-only mode, mostly because it is still the backend
of the pytest-xdist plugin. Do not use in new projects.**

.. image:: https://img.shields.io/pypi/v/execnet.svg
    :target: https://pypi.org/project/execnet/

.. image:: https://anaconda.org/conda-forge/execnet/badges/version.svg
    :target: https://anaconda.org/conda-forge/execnet

.. image:: https://img.shields.io/pypi/pyversions/execnet.svg
    :target: https://pypi.org/project/execnet/

.. image:: https://travis-ci.org/pytest-dev/execnet.svg?branch=master
    :target: https://travis-ci.org/pytest-dev/execnet

.. image:: https://ci.appveyor.com/api/projects/status/n9qy8df16my4gds9/branch/master?svg=true
    :target: https://ci.appveyor.com/project/pytestbot/execnet

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

.. _execnet: http://codespeak.net/execnet

execnet_ provides carefully tested means to ad-hoc interact with Python
interpreters across version, platform and network barriers.  It provides
a minimal and fast API targetting the following uses:

* distribute tasks to local or remote processes
* write and deploy hybrid multi-process applications
* write scripts to administer multiple hosts

Features
------------------

* zero-install bootstrapping: no remote installation required!

* flexible communication: send/receive as well as
  callback/queue mechanisms supported

* simple serialization of python builtin types (no pickling)

* grouped creation and robust termination of processes

* well tested between CPython 2.7, 3.4+, Jython 2.5.1 and PyPy 2.2
  interpreters.

* interoperable between Windows and Unix-ish systems.

* integrates with different threading models, including standard
  os threads, eventlet and gevent based systems.

%package license
Summary: license components for the execnet package.
Group: Default

%description license
license components for the execnet package.


%package python
Summary: python components for the execnet package.
Group: Default
Requires: execnet-python3 = %{version}-%{release}

%description python
python components for the execnet package.


%package python3
Summary: python3 components for the execnet package.
Group: Default
Requires: python3-core
Provides: pypi(execnet)

%description python3
python3 components for the execnet package.


%prep
%setup -q -n execnet-1.7.1
cd %{_builddir}/execnet-1.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582922204
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/execnet
cp %{_builddir}/execnet-1.7.1/LICENSE %{buildroot}/usr/share/package-licenses/execnet/82dbfd684f7c04da81d4faa852c6317142daa3e7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/execnet/82dbfd684f7c04da81d4faa852c6317142daa3e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
