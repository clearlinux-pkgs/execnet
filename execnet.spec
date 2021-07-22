#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : execnet
Version  : 1.9.0
Release  : 61
URL      : https://files.pythonhosted.org/packages/7a/3c/b5ac9fc61e1e559ced3e40bf5b518a4142536b34eb274aa50dff29cb89f5/execnet-1.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/3c/b5ac9fc61e1e559ced3e40bf5b518a4142536b34eb274aa50dff29cb89f5/execnet-1.9.0.tar.gz
Summary  : execnet: rapid multi-Python deployment
Group    : Development/Tools
License  : MIT
Requires: execnet-license = %{version}-%{release}
Requires: execnet-python = %{version}-%{release}
Requires: execnet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
========================================================
        
        Important
        ---------
        
        **execnet currently is in maintenance-only mode, mostly because it is still the backend
        of the pytest-xdist plugin. Do not use in new projects.**

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
%setup -q -n execnet-1.9.0
cd %{_builddir}/execnet-1.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623681173
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/execnet
cp %{_builddir}/execnet-1.9.0/LICENSE %{buildroot}/usr/share/package-licenses/execnet/82dbfd684f7c04da81d4faa852c6317142daa3e7
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
