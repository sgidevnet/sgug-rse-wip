Summary: Work in progress spec for EXAMPLE-WIP
Name: example-wip
Version: 0.0.1
Release: 1wip%{?dist}
License: GPLv3+
URL: https://path/to/project/site
Source: https://path/to/project/site/download/%{version}/example-wip-%{version}.tar.bz2

# Just some standard bits
BuildRequires: gcc
BuildRequires: automake, autoconf, libtool, pkgconfig

# Here's where you add parents you need in place
#Requires: parentproject

%description
A work in progress for EXAMPLE-WIP

%prep
# You can omit the "-n example-wip-%{version}" here as it's the default
# this is just to show how you'd specific a particular extracted package dir
%setup -q -n example-wip-%{version}

%build
%{configure}
make %{?_smp_mflags}

%check
# Do the tests by hand
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

# Here you add removes for stuff you don't want included
# example to remove doc
# rm -rf $RPM_BUILD_ROOT%{_prefix}/BLAH

%files
# If you have programs
#%{_bindir}/*
# If you have libraries
#%{_libdir}/*
# other stuff, add the relative paths here

%changelog
* Tue Jan 7 2020 sgug <contact@sgug.sh> - 0.0.1
- First build
