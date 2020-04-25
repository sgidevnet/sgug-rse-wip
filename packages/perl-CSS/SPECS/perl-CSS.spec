Name:           perl-CSS
Version:        1.09
Release:        17%{?dist}
Summary:        Object oriented access to Cascading Style Sheets (CSS)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CSS
Source0:        https://cpan.metacpan.org/modules/by-module/CSS/CSS-%{version}.tar.gz
Source1:        perl-CSS-build-grammar.pl
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) 
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::Simple)
BuildRequires:  dos2unix
BuildRequires:  glibc-common
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module can be used, along with a CSS::Parse::* module, to parse
CSS data and represent it as a tree of objects. Using a
CSS::Adaptor::* module, the CSS data tree can then be transformed into
other formats.

%prep
%setup -q -n CSS-%{version}
# Regenerate CSS::Parse::CompiledGrammar (#564808, CPAN RT#53948)
%{__perl} %{SOURCE1}
mv CompiledGrammar.pm CSS/Parse/

mv Changes Changes.iso88591
iconv -f ISO-8859-1 -t UTF-8 -o Changes Changes.iso88591
touch -r Changes.iso88591 Changes
rm -f Changes.iso88591
dos2unix -k examples/{dump,parsers,adapt}.pl Changes README t/css_simple

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
install -D -p -m 0644 t/css_simple examples/t/css_simple
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/CSS.pm
%{perl_vendorlib}/CSS
%{_mandir}/man3/CSS.*
%{_mandir}/man3/CSS::*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-10
- Perl 5.26 rebuild

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-9
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.09-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.09-1
- 1.09

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.08-16
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.08-13
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.08-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-8
- Mass rebuild with perl-5.12.0

* Thu Feb 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.08-7
- Add patch from Paul Howarth to fix bz #564808, thanks!

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.08-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May  1 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.08-3
- Fix broken build

* Thu Apr 24 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.08-2
- Ship t/css_simple

* Wed Apr 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.08-1
- 1.08 
- Fix license
- Simplify find options
- Fix file endings

* Sat Sep 23 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.07-2
- Add perl(Test::Simple) to buildreq
- Move iconv to %%prep
- Include examples in %%docs

* Fri Sep 21 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.07-1
- Add Parse::RecDescent to buildreq
- Specfile autogenerated by cpanspec 1.73
