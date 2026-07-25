%define modname	Pod-Plainer
%define modver 1.04

Summary:	To convert POD to old-style plainer POD
Name:		perl-%{modname}
Version:	%{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Pod-Plainer
Source0:	https://cpan.metacpan.org/authors/id/R/RM/RMBARKER/Pod-Plainer-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl-devel

%description
Pod::Plainer uses Pod::Parser which takes Pod with the (new) 'C<< .. >>'
constructs and returns the old(er) style with just 'C<>'; '<' and '>' are
replaced by 'E<lt>' and 'E<gt>'.

This can be used to pre-process Pod before using tools which do not
recognise the new style Pods.

METHODS
    * escape_ltgt

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
