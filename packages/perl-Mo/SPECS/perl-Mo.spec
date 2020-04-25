Name:           perl-Mo
Version:        0.40
Release:        10%{?dist}
Summary:        Perl micro-object system
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Mo
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/Mo-%{version}.tar.gz
# required test libraries for EPEL6
Patch1:         mo_required_test_libraries.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::MetaRole)
BuildRequires:  perl(PPI)
BuildRequires:  perl(strict)
%if 0%{?el6}
%else
BuildRequires:  perl(Test::More) >= 0.96
%endif
BuildRequires:  perl(warnings)
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(Mouse)
Requires:       perl(Mouse::Util::MetaRole)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Mo provides the bare-minimum for a Perl object system, compared to other similar
systems such as Moose, Mouse and Moo.

%prep
%setup -q -n Mo-%{version}
%if 0%{?el6}
%patch1 -p1
%endif

%build
%if 0%{?el6}
export PERL5LIB=include_test_libs/lib
%endif
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if 0%{?el6}
export PERL5LIB=include_test_libs/lib
%endif
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-3
- Perl 5.22 rebuild

* Fri Nov 14 2014 David Dick <ddick@cpan.org> - 0.39-2
- Patch for EPEL6 distribution

* Sat Sep 13 2014 David Dick <ddick@cpan.org> - 0.39-1
- Upgrade to 0.39

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.20 rebuild

* Thu Aug 21 2014 David Dick <ddick@cpan.org> - 0.38-1
- Initial release
