# Disable support for Carp-Datum because it is Artistic 1 only, CPAN RT#105332
%bcond_with datum

Name:           perl-Log-Agent
Version:        1.003
Release:        7%{?dist}
Summary:        Logging agent
License:        Artistic 2.0
URL:            https://metacpan.org/release/Log-Agent
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
# Carp::Datum not needed at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Mail::Mailer not needed at tests
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Sys::Syslog not needed at tests
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Callback)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(warnings)

%description
The Log::Agent Perl module provides an abstract layer for logging and tracing,
which is independent from the actual method used to physically perform those
activities. It acts as an agent (hence the name) that collects the requests
and delegates processing to a logging driver.

%if %{with datum}
%package Carp-Datum
Summary:        Carp::Datum driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Carp::Datum)

%description Carp-Datum
The purpose of this logging driver is to cooperate with Carp::Datum by emitting
traces to the debug channel via Carp::Datum's traces facilities.
%endif

%package mail
Summary:        E-mail driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description mail
This logging driver maps the log calls to email messages.  Each call generates
a separate email message.

%package syslog
Summary:        Syslog driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)

%description syslog
This logging driver delegates log operations to syslog() via the
Sys::Syslog interface.

%prep
%setup -q -n Log-Agent-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGELOG.md README
%{perl_vendorlib}/*
%{_mandir}/man3/*
# Carp-Datum
%exclude %{perl_vendorlib}/Log/Agent/Driver/Datum.pm
%exclude %{_mandir}/man3/Log::Agent::Driver::Datum.*
# mail
%exclude %{perl_vendorlib}/Log/Agent/Driver/Mail.pm
%exclude %{_mandir}/man3/Log::Agent::Driver::Mail.*
# syslog
%exclude %{perl_vendorlib}/Log/Agent/Channel/Syslog.pm
%exclude %{perl_vendorlib}/Log/Agent/Driver/Syslog.pm
%exclude %{_mandir}/man3/Log::Agent::Channel::Syslog.*
%exclude %{_mandir}/man3/Log::Agent::Driver::Syslog.*

%if %{with datum}
%files Carp-Datum
%{perl_vendorlib}/Log/Agent/Driver/Datum.pm
%{_mandir}/man3/Log::Agent::Driver::Datum.*
%endif

%files mail
%{perl_vendorlib}/Log/Agent/Driver/Mail.pm
%{_mandir}/man3/Log::Agent::Driver::Mail.*

%files syslog
%{perl_vendorlib}/Log/Agent/Channel/Syslog.pm
%{perl_vendorlib}/Log/Agent/Driver/Syslog.pm
%{_mandir}/man3/Log::Agent::Channel::Syslog.*
%{_mandir}/man3/Log::Agent::Driver::Syslog.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Petr Pisar <ppisar@redhat.com> - 1.003-1
- 1.003 bump

* Mon Oct 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-1
- 1.002 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Petr Pisar <ppisar@redhat.com> - 1.001-1
- 1.001 bump

* Thu Jun 18 2015 Petr Pisar <ppisar@redhat.com> 1.000-1
- Specfile autogenerated by cpanspec 1.78.
