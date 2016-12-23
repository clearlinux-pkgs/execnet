#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : execnet
Version  : 1.4.1
Release  : 14
URL      : https://pypi.python.org/packages/source/e/execnet/execnet-1.4.1.tar.gz
Source0  : https://pypi.python.org/packages/source/e/execnet/execnet-1.4.1.tar.gz
Summary  : execnet: rapid multi-Python deployment
Group    : Development/Tools
License  : MIT
Requires: execnet-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
Welcome to execnet and elastic distributed computing!
Rapidly deploy tools and code to local or remote Python interpreters.

%package python
Summary: python components for the execnet package.
Group: Default

%description python
python components for the execnet package.


%prep
%setup -q -n execnet-1.4.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
