%{?perl_default_filter}

Name:           perl-HTTP-Proxy
Version:        0.304
Release:        13%{?dist}
Summary:        A pure Perl HTTP proxy
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTTP-Proxy
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/HTTP-Proxy-%{version}.tar.gz
# Add support for IPv6, bug #1422948, CPAN RT#120275
Patch1:     HTTP-Proxy-0.304-Support-IPv6.patch
# debugging 23connect
Patch2:		HTTP-Proxy-0.303-23connect-logging-debug.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build), perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage), perl(HTML::Parser)
BuildRequires:  perl(HTTP::Daemon), perl(LWP::UserAgent), perl(Crypt::SSLeay)
BuildRequires:  perl(File::Spec), perl(Pod::Coverage::TrustPod), perl(Test::CPAN::Meta)
BuildRequires:  perl(Carp), perl(Exporter), perl(ExtUtils::MakeMaker), perl(Fcntl)
BuildRequires:  perl(File::Spec), perl(File::Spec::Functions)
BuildRequires:  perl(File::Find), perl(File::Path), perl(File::Temp), perl(HTTP::Daemon), perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers), perl(HTTP::Headers::Util), perl(HTTP::Request), perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle), perl(IO::Select), perl(IO::Socket::IP)
BuildRequires:  perl(LWP::ConnCache), perl(LWP::UserAgent), perl(POSIX)
BuildRequires:  perl(Socket), perl(Sys::Hostname), perl(Test::More), perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage), perl(URI), perl(base), perl(constant), perl(strict)
BuildRequires:  perl(vars), perl(version), perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Its main use should be to record and/or modify web sessions, so as to
help users create web robots, web testing suites, as well as proxy
systems than can transparently alter the requests to and answers from
an origin server.

%prep
%setup -q -n HTTP-Proxy-%{version}
%patch1 -p1
%patch2 -p1 -b .logging

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README eg/
%{perl_vendorlib}/HTTP/
%{_mandir}/man3/*.3pm*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.304-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.304-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.304-6
- Perl 5.26 rebuild

* Thu Feb 16 2017 Petr Pisar <ppisar@redhat.com> - 0.304-5
- Add support for IPv6 (bug #1422948)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.304-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Tom Callaway <spot@fedoraproject.org> - 0.304-1
- update to 0.304

* Mon Jun 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.303-3
- fix issue with via handling (cpan 105177)
- fix test failure in 23connect by checking for socket blocking mode (bz 1231244)

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.303-2
- Perl 5.22 rebuild

* Thu Apr 30 2015 Tom Callaway <spot@fedoraproject.org> - 0.303-1
- update to 0.303

* Fri Mar 20 2015 Tom Callaway <spot@fedoraproject.org> - 0.302-1
- update to 0.302

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.25-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 0.25-2
- Perl 5.16 rebuild

* Thu Apr 12 2012 Tom Callaway <spot@fedoraproject.org> - 0.25-1
- update to 0.25
- apply default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.23-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-7
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.23-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.23-1
- update to 0.23

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.20-2
Rebuild for new perl

* Mon Sep  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-1
- Update to 0.20.

* Fri Apr 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.19-1
- Update to 0.19.

* Wed Mar 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.18-1
- Update to 0.18.

* Mon Mar  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.17-3
- Added missing BR: perl(Test::Pod::Coverage).

* Mon Mar  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.17-2
- save.pm patched and converted to utf8 (HTTP-Proxy-0.17-save.pm.patch).

* Thu Dec  8 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.17-1
- Update to 0.17.

* Thu Sep  8 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.16-1
- Update to 0.16.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.13-0.fdr.1
- First build.
