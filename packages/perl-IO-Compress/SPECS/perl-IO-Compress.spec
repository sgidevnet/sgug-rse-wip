# Run time expensive tests
%bcond_without long_tests
# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_IO_Compress_enables_optional_test
%else
%bcond_with perl_IO_Compress_enables_optional_test
%endif

%{?perl_default_filter}

Name:           perl-IO-Compress
Version:        2.087
Release:        1%{?dist}
Summary:        Read and write compressed data
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Compress
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
# Module Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Bzip2) >= %{version}
BuildRequires:  perl(Compress::Raw::Zlib) >= %{version}
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Path)
BuildRequires:  perl(lib)
BuildRequires:  perl(threads::shared)
%if %{with perl_IO_Compress_enables_optional_test}
# Optional Tests
BuildRequires:  perl(bytes)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(overload)
# Dual-lived module needs building early in the boot process
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
%endif
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::Glob)

# This is wrapper for different Compress modules
Obsoletes:      perl-Compress-Zlib < %{version}-%{release}
Provides:       perl-Compress-Zlib = %{version}-%{release}
Obsoletes:      perl-IO-Compress-Base < %{version}-%{release}
Provides:       perl-IO-Compress-Base = %{version}-%{release}
Obsoletes:      perl-IO-Compress-Bzip2 < %{version}-%{release}
Provides:       perl-IO-Compress-Bzip2 = %{version}-%{release}
Obsoletes:      perl-IO-Compress-Zlib < %{version}-%{release}
Provides:       perl-IO-Compress-Zlib = %{version}-%{release}

%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC 1951,
RFC 1952 (i.e. gzip) and zip files/buffers.

The following modules used to be distributed separately, but are now
included with the IO-Compress distribution:
* Compress-Zlib
* IO-Compress-Zlib
* IO-Compress-Bzip2
* IO-Compress-Base

%prep
%setup -q -n IO-Compress-%{version}

# Remove spurious exec permissions
chmod -c -x lib/IO/Uncompress/{Adapter/Identity,RawInflate}.pm
find examples -type f -exec chmod -c -x {} \;

