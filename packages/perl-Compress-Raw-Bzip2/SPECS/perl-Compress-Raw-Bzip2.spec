# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Compress_Raw_Bzip2_enables_optional_test
%else
%bcond_with perl_Compress_Raw_Bzip2_enables_optional_test
%endif

Name:           perl-Compress-Raw-Bzip2
Summary:        Low-level interface to bzip2 compression library
Version:        2.087
Release:        1%{?dist}
# Other files:  GPL+ or Artistic
## unbundled
# bzip2-src:    BSD
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Compress-Raw-Bzip2
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{version}.tar.gz 
# Module Build
BuildRequires:  bzip2-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
# Module Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(File::Path)
BuildRequires:  perl(threads::shared)
%if %{with perl_Compress_Raw_Bzip2_enables_optional_test}
# Optional Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
BuildRequires:  perl(Scalar::Util)
%endif
BuildRequires:  perl(vars)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides a Perl interface to the bzip2 compression library.
It is used by IO::Compress::Bzip2.

%prep
%setup -q -n Compress-Raw-Bzip2-%{version}
# Remove bundled bzip2 sources
rm -r bzip2-src
perl -i -ne 'print unless /^bzip2-src\//' MANIFEST

%build
BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}
export BUILD_BZIP2 BZIP2_LIB
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Bzip2.3*

%changelog
* Mon Aug 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.087-1
- 2.087 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.086-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.086-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.086-2
- Perl 5.30 rebuild

* Mon Apr 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.086-1
- 2.086 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.084-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.084-1
- 2.084 bump

* Wed Jan 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.083-1
- 2.083 bump

* Mon Jul 30 2018 Petr Pisar <ppisar@redhat.com> - 2.081-5
- Prune bundled bzip2 sources

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.081-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-2
- Perl 5.28 rebuild

* Mon Apr 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-1
- 2.081 bump

* Wed Apr 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.080-1
- 2.080 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.074-397
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.074-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.074-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.074-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.074-393
- Perl 5.26 rebuild

* Mon Feb 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.074-1
- 2.074 bump

