Name:           perl-Clone
Version:        0.39
Release:        5%{?dist}
Summary:        Recursively copy perl data types
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Clone
Source:         http://search.cpan.org/CPAN/authors/id/G/GA/GARU/Clone-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Optional tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Taint::Runtime)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types,
including tied variables and objects.

clone() takes a scalar argument and an optional parameter that
can be used to limit the depth of the copy. To duplicate lists,
arrays or hashes, pass them in by reference.

%prep
%setup -q -n Clone-%{version}
find . -type f -exec chmod -c -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/Clone/
%{perl_vendorarch}/Clone.pm
%{_mandir}/man3/*.3*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.26 rebuild

* Mon Apr 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-1
- 0.39 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-2
- Perl 5.22 rebuild

* Fri Mar 20 2015 Tom Callaway <spot@fedoraproject.org> - 0.38-1
- update to 0.38

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.34-4
- Perl 5.18 rebuild

* Mon Jun 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-3
- Update dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Petr Šabata <contyk@redhat.com> - 0.34-1
- 0.34 bump for DBI 1.623
- Modernize the spec
- Update filters and Source URL

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.31-10
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.31-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.31-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.31-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.31-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.31-2
- filter private Perl solibs from provides
- remove some executable bits -- keep rpmlint happy

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-1
- update to 0.31

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.28-4
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.28-3
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.28-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.28-1
- bump to 0.28

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.27-2
- license fix

* Fri Jul 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.27-1
- bump to 0.27

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.22-1
- bump to 0.22

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.20-2
- bump for fc6

* Fri Mar 31 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.20-1
- bump to 0.20
- new BR: perl-Taint-Runtime

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.18-3
- bump for FC-5

* Fri Jan  6 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.18-2
- don't pass optflags twice
- remove .bs files

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.18-1
- Initial package for Fedora Extras
