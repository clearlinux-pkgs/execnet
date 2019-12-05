#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : execnet
Version  : 1.7.1
Release  : 45
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

%description python3
python3 components for the execnet package.


%prep
%setup -q -n execnet-1.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567180384
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
cp LICENSE %{buildroot}/usr/share/package-licenses/execnet/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/execnet/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