* Mon Feb 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.072-1
- 2.072 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.070-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Paul Howarth <paul@city-fan.org> - 2.070-1
- Update to 2.070
  - Fix wrong APPEND_OUTPUT logic (CPAN RT#119005, CPAN RT#119141)
  - Fix some gcc warnings (CPAN RT#100817, CPAN RT#105647)
- Simplify find commands using -empty and -delete

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.069-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Paul Howarth <paul@city-fan.org> - 2.069-1
- Update to 2.069
  - Reduce compiler warnings and stderr noise (CPAN RT#101340)
  - consting misc tables (CPAN RT#101296)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.068-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-2
- Perl 5.22 rebuild

* Wed Dec 24 2014 Paul Howarth <paul@city-fan.org> - 2.068-1
- Update to 2.068 (no changes)

* Tue Dec  9 2014 Paul Howarth <paul@city-fan.org> - 2.067-1
- Update to 2.067 (silence compiler warnings)
- Classify buildreqs by usage

* Mon Sep 22 2014 Paul Howarth <paul@city-fan.org> - 2.066-1
- Update to 2.066 (no changes)

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.064-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.064-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.064-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.064-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.064-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb  2 2014 Paul Howarth <paul@city-fan.org> - 2.064-1
- Update to 2.064
  - Handle non-PVs better (CPAN RT#91558)

* Sun Nov  3 2013 Paul Howarth <paul@city-fan.org> - 2.063-1
- Update to 2.063
  - gcc -g3: final link failed: Memory exhausted (CPAN RT#88936)

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.062-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Mon Aug 12 2013 Paul Howarth <paul@city-fan.org> - 2.062-1
- Update to 2.062 (no changes)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.061-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.061-2
- Perl 5.18 rebuild

* Mon May 27 2013 Paul Howarth <paul@city-fan.org> - 2.061-1
- Update to 2.061
  - Silence compiler warning by making 2nd parameter to DispStream a const char*

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.060-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Paul Howarth <paul@city-fan.org> - 2.060-1
- Update to 2.060 (no changes)

* Sun Nov 25 2012 Paul Howarth <paul@city-fan.org> - 2.059-1
- Update to 2.059
  - Copy-on-write support (CPAN RT#81352)

* Tue Nov 13 2012 Paul Howarth <paul@city-fan.org> - 2.058-1
- Update to 2.058
  - Compress::Raw::Bzip2 needs to use PERL_NO_GET_CONTEXT (CPAN RT#80318)
  - Install to 'site' instead of 'perl' when perl version is 5.11+
    (CPAN RT#79811)
  - Update to ppport.h that includes SvPV_nomg_nolen (CPAN RT#78080)

* Mon Aug  6 2012 Paul Howarth <paul@city-fan.org> - 2.055-1
- Update to 2.055
  - Fix misuse of magic in API (CPAN RT#78080)
- Drop redundant explicit requires for perl(Exporter) and perl(File::Temp)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.052-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.052-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.052-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 2.052-2
- Omit optional Test::Pod tests on bootstrap

* Sun Apr 29 2012 Paul Howarth <paul@city-fan.org> - 2.052-1
- Update to 2.052 (no changes)
- Don't need to remove empty directories from buildroot

* Sat Feb 18 2012 Paul Howarth <paul@city-fan.org> - 2.049-1
- Update to 2.049 (no changes)

* Sun Jan 29 2012 Paul Howarth <paul@city-fan.org> - 2.048-1
- Update to 2.048 (set minimum Perl version to 5.6)
- Don't use macros for commands

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 2.045-2
- Rebuild for gcc 4.7 in Rawhide

* Sun Dec  4 2011 Paul Howarth <paul@city-fan.org> - 2.045-1
- Update to 2.045
  - Moved FAQ.pod to IO::Compress

* Sun Dec  4 2011 Paul Howarth <paul@city-fan.org> - 2.044-1
- Update to 2.044
  - Moved FAQ.pod under the lib directory so it can get installed

* Mon Nov 21 2011 Paul Howarth <paul@city-fan.org> - 2.043-1
- Update to 2.043 (no changes)

* Fri Nov 18 2011 Paul Howarth <paul@city-fan.org> - 2.042-1
- Update to 2.042 (no changes)

* Sat Oct 29 2011 Paul Howarth <paul@city-fan.org> - 2.040-1
- Update to 2.040
  - Croak if attempt to freeze/thaw compression object (CPAN RT#69985)
- BR: perl(Carp)

* Thu Jul 28 2011 Karsten Hopp <karsten@redhat.com> 2.037-3
- Bump and rebuild, got compiled with old perl on ppc

* Wed Jun 22 2011 Paul Howarth <paul@city-fan.org> - 2.037-2
- Perl mass rebuild

* Wed Jun 22 2011 Paul Howarth <paul@city-fan.org> - 2.037-1
- Update to 2.037 (no changes)

* Mon Jun 20 2011 Paul Howarth <paul@city-fan.org> - 2.036-2
- Perl mass rebuild

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 2.036-1
- 2.036 bump (no changes)

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.035-3
- Perl mass rebuild

* Fri Jun 17 2011 Paul Howarth <paul@city-fan.org> - 2.035-2
- Perl mass rebuild

* Sat May  7 2011 Paul Howarth <paul@city-fan.org> - 2.035-1
- Update to 2.035 (no changes)

* Tue May  3 2011 Petr Sabata <psabata@redhat.com> - 2.034-1
- 2.034 bump
- Buildroot cleanup, defattr cleanup
- Correcting BRs/Rs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Paul Howarth <paul@city-fan.org> - 2.033-1
- Update to 2.033 (fixed typos and spelling errors - Perl RT#81782)

* Fri Jan 07 2011 Petr Pisar <ppisar@redhat.com> - 2.032-1
- 2.032 bump

* Wed Sep 29 2010 jkeating - 2.031-2
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Petr Pisar <ppisar@redhat.com> - 2.031-1
- 2.031 bump

* Mon Jul 26 2010 Petr Sabata <psabata@redhat.com> - 2.030-1
- 2.030 version bump

* Thu May  6 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.027-1
- update
 
* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.026-2
- Mass rebuild with perl-5.12.0

* Sat Apr 10 2010 Chris Weyl <cweyl@alumni.drew.edu> 2.026-1
- PERL_INSTALL_ROOT => DESTDIR, use _fixperms incantation
- add perl_default_filter (XS package)
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (2.026)

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 2.020-2
- rebuild against perl 5.10.1

* Mon Jul 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.020-1
- update

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.005-5
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.005-4
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Robin Norwood <rnorwood@redhat.com> - 2.005-3
- Update license tag.

* Tue Jul 17 2007 Robin Norwood <rnorwood@redhat.com> - 2.005-2
- Bump release to beat F-7 version

* Sun Jul 01 2007 Steven Pritchard <steve@kspei.com> 2.005-1
- Update to 2.005.
- Build against system libbz2 (#246401).

* Tue Jun 05 2007 Robin Norwood <rnorwood@redhat.com> - 2.004-1
- Initial build from CPAN
