Summary: WIP spec for python 3.8
Name: python38-wip
Version: 3.8.1
Release: 1wip%{?dist}
License: GPLv3+
URL: https://www.python.org
Source: https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz

BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

AutoReqProv: 0

Patch0: python-3.8.1-irix.patch

%description
A minimal port of python 3.8.1 against sgug-rse.

%prep

%setup -q -n Python-%{version}
%patch0 -p1 -b .3.8.1-irix~

%build
export LDFLAGS="-lpthread -Wl,-rpath -Wl,%{_libdir}"
%{configure} --enable-shared
make %{?_smp_mflags}

%check
# Do the tests by hand
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

%files
%{_bindir}/*
%{_libdir}/libpython3*
%{_libdir}/pkgconfig/*
%{_libdir}/python3.8/*
%{_prefix}/lib/python3.8/*
%{_prefix}/include/python3.8/*
%{_prefix}/man/*

%changelog
* Sat Feb 15 2020 Erno Palonheimo <esp@iki.fi> - 0.0.1
- Initial attempt at spec

