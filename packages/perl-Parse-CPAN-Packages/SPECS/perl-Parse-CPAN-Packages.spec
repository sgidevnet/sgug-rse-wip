Name:           perl-Parse-CPAN-Packages
Version:        2.40
Release:        14%{?dist}
Summary:        Parse 02packages.details.txt.gz
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Parse-CPAN-Packages
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/Parse-CPAN-Packages-%{version}.tar.gz
Patch0:         Parse-CPAN-Packages-2.40-Test::InDistDir.patch
BuildArch:      noarch
# Module Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(Archive::Peek)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(version)
# Test Suite
# perl(Test::InDistDir) dependency patched out
BuildRequires:  perl(Test::More)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
The Comprehensive Perl Archive Network (CPAN) is a very useful collection
of Perl code. It has several indices of the files that it hosts, including
a file named "02packages.details.txt.gz" in the "modules" directory. This
file contains lots of useful information and this module provides a simple
interface to the data contained within.

%prep
%setup -q -n Parse-CPAN-Packages-%{version}
# Remove the need for (so-far unpackaged) Test::InDistDir
%patch0 -p1
# Strip spurious exec permissions
find . -type f -exec chmod -c -x {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/Parse/
%{_mandir}/man3/Parse::CPAN::Packages.3pm*
%{_mandir}/man3/Parse::CPAN::Packages::Distribution.3pm*
%{_mandir}/man3/Parse::CPAN::Packages::Package.3pm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.40-2
- Perl 5.22 rebuild

* Wed Feb 18 2015 Petr Šabata <contyk@redhat.com> - 2.40-1
- 2.40 bump, a changelog fix

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.38-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Paul Howarth <paul@city-fan.org> - 2.38-1
- Update to 2.38
  - Added methods to the generated objects to try to retrieve dist contents
    from a local cpan mirror
  - Some refactoring/cleanup
  - Added rudimentary logic to return the subs in a package, as well as verify
    via regex whether a given sub is in the package
  - Moved author tests to xt/ to avoid them being run on the user side
  - Removed some dependency on hash ordering in the tests
- Classify buildreqs by usage
- Don't use macros for commands
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Drop EL-5 support as dependencies can't be met there
- Make %%files list more explicit
- Patch out Test::InDistDir dependency, only needed to support upstream's IDE

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.33-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 2.33-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.33-5
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.33-4
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.33-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Steven Pritchard <steve@kspei.com> 2.33-1
- Update to 2.33.
- Update Source0 URL.

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.31-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.31-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.31-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Steven Pritchard <steve@kspei.com> 2.31-1
- Update to 2.31.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Steven Pritchard <steve@kspei.com> 2.30-1
- Update to 2.30.
- BR Compress::Zlib, Moose, Test::Pod, and Test::Pod::Coverage.
- Drop BR Class::Accessor::Fast, IO::Zlib, and Sort::Versions.

* Thu Dec 11 2008 Steven Pritchard <steve@kspei.com> 2.29-1
- Update to 2.29.

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.27-2
- rebuild for new perl

* Sat Jan 12 2008 Steven Pritchard <steve@kspei.com> 2.27-1
- Update to 2.27.
- Switch from building with Build.PL to Makefile.PL.

* Sat Dec 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.26-5
- Adjust License-tag.
- Add BR: perl(Test::More) (BZ 419631).

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 2.26-4
- Use fixperms macro instead of our own chmod incantation.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 2.26-3
- Fix find option order.

* Sat Jul 01 2006 Steven Pritchard <steve@kspei.com> 2.26-2
- BR version.pm.

* Sat Jul 01 2006 Steven Pritchard <steve@kspei.com> 2.26-1
- Update to 2.26.
- Various cleanups.

* Wed Feb 01 2006 Steven Pritchard <steve@kspei.com> 2.25-2
- Drop explicit Requires (except perl(Class::Accessor::Fast), which isn't
  picked up automatically).

* Mon Sep 19 2005 Steven Pritchard <steve@kspei.com> 2.25-1
- Specfile autogenerated.
