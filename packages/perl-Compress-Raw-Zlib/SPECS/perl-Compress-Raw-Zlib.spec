# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Compress_Raw_Zlib_enables_optional_test
%else
%bcond_with perl_Compress_Raw_Zlib_enables_optional_test
%endif

Name:           perl-Compress-Raw-Zlib
Version:        2.087
Release:        1%{?dist}
Summary:        Low-level interface to the zlib compression library
# Zlib.xs:  (GPL+ or Artistic) and zlib
# Others:   GPL+ or Artistic
## Not used to produce binary packages
# zlib-src: zlib
License:        (GPL+ or Artistic) and zlib
URL:            https://metacpan.org/release/Compress-Raw-Zlib
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(vars)
BuildRequires:  sed
BuildRequires:  zlib-devel >= 1.2.1
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
%if %{with perl_Compress_Raw_Zlib_enables_optional_test}
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
%endif
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library, which is used by IO::Compress::Zlib.

%prep
%setup -q -n Compress-Raw-Zlib-%{version}
# Remove bundled zlib
rm -rf zlib-src
sed -i -e '/^zlib-src\//d' MANIFEST

%build
OLD_ZLIB=False
BUILD_ZLIB=False 
ZLIB_LIB=%{_libdir}
ZLIB_INCLUDE=%{_includedir}
export BUILD_ZLIB OLD_ZLIB ZLIB_LIB ZLIB_INCLUDE
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test COMPRESS_ZLIB_RUN_MOST=1

%files
%doc Changes README
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Zlib.3*

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

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.076-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.076-1
- 2.076 bump

* Wed Nov 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.075-1
- 2.075 bump

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

