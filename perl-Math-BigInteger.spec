%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BigInteger
Summary:	Math::BigInteger perl module
Summary(pl):	Modu³ perla Math::BigInteger
Name:		perl-Math-BigInteger
Version:	1.0
Release:	7
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInteger module gives access to Eric Young's bignum library.

%description -l pl
Modu³ Math::BigInteger umo¿liwia dostêp do biblioteki bignum Erica
Younga.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Math/BigInteger.pm
%dir %{perl_sitearch}/auto/Math/BigInteger
%{perl_sitearch}/auto/Math/BigInteger/BigInteger.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/BigInteger/BigInteger.so
%{_mandir}/man3/*
