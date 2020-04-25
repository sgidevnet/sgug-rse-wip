Name:		perl-Fennec
Version:	2.018
Release:	6%{?dist}
Summary:	A tester's toolbox, and best friend
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Fennec
Source0:	http://cpan.metacpan.org/authors/id/E/EX/EXODIST/Fennec-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build) >= 0.42
# Module Runtime
BuildRequires:	perl(B)
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Child) >= 0.010
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter::Declare)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Mock::Quick) >= 1.106
BuildRequires:	perl(Parallel::Runner) >= 0.013
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder) >= 0.88
BuildRequires:	perl(Test::Exception) >= 0.29
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Simple) >= 0.88
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Pod) >= 1.00
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Child) >= 0.010
Requires:	perl(Mock::Quick) >= 1.106
Requires:	perl(Test::Exception) >= 0.29
Requires:	perl(Test::More) >= 0.88
Requires:	perl(Test::Warn)
Requires:	perl(utf8)

%description
Fennec ties together several testing-related modules and enhances their
functionality in ways you don't get loading them individually. Fennec
makes testing easier, and more useful.

This module is deprecated in favor of Test2::Suite, specifically
Test2::Tools::Spec and Test2::Bundle::SpecDeclare.

%prep
%setup -q -n Fennec-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc CHANGES README
%{perl_vendorlib}/Fennec.pm
%dir %{perl_vendorlib}/Fennec/
%{perl_vendorlib}/Fennec/Collector.pm
%{perl_vendorlib}/Fennec/Collector/
%{perl_vendorlib}/Fennec/EndRunner.pm
%{perl_vendorlib}/Fennec/Finder.pm
%doc %{perl_vendorlib}/Fennec/Manual.pod
%dir %{perl_vendorlib}/Fennec/Manual/
%doc %{perl_vendorlib}/Fennec/Manual/CustomFennec.pod
%{perl_vendorlib}/Fennec/Meta.pm
%{perl_vendorlib}/Fennec/Runner.pm
%{perl_vendorlib}/Fennec/Test.pm
%{perl_vendorlib}/Fennec/Util.pm
%{perl_vendorlib}/Test/
%{_mandir}/man3/Fennec.3*
%{_mandir}/man3/Fennec::Collector.3*
%{_mandir}/man3/Fennec::Collector::TB.3*
%{_mandir}/man3/Fennec::Collector::TB::TempFiles.3*
%{_mandir}/man3/Fennec::EndRunner.3*
%{_mandir}/man3/Fennec::Finder.3*
%{_mandir}/man3/Fennec::Manual.3*
%{_mandir}/man3/Fennec::Manual::CustomFennec.3*
%{_mandir}/man3/Fennec::Meta.3*
%{_mandir}/man3/Fennec::Runner.3*
%{_mandir}/man3/Fennec::Test.3*
%{_mandir}/man3/Fennec::Util.3*
%{_mandir}/man3/Test::Workflow.3*
%{_mandir}/man3/Test::Workflow::Block.3*
%{_mandir}/man3/Test::Workflow::Layer.3*
%{_mandir}/man3/Test::Workflow::Meta.3*
%{_mandir}/man3/Test::Workflow::Test.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.018-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.018-2
- Perl 5.28 rebuild

* Mon Jun 11 2018 Paul Howarth <paul@city-fan.org> - 2.018-1
- Update to 2.018
  - Documentation fixes, deprecate in favor of Test2::Suite
- Drop patch for building with Module::Build < 0.42

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.017-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.017-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.017-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.017-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.017-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.017-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Paul Howarth <paul@city-fan.org> - 2.017-2
- Downgrade Module::Build version requirement to 0.40 (for EPEL-7)

* Wed Apr 23 2014 Paul Howarth <paul@city-fan.org> - 2.017-1
- Update to 2.017
  - Require newer Child.pm

* Tue Mar 18 2014 Paul Howarth <paul@city-fan.org> - 2.016-1
- Update to 2.016
  - Improved subclass support

* Mon Mar 17 2014 Paul Howarth <paul@city-fan.org> - 2.014-1
- Update to 2.014
  - Support FENNEC_PARALLEL=0 environment variable setting

* Mon Jan  6 2014 Paul Howarth <paul@city-fan.org> - 2.013-1
- Update to 2.013
  - Add extra debugging for Dreamhost issue
  - Run 'before_all' after waiting, not before

* Mon Dec  9 2013 Paul Howarth <paul@city-fan.org> - 2.012-1
- Update to 2.012
  - Fix around_all
  - Documentation fixes

* Wed Dec  4 2013 Paul Howarth <paul@city-fan.org> - 2.011-1
- Update to 2.011
  - Typo fixes and documentation enhancements
  - Support the generation of tracking debugging information

* Mon Sep  2 2013 Paul Howarth <paul@city-fan.org> - 2.010-3
- BR: perl(lib) and perl(Data::Dumper) (#997554)

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 2.010-2
- Sanitize for Fedora submission

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 2.010-1
- Initial RPM version
