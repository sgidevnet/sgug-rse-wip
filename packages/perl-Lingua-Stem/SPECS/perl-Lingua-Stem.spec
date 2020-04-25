Name:           perl-Lingua-Stem
Version:        0.84
Release:        26%{?dist}
Summary:        Stemming of words
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Lingua-Stem
Source0:        https://cpan.metacpan.org/authors/id/S/SN/SNOWHARE/Lingua-Stem-%{version}.tar.gz
# Define POD encoding, CPAN RT#87242
Patch0:         Lingua-Stem-0.84-Define-POD-encoding.patch
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Lingua::GL::Stemmer)
BuildRequires:  perl(Lingua::PT::Stemmer)
BuildRequires:  perl(Lingua::Stem::Fr) >= 0.02
BuildRequires:  perl(Lingua::Stem::It)
# XXX: BuildRequires:  perl(Lingua::Stem::Ru)
BuildRequires:  perl(Lingua::Stem::Snowball::Da) >= 1.01
BuildRequires:  perl(Lingua::Stem::Snowball::No) >= 1.00
BuildRequires:  perl(Lingua::Stem::Snowball::Se) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::German)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
# Optional tests only
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Lingua::Stem::Snowball::Da) >= 1.01
Requires:       perl(Lingua::Stem::Snowball::No) >= 1.00
Requires:       perl(Lingua::Stem::Snowball::Se) >= 1.01
Requires:       perl(Lingua::Stem::Fr) >= 0.02
Requires:       perl(Lingua::Stem::It)
Requires:       perl(Lingua::Stem::Ru)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Lingua::Stem::Snowball::Da\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Lingua::Stem::Snowball::No\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Lingua::Stem::Snowball::Se\\)$


%description
This routine applies stemming algorithms to its parameters, returning the
stemmed words as appropriate to the selected locale.

%prep
%setup -q -n Lingua-Stem-%{version}
%patch0 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
TEST_POD_COVERAGE=1 ./Build test

%files
# The LICENSE file doesn't contain license texts
%license Artistic_License.txt GPL_License.txt
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-22
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-17
- Perl 5.24 rebuild

* Thu Feb 18 2016 Petr Šabata <contyk@redhat.com> - 0.84-16
- Package cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-13
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.84-9
- Perl 5.18 rebuild
- Define POD encoding (CPAN RT#87242)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.84-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.84-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.84-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon Aug 16 2010 Iain Arnell <iarnell@epo.org> 0.84-1
- Specfile autogenerated by cpanspec 1.78.
