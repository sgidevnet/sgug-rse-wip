%global base_version 3.35
Name:           perl-ExtUtils-ParseXS
# Epoch to compete with perl.spec
Epoch:          1
Version:        3.40
Release:        439%{?dist}
Summary:        Module and a script for converting Perl XS code into C code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-ParseXS
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{base_version}.tar.gz
# Unbundled from perl 5.28.0-RC1
Patch0:         ExtUtils-ParseXS-3.35-Upgrade-to-3.39.patch
# Unbundled from perl 5.29.10
# Fix generating Perl prototypes for XS functions with OUTLIST parameters,
# RT#133654
Patch1:         ExtUtils-ParseXS-3.39-Upgrade-to-3.40.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter) >= 5.57
# ExtUtils::XSSymSet not needed
BuildRequires:  perl(File::Basename)
# Getopt::Long not tested
BuildRequires:  perl(re)
BuildRequires:  perl(Symbol)
# Tests:
BuildRequires:  perl(attributes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Exporter) >= 5.57

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and creates
the glue necessary to let Perl access those functions.

%prep
%setup -q -n ExtUtils-ParseXS-%{base_version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
# Do not install xsubpp twice, RT#117289
rm $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/xsubpp
ln -s ../../../../bin/xsubpp $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.40-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.40-438
- Increase release to favour standalone package

* Thu May 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.40-1
- Upgrade to 3.40 as provided in perl-5.29.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.39-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Petr Pisar <ppisar@redhat.com> - 1:3.39-418
- Fix generating Perl prototypes for XS functions with OUTLIST parameters
  (RT#133654)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.39-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.39-416
- Increase release to favour standalone package

* Thu May 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.39-1
- Upgrade to 3.39 as provided in perl-5.28.0-RC1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Petr Pisar <ppisar@redhat.com> - 1:3.35-1
- 3.35 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.34-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 1:3.34-1
- Upgrade to 3.34 as provided in perl-5.25.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.31-368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Petr Pisar <ppisar@redhat.com> - 1:3.31-367
- Remove old obsoleting perl-ExtUtils-Typemaps

* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.31-366
- Avoid loading optional modules from default . (CVE-2016-1238)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.31-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.31-1
- 3.31 bump in order to dual-live with perl 5.24

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 1:3.30-3
- Remove dependency on perl-devel (bug #1129443)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Petr Pisar <ppisar@redhat.com> - 1:3.30-1
- 3.30 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.28-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.28-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.28-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 1:3.28-1
- 3.28 bump in order to dual-live with perl 5.22

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:3.24-310
- Perl 5.20 rebuild
- Increase release to favour standalone package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Petr Pisar <ppisar@redhat.com> - 1:3.24-1
- 3.24 bump

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 1:3.22-1
- 3.22 bump

* Mon Aug 26 2013 Petr Pisar <ppisar@redhat.com> - 1:3.21-1
- 3.21 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.18-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:3.18-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:3.18-2
- Perl 5.18 rebuild

* Fri Mar 22 2013 Petr Pisar <ppisar@redhat.com> 1:3.18-1
- Specfile autogenerated by cpanspec 1.78.
