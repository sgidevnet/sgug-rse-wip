Name:           perl-XML-Feed
Version:        0.59
Release:        3%{?dist}
Summary:        Syndication feed parser and auto-discovery
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XML-Feed
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/XML-Feed-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Flexible)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::Natural)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Feed::Find)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Fetch)
BuildRequires:  perl(XML::Atom) >= 0.38
BuildRequires:  perl(XML::LibXML) >= 1.66
BuildRequires:  perl(XML::RSS) >= 1.47
BuildRequires:  perl(XML::RSS::LibXML)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Class::ErrorHandler)
Requires:       perl(XML::RSS) >= 1.47

%?perl_default_filter

%description
XML::Feed is a syndication feed parser for both RSS and Atom feeds. It also
implements feed auto-discovery for finding feeds, given a URI.

%prep
%setup -q -n XML-Feed-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/XML*
%{_mandir}/man3/XML*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-2
- Perl 5.30 rebuild

* Sun Feb 10 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.59-1
- Update to 0.59

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.55-1
- Update to 0.55

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.53-1
- Update to 0.53

* Thu Nov 19 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.52-8
- Use NO_PACKLIST=1 when creating Makefile
- Add more BuildRequires
- Tighten file listing

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-6
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.52-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Iain Arnell <iarnell@gmail.com> 0.52-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 0.51-1
- udpate to latest upstream version

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 0.50-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.49-2
- Perl 5.16 rebuild

* Mon Apr 09 2012 Iain Arnell <iarnell@gmail.com> 0.49-1
- update to latest upstream version

* Wed Mar 14 2012 Iain Arnell <iarnell@gmail.com> 0.48-1
- update to latest upstream version

* Sun Mar 11 2012 Iain Arnell <iarnell@gmail.com> 0.47-1
- update to latest upstream version

* Fri Jan 20 2012 Iain Arnell <iarnell@gmail.com> 0.46-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter and DESTDIR

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.43-8
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.43-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.43-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.43-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.43-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Iain Arnell 0.43-1
- Specfile autogenerated by cpanspec 1.77.
