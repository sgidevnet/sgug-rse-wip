# Perform optional tests
%bcond_without perl_Devel_PPPort_enables_optional_test

Name:           perl-Devel-PPPort
Version:        3.52
Release:        440%{?dist}
Summary:        Perl Pollution Portability header generator
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-PPPort
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Devel-PPPort-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.3
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)
%if %{with perl_Devel_PPPort_enables_optional_test} && !%{defined %perl_bootstrap}
# Optional tests:
# File::Spec not helpful
# Test has a fallback
BuildRequires:  perl(Test::Pod) >= 0.95
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C name space
environment (reduced pollution). The header file written by this module,
typically ppport.h, attempts to bring some of the newer Perl API features
to older versions of Perl, so that you can worry less about keeping track
of old releases, but users can still reap the benefit.

%{?perl_default_filter}

%prep
%setup -q -n Devel-PPPort-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset PERL_CORE SKIP_SLOW_TESTS
make regen_tests
make test

%files
# README.md is useless
%doc Changes HACKERS README soak TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.52-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.52-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.52-438
- Increase release to favour standalone package

* Wed May 15 2019 Petr Pisar <ppisar@redhat.com> - 3.52-1
- 3.52 bump

* Thu May 02 2019 Petr Pisar <ppisar@redhat.com> - 3.51-1
- 3.51 bump

* Tue Apr 30 2019 Petr Pisar <ppisar@redhat.com> - 3.49-1
- 3.49 bump

* Mon Apr 29 2019 Petr Pisar <ppisar@redhat.com> - 3.48.again-1
- 3.48-again bump

* Fri Apr 05 2019 Petr Pisar <ppisar@redhat.com> - 3.45-2
- Fix a leak in tests

* Wed Mar 20 2019 Petr Pisar <ppisar@redhat.com> - 3.45-1
- 3.45 bump

* Thu Feb 21 2019 Petr Pisar <ppisar@redhat.com> - 3.44-1
- 3.44 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.43-1
- 3.43 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.42-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Petr Pisar <ppisar@redhat.com> - 3.42-1
- 3.42 bump

* Tue Mar 06 2018 Petr Pisar <ppisar@redhat.com> - 3.36-6
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.36-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 3.36-1
- 3.36 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Petr Pisar <ppisar@redhat.com> - 3.35-1
- 3.35 bump

* Wed Jun 15 2016 Petr Pisar <ppisar@redhat.com> - 3.34-1
- 3.34 bump

* Mon Jun 06 2016 Petr Pisar <ppisar@redhat.com> - 3.33-1
- 3.33 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.32-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Petr Pisar <ppisar@redhat.com> - 3.32-1
- 3.32 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.31-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.31-2
- Perl 5.22 rebuild

* Fri Mar 13 2015 Petr Pisar <ppisar@redhat.com> - 3.31-1
- 3.31 bump

* Fri Mar 06 2015 Petr Pisar <ppisar@redhat.com> - 3.30-1
- 3.30 bump

* Mon Jan 19 2015 Petr Pisar <ppisar@redhat.com> - 3.28-1
- 3.28 bump

* Fri Jan 09 2015 Petr Pisar <ppisar@redhat.com> - 3.25-2
- Do not export private library

* Fri Dec 05 2014 Petr Pisar <ppisar@redhat.com> - 3.25-1
- 3.25 bump

* Thu Sep 18 2014 Petr Pisar <ppisar@redhat.com> 3.24-1
- Specfile autogenerated by cpanspec 1.78.