* Tue Feb 07 2017 Petr Pisar <ppisar@redhat.com> - 2.071-2
- Adapt tests to zlib-1.2.11 (bug #1419841)

* Sat Dec 31 2016 Paul Howarth <paul@city-fan.org> - 2.071-1
- Update to 2.071
  - One (last?) compilation warning in bundled inflate.c (CPAN RT#119580,
    https://github.com/madler/zlib/issues/111)

* Thu Dec 29 2016 Paul Howarth <paul@city-fan.org> - 2.070-1
- Update to 2.070
  - Fix compilation warning from inflate.c (CPAN RT#107642)
  - Fix wrong FLAG_APPEND logic, analog to Bzip2 (CPAN RT#119007)
- Simplify find commands using -empty and -delete

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.069-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Paul Howarth <paul@city-fan.org> - 2.069-1
- Update to 2.069
  - Reduce compiler warnings and stderr noise (CPAN RT#101341)
  - amigaos4: cpan/Compress-Raw-Zlib: also __amigaos4__ (CPAN RT#106799)
  - const all global data (CPAN RT#101298)
  - Coverity finding: Unused value (CPAN RT#105414)
  - Coverity findings (CPAN RT#102399)
  - Coverity finding: Overlapping buffer in memory copy (CPAN RT#105413)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.068-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-3
- Perl 5.22 rebuild

* Thu Mar 19 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-2
- Correct license from (GPL+ or Artistic) to ((GPL+ or Artistic) and zlib)

* Wed Dec 24 2014 Paul Howarth <paul@city-fan.org> - 2.068-1
- Update to 2.068
  - Silence more compiler warnings
  - Disable running of 07bufsize.t by default; COMPRESS_ZLIB_RUN_MOST needs to
    be set to run it, which makes life more bearable on legacy platforms

* Tue Dec  9 2014 Paul Howarth <paul@city-fan.org> - 2.067-1
- Update to 2.067 (silence compiler warnings)
- Classify buildreqs by usage

* Mon Sep 22 2014 Paul Howarth <paul@city-fan.org> - 2.066-1
- Update to 2.066
  - Another COW violation (CPAN RT#98069)
  - Misleading nesting/indentation found by Coverity (CPAN RT#95405)

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.065-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.065-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.065-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.065-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.065-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb  4 2014 Paul Howarth <paul@city-fan.org> - 2.065-1
- Update to 2.065
  - Resolve c++ build failure in core (CPAN RT#92657)
  - gcc -g3: final link failed: Memory exhausted (CPAN RT#88936)

* Sun Feb  2 2014 Paul Howarth <paul@city-fan.org> - 2.064-1
- Update to 2.064
  - Handle non-PVs better (CPAN RT#91558)
  - Z_OK instead of Z_BUF_ERROR (CPAN RT#92521)

* Sun Nov  3 2013 Paul Howarth <paul@city-fan.org> - 2.063-1
- Update to 2.063
  - gcc -g3: final link failed: Memory exhausted (CPAN RT#88936)
  - Compress::Raw::Zlib uses AutoLoader for no reason (CPAN RT#88260)
  - Typo in Compress::Zlib _combine function documentation (CPAN RT#89305)

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.062-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Mon Aug 12 2013 Paul Howarth <paul@city-fan.org> - 2.062-1
- Update to 2.062
  - Typo fix (CPAN RT#86417)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.061-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.061-2
- Perl 5.18 rebuild

* Mon May 27 2013 Paul Howarth <paul@city-fan.org> - 2.061-1
- Update to 2.061
  - Include zlib 1.2.8 source
  - Typo fix (CPAN RT#85431)
  - Silence compiler warning by making 2nd parameter to DispStream a const char*

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.060-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Paul Howarth <paul@city-fan.org> - 2.060-1
- Update to 2.060 (mention SimpleZip in POD)

* Sun Nov 25 2012 Paul Howarth <paul@city-fan.org> - 2.059-1
- Update to 2.059
  - Copy-on-write support (CPAN RT#81353)

* Tue Nov 13 2012 Paul Howarth <paul@city-fan.org> - 2.058-1
- Update to 2.058
  - Compress::Raw::Zlib needs to use PERL_NO_GET_CONTEXT (CPAN RT#80319)
  - Install to 'site' instead of 'perl' when perl version is 5.11+
    (CPAN RT#79812)
  - Update to ppport.h that includes SvPV_nomg_nolen (CPAN RT#78079)

* Sat Aug 11 2012 Paul Howarth <paul@city-fan.org> - 2.056-1
- Update to 2.056
  - Fix C++ build issue

* Mon Aug  6 2012 Paul Howarth <paul@city-fan.org> - 2.055-1
- Update to 2.055
  - Fix misuse of magic in API (CPAN RT#78079)
  - Include zlib 1.2.7 source
- BR: perl(Exporter) and perl(lib)
- BR: perl(Test::NoWarnings) except when bootstrapping
- Drop redundant explicit require for perl(Exporter)
- Drop BR: perl(bytes), not dual-lived

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.054-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.054-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.054-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 2.054-2
- Omit optional Test::Pod tests on bootstrap

* Tue May  8 2012 Paul Howarth <paul@city-fan.org> - 2.054-1
- Update to 2.054
  - Fix build issue on Win32 (CPAN RT#77030)

* Sun May  6 2012 Paul Howarth <paul@city-fan.org> - 2.053-1
- Update to 2.053
  - Include zlib 1.2.7 source

* Sun Apr 29 2012 Paul Howarth <paul@city-fan.org> - 2.052-1
- Update to 2.052
  - Fix build issue when Perl is built with C++
- Don't need to remove empty directories from buildroot

* Thu Feb 23 2012 Paul Howarth <paul@city-fan.org> - 2.051-1
- Update to 2.051
  - Fix bug in Compress::Raw::Zlib on 64-bit Windows (CPAN RT#75222)

* Tue Feb 21 2012 Paul Howarth <paul@city-fan.org> - 2.050-1
- Update to 2.050
  - Fix build failure on Irix and Solaris (CPAN RT#75151)

* Sat Feb 18 2012 Paul Howarth <paul@city-fan.org> - 2.049-1
- Update to 2.049
  - Include zlib 1.2.6 source

* Sun Jan 29 2012 Paul Howarth <paul@city-fan.org> - 2.048-1
- Update to 2.048
  - Allow flush to be called multiple times without any intermediate call to
    deflate and still return Z_OK
  - Added support for zlibCompileFlags
  - Set minimum Perl version to 5.6
  - Set minimum zlib version to 1.2.0
- Don't use macros for commands

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 2.045-2
- Rebuild for gcc 4.7 in Rawhide

* Sun Dec  4 2011 Paul Howarth <paul@city-fan.org> - 2.045-1
- Update to 2.045
  - Moved FAQ.pod into Zlib.pm

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

* Tue Aug 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.037-4
- Install to vendorlib so that our debuginfo does not conflict with that of
  the main perl package

* Thu Jul 28 2011 Karsten Hopp <karsten@redhat.com> 2.037-3
- Bump and rebuild as it got compiled with the old perl on ppc

* Wed Jun 22 2011 Paul Howarth <paul@city-fan.org> - 2.037-2
- Perl mass rebuild

* Wed Jun 22 2011 Paul Howarth <paul@city-fan.org> - 2.037-1
- Update to 2.037 (no changes)

* Mon Jun 20 2011 Paul Howarth <paul@city-fan.org> - 2.036-2
- Perl mass rebuild

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 2.036-1
- 2.036 bump (added offset parameter to CRC32)

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.035-3
- Perl mass rebuild

* Fri Jun 17 2011 Paul Howarth <paul@city-fan.org> - 2.035-2
- Perl mass rebuild

* Sat May  7 2011 Paul Howarth <paul@city-fan.org> - 2.035-1
- Update to 2.035 (no changes)

* Tue May  3 2011 Petr Sabata <psabata@redhat.com> - 2.034-1
- 2.034 bump
- Buildroot and defattr cleanup
- Correcting BRs/Rs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.033-3
- remove epoch again, it's actually rpmdev bug
 https://fedorahosted.org/rpmdevtools/ticket/13

* Fri Jan 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.033-2
- re-add epoch. rpmdev-vercmp "0" 2.032 2 "" 2.033 1 -> 2.032

* Thu Jan 13 2011 Paul Howarth <paul@city-fan.org> - 2.033-1
- Update to 2.033 (fixed typos and spelling errors - Perl RT#81782)
- Drop redundant Obsoletes and Epoch tags
- Simplify provides filter

* Fri Jan 07 2011 Petr Pisar <ppisar@redhat.com> - 0:2.032-2
- BuildRequire perl(Test::Pod) for tests

* Fri Jan 07 2011 Petr Pisar <ppisar@redhat.com> - 0:2.032-1
- 2.032 bump

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0:2.030-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Jul 26 2010 Petr Sabata <psabata@redhat.com> - 0:2.030-1
- 2.030 version bump

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0:2.027-1
- update

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0:2.024-3
- Mass rebuild with perl-5.12.0

* Mon Mar 29 2010 Marcela Mašláňová <mmaslano@redhat.com> 2.024-2
- split again from main package for updated version

* Tue Jul 17 2007 Robin Norwood <rnorwood@redhat.com> - 2.005-2
- Bump release to beat F-7 version

* Sun Jul 01 2007 Robin Norwood <rnorwood@redhat.com> - 2.005-1
- update to 2.005.

* Tue Jun 05 2007 Robin Norwood <rnorwood@redhat.com> - 2.004-1
- Initial build from CPAN

