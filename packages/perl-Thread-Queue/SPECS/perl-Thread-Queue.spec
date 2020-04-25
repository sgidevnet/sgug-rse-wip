Name:           perl-Thread-Queue
Version:        3.13
Release:        439%{?dist}
Summary:        Thread-safe queues
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Thread-Queue
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/Thread-Queue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util) >= 1.10
BuildRequires:  perl(threads::shared) >= 1.21
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More) >= 0.50
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)

%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{_datadir}/doc/

%description
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.

%prep
%setup -q -n Thread-Queue-%{version}
# Correct shell bang
sed -i -e '1 s|^#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|' examples/queue.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.13-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Petr Pisar <ppisar@redhat.com> - 3.13-1
- 3.13 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.12-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.12-393
- Perl 5.26 rebuild

* Fri Feb 17 2017 Petr Pisar <ppisar@redhat.com> - 3.12-1
- 3.12 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 23 2016 Petr Pisar <ppisar@redhat.com> - 3.11-1
- 3.11 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.09-365
- Increase release to favour standalone package

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 3.09-1
- 3.09 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Petr Pisar <ppisar@redhat.com> - 3.07-1
- 3.07 bump

* Wed Aug 26 2015 Petr Pisar <ppisar@redhat.com> - 3.06-1
- 3.06 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.05-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.05-311
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.05-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.05-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Petr Pisar <ppisar@redhat.com> - 3.05-1
- 3.05 bump

* Fri Mar 14 2014 Petr Pisar <ppisar@redhat.com> - 3.04-1
- 3.04 bump

* Fri Mar 07 2014 Petr Pisar <ppisar@redhat.com> - 3.03-1
- 3.03 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 3.02-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 3.02-2
- Link minimal build-root packages against libperl.so explicitly

* Fri Mar 01 2013 Petr Pisar <ppisar@redhat.com> - 3.02-1
- 3.02 bump

* Thu Feb 14 2013 Petr Pisar <ppisar@redhat.com> 3.01-1
- Specfile autogenerated by cpanspec 1.78.
