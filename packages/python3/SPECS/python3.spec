Summary: WIP spec for python 3.8
Name: python3
Version: 3.8.1
Release: 2wip%{?dist}
License: GPLv3+
URL: https://www.python.org
Source: https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz

Provides: python3, python3-devel
Provides: %{_bindir}/python
Provides: %{_bindir}/python3
Provides: %{_bindir}/python3.8
Provides: %{_bindir}/python3-config
Provides: %{_bindir}/python3.8-config

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: python-rpm-macros

Patch0: python-3.8.1-irix.patch
Patch1: python-3.8.1-syspath-lib32.patch
Patch2: python-3.8.1-more-lib32.patch
Patch3: python-3.8.1-even-more-lib32.patch

%description
A minimal port of python 3.8.1 against sgug-rse.

%prep

%setup -q -n Python-%{version}
%patch0 -p1 -b .3.8.1-irix~
%patch1 -p0 -b .3.8.1-irix~
%patch2 -p1 -b .3.8.1-irix~
%patch3 -p1 -b .3.8.1-irix~

# Rewrite hardcoded paths causing unwanted Requires
perl -pi -e "s|/usr/local/bin/python|%{_bindir}/python|g" Lib/cgi.py

perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" Doc/library/pathlib.rst
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" Lib/test/test_*.py
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" Lib/test/cfgparser.2
perl -pi -e "s|/bin/bash|%{_bindir}/bash|g" Lib/test/ziptestdata/header.sh

%build
#export LDFLAGS="-lpthread -Wl,-rpath -Wl,%{_libdir}"
export ac_cv_func_strsignal=no
%{configure} --enable-shared
# this can't be set through configure
X=`mktemp`
sed 's,^SCRIPTDIR.*$,SCRIPTDIR=     $(prefix)/lib32,g' < Makefile > $X
cat $X > Makefile
rm -f $X
make %{?_smp_mflags}

%check
# Do the tests by hand
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'
# ugly, but can't be done otherwise
tar -C $RPM_BUILD_ROOT%{_prefix}/lib/python3.8/ -cf - . | tar -C $RPM_BUILD_ROOT%{_libdir}/python3.8/ -xvf -
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib

# Setup a symbolic link so that we "provide" %{_bindir}/python
export PREV_WD=`pwd`
cd $RPM_BUILD_ROOT%{_bindir}
ln -s python3 python
cd $PREV_WD

# Remove some ugly archives containing hard references to bash
rm $RPM_BUILD_ROOT%{_libdir}/python3.8/test/ziptestdata/exe_with_z64
rm $RPM_BUILD_ROOT%{_libdir}/python3.8/test/ziptestdata/exe_with_zip

%files
%{_bindir}/*
%{_libdir}/libpython3*
%{_libdir}/pkgconfig/*
%{_libdir}/python3.8/*

%{_prefix}/include/python3.8/*
%{_prefix}/man/*

%changelog
* Sun Apr 12 2020 Daniel Hams <daniel.hams@gmail.com> - 3.8.1-2
- Rename to python3, Provides: of python3 and python3-devel
  Fix up hardcoded paths + bug fix to system lib path

* Sat Feb 15 2020 Erno Palonheimo <esp@iki.fi> - 3.8.1-1
- Initial attempt at spec
