# Run optional tests
%bcond_without perl_CPAN_Meta_Requirements_enables_optional_test

Name:           perl-CPAN-Meta-Requirements
Version:        2.140
Release:        440%{?dist}
Summary:        Set of version requirements for a CPAN dist
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CPAN-Meta-Requirements
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-Requirements-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.88
BuildRequires:  perl(warnings)
# Test
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Extra Tests (not run when bootstrapping due to circular build dependencies)
%if !%{defined perl_bootstrap} && ! ( 0%{?rhel} ) && %{with perl_CPAN_Meta_Requirements_enables_optional_test}
BuildRequires:  perl(blib)
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(English)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire)
BuildRequires:  perl(Perl::Critic::Policy::Miscellanea::RequireRcsKeywords)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Pod::Wordlist)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Portability::Files)
BuildRequires:  perl(Test::Spelling) >= 0.12, hunspell-en
BuildRequires:  perl(Test::Version) >= 1
%endif
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(B)
Requires:       perl(version) >= 0.88

# CPAN-Meta-Requirements was split from CPAN-Meta
Conflicts:      perl-CPAN-Meta < 2.120921

# Had a six-digit version in a previous life
%global six_digit_version %(LC_ALL=C; printf '%.6f' '%{version}')

# Provide the six-digit version of the module
%if "%{version}" != "%{six_digit_version}"
Provides:       perl(CPAN::Meta::Requirements) = %{six_digit_version}
%global __provides_exclude ^perl\\(CPAN::Meta::Requirements\\)
%endif

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions. It
can be built up by adding more and more constraints, and it will reduce them
to the simplest representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep
%setup -q -n CPAN-Meta-Requirements-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor UNINST=0
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test AUTHOR_TESTING=1
%if !%{defined perl_bootstrap} && ! ( 0%{?rhel} ) && %{with perl_CPAN_Meta_Requirements_enables_optional_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README
%{perl_vendorlib}/CPAN/
%{_mandir}/man3/CPAN::Meta::Requirements.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-393
- Perl 5.26 rebuild

* Thu Apr  6 2017 Paul Howarth <paul@city-fan.org> - 2.140-7
- Introduce build-condition for optional tests
- Simplify find command using -delete
- Switch to hunspell for spell check

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 2.140-5
- Do not use perl to compute Provides version

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.140-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.140-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Paul Howarth <paul@city-fan.org> - 2.140-1
- Update to 2.140
  - Added method for getting structured requirements
  - Skips impossible tests on Perls earlier than 5.8.0 (before v-string magic)
  - On Perls before 5.8.1, pad 1-part and 2-part literal v-strings to avoid old
    version.pm bugs with v-strings less than 3 characters
  - Protect internal _isa_version from non-refs that pass ->isa('version')
  - Much better error messages, explaining what conflicted and how
  - Repackage with fixed tests
  - Expanded dist.ini from author bundle to individual plugins

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.133-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.133-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.133-2
- Perl 5.22 rebuild

* Sun Feb 22 2015 Paul Howarth <paul@city-fan.org> - 2.133-1
- Update to 2.133
  - In fixing preservation of "0.00", some Module => 0 optimizations were lost;
    this restores those optimizations

* Fri Jan 23 2015 Paul Howarth <paul@city-fan.org> - 2.132-1
- Update to 2.132
  - Precision of version requirement "0.00" is preserved when merging
    requirements

* Wed Dec 24 2014 Paul Howarth <paul@city-fan.org> - 2.131-1
- Update to 2.131
  - Merging Module => 0 into requirements is now optimized
  - Scalar::Utils removed as a prerequisite

* Thu Nov 20 2014 Paul Howarth <paul@city-fan.org> - 2.130-1
- Update to 2.130
  - from_string_hash can take optional constructor arguments
  - bad_version_hook callback gets module name as well as version string
  - undefined/empty versions given to from_string_hash or
    add_string_requirement now carp and are coerced to "0" instead of being
    fatal; this is more consistent with how the other requirement functions
    work
- Provide six-digit version in a more robust way

* Fri Nov 14 2014 Paul Howarth <paul@city-fan.org> - 2.129-1
- Update to 2.129
  - from_string_hash can now accept v-strings as hash values

* Thu Sep 18 2014 Petr Pisar <ppisar@redhat.com> - 2.128-1
- 2.128 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.126-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.126-2
- Perl 5.20 rebuild

* Thu Jul 31 2014 Paul Howarth <paul@city-fan.org> - 2.126-1
- Update to 2.126
  - Fixed compatibility with version.pm 0.77
  - Minor documentation fixes
  - Modernized distribution meta files
- Use %%license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Paul Howarth <paul@city-fan.org> - 2.125-1
- Update to 2.125
  - On Perls prior to v5.12, CPAN::Meta::Requirements will force UNINST=1 when
    necessary to remove stale copies from ExtUtils::MakeMaker
  - Updated Makefile.PL logic to support PERL_NO_HIGHLANDER
- README.PATCHING renamed to CONTRIBUTING
- Classify buildreqs by usage
- Add note about logically-impossible constraints to %%description

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.122-292
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.122-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.122-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.122-6
- Conditionalize Test::*

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.122-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.122-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.122-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com>
- Skip some tests on bootstrap

* Mon May 07 2012 Iain Arnell <iarnell@gmail.com> 2.122-1
- update to latest upstream version

* Tue Apr 03 2012 Iain Arnell <iarnell@gmail.com> 2.121-3
- provide perl(CPAN::Meta::Requirements) with six decimal places

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 2.121-2
- clean up spec following review
- run release/author tests too

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 2.121-1
- Specfile autogenerated by cpanspec 1.79.
