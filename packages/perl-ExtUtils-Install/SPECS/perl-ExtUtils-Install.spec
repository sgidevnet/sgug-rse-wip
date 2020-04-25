# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_ExtUtils_Install_enables_optional_test
%else
%bcond_with perl_ExtUtils_Install_enables_optional_test
%endif

Name:           perl-ExtUtils-Install
Version:        2.14
Release:        440%{?dist}
Summary:        Install Perl files from here to there
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-Install
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/ExtUtils-Install-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(AutoSplit)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
# Data::Dumper not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
# POSIX is optional
BuildRequires:  perl(vars)
# VMS::Filespec not used
# Win32API::File not used
# Tests:
BuildRequires:  perl(diagnostics)
# ExtUtils::CBuilder not used
BuildRequires:  perl(ExtUtils::MM)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
# VMS::DCLsymnot used
# Unbundled tests:
# Test::Builder not used
%if %{with perl_ExtUtils_Install_enables_optional_test}
# Optional testes:
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::Pod) >= 1.14
# Test::Pod::Coverage 1.08 not used
# Pod::Coverage 0.17 not used
%endif
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(AutoSplit)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Compare)
Recommends:     perl(POSIX)

%{?perl_default_filter}

%description
Handles the installing and uninstalling of Perl modules, scripts, man
pages, etc.

%prep
%setup -q -n ExtUtils-Install-%{version}
# Remove bundled modules
rm -rf t/lib/Test
sed -i -e '/^t\/lib\/Test\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Petr Pisar <ppisar@redhat.com> - 2.14-1
- 2.14 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-367
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-2
- Perl 5.22 rebuild

* Thu Sep 18 2014 Petr Pisar <ppisar@redhat.com> 2.04-1
- Specfile autogenerated by cpanspec 1.78.
