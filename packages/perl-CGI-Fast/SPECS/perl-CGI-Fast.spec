Name:           perl-CGI-Fast
Version:        2.15
Release:        3%{?dist}
Summary:        CGI Interface for Fast CGI
# lib/CGI/Fast.pm probably qotes piece of Artistic license before declaring
# "as Perl itself" <https://github.com/leejo/cgi-fast/issues/13>
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CGI-Fast
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-Fast-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(CGI) >= 4.00
BuildRequires:  perl(CGI::Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(FCGI) >= 0.67
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(deprecate)
Requires:       perl(CGI) >= 4.00
Requires:       perl(FCGI) >= 0.67
# perl-CGI-Fast was split from perl-CGI
Conflicts:      perl-CGI < 4.00

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((CGI|FCGI)\\)$

%description
CGI::Fast is a subclass of the CGI object created by CGI.pm. It is
specialized to work well FCGI module, which greatly speeds up CGI scripts
by turning them into persistently running server processes. Scripts that
perform time-consuming initialization processes, such as loading large
modules or opening persistent database connections, will see large
performance improvements.

%prep
%setup -q -n CGI-Fast-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-2
- Perl 5.30 rebuild

* Mon Apr 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.15-1
- 2.15 bump

* Tue Mar 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-1
- 2.14 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Petr Pisar <ppisar@redhat.com> - 2.13-1
- 2.13 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-1
- 2.12 bump

* Mon Nov 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-1
- 2.11 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.10-1
- 2.10 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-2
- Perl 5.22 rebuild

* Thu Mar 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-1
- 2.09 bump

* Mon Feb 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-1
- 2.07 bump

* Wed Jan 14 2015 Petr Pisar <ppisar@redhat.com> - 2.05-2
- Specify run-time dependency versions

* Mon Dec 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-1
- 2.05 bump

* Wed Dec 10 2014 Petr Pisar <ppisar@redhat.com> - 2.04-2
- Do not load Test::Deep where not needed
- Make Test::Deep tests optional as it's not in the core in contrast to the
  CGI-Fast

* Mon Oct 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-1
- 2.04 bump

* Wed Sep 10 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-1
- 2.03 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-2
- Perl 5.20 rebuild

* Mon Jun 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-1
- 2.02 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-1
- 2.01 bump

* Mon May 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- Specfile autogenerated by cpanspec 1.78.
