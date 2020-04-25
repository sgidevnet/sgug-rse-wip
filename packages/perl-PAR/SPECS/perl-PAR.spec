Name:           perl-PAR
Version:        1.016
Release:        3%{?dist}
Summary:        Perl Archive Toolkit
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/PAR
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/PAR-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl(Archive::Unzip::Burst)
BuildRequires:  perl(Archive::Zip) >= 1
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
# XXX: BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA) >= 5.45
# XXX: BuildRequires:  perl(Digest::SHA1)
# XXX: BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Fcntl)
# XXX: BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.05
# XXX: BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(AutoLoader) >= 5.66
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Archive::Zip) >= 1
Requires:       perl(Digest::SHA) >= 5.45
Requires:       perl(File::Glob)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp) >= 0.05
Requires:       perl(LWP::Simple)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Zip\\)$

%description
This module lets you use special zip files, called Perl Archives, as
libraries from which Perl modules can be loaded.

%prep
%setup -q -n PAR-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc AUTHORS Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.016-2
- Perl 5.30 rebuild

* Tue May 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.016-1
- 1.016 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-3
- Perl 5.26 rebuild

* Wed Apr 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-2
- Fix changelog entry

* Tue Apr 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-1
- 1.015 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-1
- 1.014 bump

* Mon Nov 28 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-1
- 1.013 bump

* Thu Sep 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-1
- 1.011 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Petr Šabata <contyk@redhat.com> - 1.010-1
- 1.010 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-2
- Perl 5.22 rebuild

* Thu Apr 23 2015 Petr Šabata <contyk@redhat.com> - 1.009-1
- 1.009 bump

* Tue Feb 03 2015 Petr Pisar <ppisar@redhat.com> - 1.008-1
- 1.008 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.007-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Petr Šabata <contyk@redhat.com> - 1.007-1
- 1.007 bugfix bump

* Mon Oct 15 2012 Petr Šabata <contyk@redhat.com> - 1.006-1
- 1.006 bump
- Drop command macros

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.005-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Petr Pisar <ppisar@redhat.com> - 1.005-1
- 1.005 bump

* Thu Dec 01 2011 Petr Pisar <ppisar@redhat.com> - 1.004-1
- 1.004 bump

* Tue Nov 29 2011 Petr Šabata <contyk@redhat.com> - 1.003-1
- 1.003 bump
- Update Source URL
- It's time to drop Buildroot and defattr here as well

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.002-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.002-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Sep 14 2010 Petr Sabata <psabata@redhat.com> - 1.002-1
- New release, v1.002

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 1.000-2
- rebuild

* Fri Jun 11 2010 Petr Sabata <psabata@redhat.com> - 1.000-1
- Update to the latest release.

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.994-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.994-2
- rebuild against perl 5.10.1

* Fri Aug 21 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.994-1
- update and fix 505576 which was probably fixed by new release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.992-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.992-1
- update to the latest release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.983-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.983-2
- Specfile autogenerated by cpanspec 1.77.