# Fix shellbangs in examples
perl -MConfig -pi -e 's|^#!/usr/local/bin/perl\b|$Config{startperl}|' examples/io/anycat \
        examples/io/bzip2/* examples/io/gzip/* examples/compress-zlib/*

%build
perl Makefile.PL NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot} INSTALLDIRS=perl
%{_fixperms} -c %{buildroot}

%check
# Build using "--without long_tests" to avoid very long tests
# (full suite can take nearly an hour on an i7 920)
make test COMPRESS_ZLIB_RUN_%{?with_long_tests:ALL}%{!?with_long_tests:MOST}=1

%files
%doc Changes README examples/*
%{_bindir}/zipdetails
%{perl_privlib}/Compress/
%{perl_privlib}/File/
%dir %{perl_privlib}/IO/
%dir %{perl_privlib}/IO/Compress/
%doc %{perl_privlib}/IO/Compress/FAQ.pod
%{perl_privlib}/IO/Compress/Adapter/
%{perl_privlib}/IO/Compress/Base/
%{perl_privlib}/IO/Compress/Base.pm
%{perl_privlib}/IO/Compress/Bzip2.pm
%{perl_privlib}/IO/Compress/Deflate.pm
%{perl_privlib}/IO/Compress/Gzip/
%{perl_privlib}/IO/Compress/Gzip.pm
%{perl_privlib}/IO/Compress/RawDeflate.pm
%{perl_privlib}/IO/Compress/Zip/
%{perl_privlib}/IO/Compress/Zip.pm
%{perl_privlib}/IO/Compress/Zlib/
%{perl_privlib}/IO/Uncompress/
%{_mandir}/man1/zipdetails.1*
%{_mandir}/man3/Compress::Zlib.3*
%{_mandir}/man3/File::GlobMapper.3*
%{_mandir}/man3/IO::Compress::*.3*
%{_mandir}/man3/IO::Uncompress::*.3*

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

* Mon Jan  7 2019 Paul Howarth <paul@city-fan.org> - 2.084-1
- 2.084 bump

* Wed Jan 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.083-1
- 2.083 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.081-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-4
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-2
- Perl 5.28 rebuild

* Mon Apr 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-1
- 2.081 bump

* Wed Apr  4 2018 Paul Howarth <paul@city-fan.org> - 2.080-1
- 2.080 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.074-397
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Petr Pisar <ppisar@redhat.com> - 2.074-396
- Rewrite shell bangs using running perl

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

* Fri Feb 10 2017 Petr Pisar <ppisar@redhat.com> - 2.070-2
- Adjust tests to zlib-1.2.11 (bug #1420012)

* Thu Dec 29 2016 Paul Howarth <paul@city-fan.org> - 2.070-1
- Update to 2.070
  - Fix prototype errors while lazy loading File::GlobMapper (CPAN RT#117675)
  - zipdetails: Avoid loading optional modules from default . (CPAN RT#116538,
    CVE-2016-1238)
- Simplify find command using -delete

* Tue Aug 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-367
- Avoid loading optional modules from default . (CVE-2016-1238)

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.069-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.069-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Paul Howarth <paul@city-fan.org> - 2.069-1
- Update to 2.069
  - IO::Compress::FAQ - Added a section on bgzip (CPAN RT#103295)
  - IO::Compress::Zip - Zip64 needs to be first in extra field to work around
    a Windows Explorer bug (see
    http://www.info-zip.org/phpBB3/viewtopic.php?f=3&t=440 for details)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.068-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.068-2
- Perl 5.22 rebuild

* Wed Dec 24 2014 Paul Howarth <paul@city-fan.org> - 2.068-1
- Update to 2.068
  - Disable running of some of the slower test harnesses by default;
    COMPRESS_ZLIB_RUN_MOST needs to be set to run them, which makes life more
    bearable on legacy platforms

* Tue Dec  9 2014 Paul Howarth <paul@city-fan.org> - 2.067-1
- Update to 2.067
  - IO::Compress::RawDeflate unnecessarily loads IO::Seekable (CPAN RT#100257)
- Classify buildreqs by usage

* Mon Sep 22 2014 Paul Howarth <paul@city-fan.org> - 2.066-1
- Update to 2.066
  - IO::Uncompress::Gzip
    - Documentation of ExtraFlags stated the XFL values for BEST_COMPRESSION
      and BEST_SPEED use the values 2 and 4 respectively; they should be 4 and
      2 (code for setting XFL was correct)
  - IO::Uncompress::Gunzip
    - Fix regression preventing gunzip to in-memory file handle (CPAN RT#95494)

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.064-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.064-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.064-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.064-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb  2 2014 Paul Howarth <paul@city-fan.org> - 2.064-1
- Update to 2.064
  - Use android-compatible flags when calling gzip in
    IO-Compress/t/050interop-gzip.t (CPAN RT#90216)

* Sun Nov  3 2013 Paul Howarth <paul@city-fan.org> - 2.063-1
- Update to 2.063
  - Typo in Compress::Zlib _combine function documentation (CPAN RT#89305)

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.062-2
- Perl 5.18 re-rebuild of bootstrapped packages

* Mon Aug 12 2013 Paul Howarth <paul@city-fan.org> - 2.062-1
- Update to 2.062
  - Fix up tests for imminent bleadperl changes (CPAN RT#87335)
  - Typo fixes (CPAN RT#84647)
  - IO::Compress::Gzip test t/100generic-bzip2.t hung on Cygwin (CPAN RT#86814)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.061-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.061-2
- Perl 5.18 rebuild

* Mon May 27 2013 Paul Howarth <paul@city-fan.org> - 2.061-1
- Update to 2.061
  - zipdetails (1.06)
    - Get it to cope with Android 'zipalign' non-standard extra fields; these
      are used to make sure that a non-compressed member starts on a 4 byte
      boundary
  - unzip example with IO::Uncompress::Unzip (CPAN RT#84647)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.060-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Paul Howarth <paul@city-fan.org> - 2.060-1
- Update to 2.060
  - Updated POD
    - CPAN RT#82138: Example code not clear - gunzip() takes filenames!
  - IO::Compress::Base
    - Remove the flush call when opening a filehandle

* Sun Dec 16 2012 Paul Howarth <paul@city-fan.org> - 2.059-1
- Update to 2.059
  - IO::Compress::Base
    - Added "Encode" option (fixes the encoding half of CPAN RT#42656)

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 2.058-2
- Add missing File::* buildtime dependencies

* Tue Nov 13 2012 Paul Howarth <paul@city-fan.org> - 2.058-1
- Update to 2.058
  - IO::Compress::Zip
    - Allow member name and Zip Comment to be "0"
  - IO::Compress::Base::Common
    - Remove "-r" test - the file open will catch this
    - IO::Compress::Base::Common returned that it could not read readable files
      in NFS (CPAN RT#80855)
  - Install to 'site' instead of 'perl' when perl version is 5.11+
    (CPAN RT#79820)
  - General performance improvements
  - Fix failing 01misc.t subtest introduced in 2.057 (CPAN RT#81119)
- Explicitly install to 'perl' directories

* Mon Aug  6 2012 Paul Howarth <paul@city-fan.org> - 2.055-1
- Update to 2.055
  - FAQ: added a few paragraphs on how to deal with pbzip2 files
    (CPAN RT#77743)
  - Compress::Zip: speed up compress, uncompress, memGzip and memGunzip
    (CPAN RT#77350)
- BR: perl(lib)
- Drop BR: perl(Test::Builder) and perl(Test::More) as they're bundled
- Drop BR: perl(Config), perl(Fcntl), perl(File::Copy), perl(File::Glob),
  perl(POSIX) and perl(Symbol) as they're not dual-lived
- Drop redundant explicit require for perl(Exporter)
- Don't use macros for commands

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.052-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2.052-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.052-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 2.052-2
- Omit optional Test::Pod and Test::NoWarnings tests on bootstrap

* Sun Apr 29 2012 Paul Howarth <paul@city-fan.org> - 2.052-1
- Update to 2.052
  - IO::Compress::Zip: force a ZIP64 archive when it contains ≥ 0xFFFF entries
  - Fix typo in POD (CPAN RT#76130)
- Don't need to remove empty directories from buildroot

* Sat Feb 18 2012 Paul Howarth <paul@city-fan.org> - 2.049-1
- Update to 2.049
  - IO::Compress::Zip:
    - Error in t/cz-03zlib-v1.t that caused warnings with 5.15 (Perl RT#110736)

* Sun Jan 29 2012 Paul Howarth <paul@city-fan.org> - 2.048-1
- Update to 2.048
  - Set minimum Perl version to 5.6
  - Set minimum zlib version to 1.2.0
  - IO::Compress::Zip:
    - In one-shot zip, set the Text Flag if "-T" thinks the file is a text file
    - In one-shot mode, wrote mod time and access time in wrong order in the
      "UT" extended field
  - IO::Compress test suite fails with Compress::Raw::Zlib 2.047 and zlib < 1.2.4
    (CPAN RT#74503)
- Resync Compress::Raw::* dependency versions
- Add buildreqs for core perl modules, which might be dual-lived
- Don't use macros for commands

* Tue Jan 10 2012 Paul Howarth <paul@city-fan.org> - 2.046-2
- Fedora 17 mass rebuild

* Mon Dec 19 2011 Paul Howarth <paul@city-fan.org> - 2.046-1
- Update to 2.046
  - Minor update to bin/zipdetails
  - Typo in name of IO::Compress::FAQ.pod
  - IO::Uncompress::Unzip:
    - Example for walking a zip file used eof to control the outer loop; this
      is wrong
  - IO::Compress::Zip:
    - Change default for CanonicalName to false (CPAN RT#72974)
- Freeze Compress::Raw::* dependency versions until next synchronized release

* Sun Dec  4 2011 Paul Howarth <paul@city-fan.org> - 2.045-1
- Update to 2.045
  - Restructured IO::Compress::FAQ.pod

* Sun Dec  4 2011 Paul Howarth <paul@city-fan.org> - 2.044-1
- Update to 2.044
  - Moved FAQ.pod under the lib directory so it can get installed
  - Added bin/zipdetails
  - In IO::Compress::Zip, in one-shot mode, enable Zip64 mode if the input
    file/buffer ≥ 0xFFFFFFFF bytes
  - Update IO::Compress::FAQ

* Mon Nov 21 2011 Paul Howarth <paul@city-fan.org> - 2.043-1
- Update to 2.043
  - IO::Compress::Base:
    - Fixed issue that with handling of Zip files with two (or more) entries
      that were STORED; symptom is the first is uncompressed ok but the next
      will terminate early if the size of the file is greater than BlockSize
      (CPAN RT#72548)

* Fri Nov 18 2011 Paul Howarth <paul@city-fan.org> - 2.042-1
- Update to 2.042
  - IO::Compress::Zip:
    - Added exUnixN option to allow creation of the "ux" extra field, which
      allows 32-bit UID/GID to be stored
    - In one-shot mode use exUnixN rather than exUnix2 for the UID/GID
  - IO::Compress::Zlib::Extra::parseExtraField:
    - Fixed bad test for length of ID field (CPAN RT#72329, CPAN RT#72505)

* Sat Oct 29 2011 Paul Howarth <paul@city-fan.org> - 2.040-1
- Update to 2.040
  - IO::Compress::Zip:
    - Added CanonicalName option (note this option is set to true by default)
    - Added FilterName option
    - ExtAttr now populates MSDOS attributes
  - IO::Uncompress::Base:
    - Fixed issue where setting $\ would corrupt the uncompressed data
  - t/050interop-*.t:
    - Handle case when external command contains a whitespace (CPAN RT#71335)
  - t/105oneshot-zip-only.t:
    - CanonicalName test failure on Windows (CPAN RT#68926)

* Wed Jun 22 2011 Paul Howarth <paul@city-fan.org> - 2.037-2
- Perl mass rebuild

* Wed Jun 22 2011 Paul Howarth <paul@city-fan.org> - 2.037-1
- Update to 2.037 (support streamed stored content in IO::Uncompress::Unzip)

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.036-2
- Perl mass rebuild

* Mon Jun 20 2011 Petr Sabata <contyk@redhat.com> - 2.036-1
- 2.036 bump (Zip/Unzip enhancements)

* Sat May  7 2011 Paul Howarth <paul@city-fan.org> - 2.035-1
- Update to 2.035 (fix test failure on Windows - CPAN RT#67931)

* Tue May  3 2011 Petr Sabata <psabata@redhat.com> - 2.034-1
- 2.034 bump
- Buildroot and defattr cleanup
- Correcting BRs/Rs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Paul Howarth <paul@city-fan.org> - 2.033-1
- Update to 2.033 (fixed typos and spelling errors - Perl RT#81816)
- Use more explicit %%files list
- Simplify inclusion of IO::Compress::FAQ
- Drop redundant explicit requires of Compress::Raw::{Bzip2,Zlib}
- Drop installdirs patch, not needed with perl 5.12
- Default installdirs are perl, so no need to specify it explicitly
- Make %%summary less generic

* Fri Jan 07 2011 Petr Pisar <ppisar@redhat.com> - 2.032-1
- 2.032 bump
- Small improvements in spec file

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.030-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 21 2010 Paul Howarth <paul@city-fan.org> 2.030-3
- Turn long-running tests back on and support build --without long_tests
  to skip them

* Thu Sep 16 2010 Ville Skyttä <ville.skytta@iki.fi> - 2.030-2
- Install IO::Compress::FAQ into usual POD and man dirs (#634722)

* Mon Jul 26 2010 Petr Sabata <psabata@redhat.com> 2.030-1
- 2.030 version bump

* Thu May 06 2010 Marcela Mašláňová <mmaslano@redhat.com> 2.027-1
- update

* Mon Apr 12 2010 Marcela Mašláňová <mmaslano@redhat.com> 2.024-3
- few fixes in specfile 573932

* Tue Mar 16 2010 Marcela Mašláňová <mmaslano@redhat.com> 2.024-2
- Specfile autogenerated by cpanspec 1.78.
- thanks with fixes of specfile to Paul Howarth

