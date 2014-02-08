%define upstream_name    Pod-Plainer
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	To convert POD to old-style plainer POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Pod::Plainer uses Pod::Parser which takes Pod with the (new) 'C<< .. >>'
constructs and returns the old(er) style with just 'C<>'; '<' and '>' are
replaced by 'E<lt>' and 'E<gt>'.

This can be used to pre-process Pod before using tools which do not
recognise the new style Pods.

METHODS
    * escape_ltgt

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.30.0-3mdv2011.0
+ Revision: 656961
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 597195
- rebuild

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 573810
- update to 1.03

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 562433
- rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 504488
- update to 1.02

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 462494
- import perl-Pod-Plainer


* Sat Nov 07 2009 cpan2dist 1.01-1mdv
- initial mdv release, generated with cpan2dist
