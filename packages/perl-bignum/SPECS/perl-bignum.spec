Name:           perl-bignum
Version:        0.51
Release:        439%{?dist}
Summary:        Transparent big number support for Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/bignum
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/bignum-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt) >= 1.999812
BuildRequires:  perl(Math::BigRat) >= 0.12
BuildRequires:  perl(overload)
# Optional run-time:
# Math::BigInt::Lite not packaged
# Tests:
# Algorithm::Combinatorics not used
BuildRequires:  perl(Test::More) >= 0.88
# Test::Version not used
# Optional tests:
# Module::Signature not used and not helpful
# Pod::Coverage 0.18 not used
# Socket not used
# Test::CPAN::Changes not used
# Test::Pod 1.22 not used
# Test::Pod::Coverage 1.08 not used
# Test::Portability::Files not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Math::BigInt) >= 1.999812
Requires:       perl(Math::BigRat) >= 0.12
Conflicts:      perl < 4:5.22.0-348

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::BigInt\\)$

%description
This package attempts to make it easier to write scripts that use BigInts and
BigFloats in a transparent way.

%prep
%setup -q -n bignum-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc BUGS CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-1
- 0.51 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-2
- Perl 5.28 rebuild

* Wed Apr 18 2018 Petr Pisar <ppisar@redhat.com> - 0.50-1
- 0.50 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Petr Pisar <ppisar@redhat.com> - 0.49-1
- 0.49 bump

* Fri Feb 02 2018 Petr Pisar <ppisar@redhat.com> - 0.48-1
- 0.48 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.47-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Petr Pisar <ppisar@redhat.com> 0.47-1
- Specfile autogenerated by cpanspec 1.78.