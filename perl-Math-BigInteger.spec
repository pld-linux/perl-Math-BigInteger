#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInteger
Summary:	Math::BigInteger perl module
Summary(pl.UTF-8):	Moduł perla Math::BigInteger
Name:		perl-Math-BigInteger
Version:	1.01
Release:	1
# if used in a product, Systemics should be given attribution
License:	free use, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4aa79e070f3f5f8e7f01443fdc03b8e
Patch0:		%{name}-Fputc_to_fputc.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInteger module gives access to Eric Young's bignum library.

%description -l pl.UTF-8
Moduł Math::BigInteger umożliwia dostęp do biblioteki bignum Erica
Younga.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYRIGHT
%{perl_vendorarch}/Math/BigInteger.pm
%dir %{perl_vendorarch}/auto/Math/BigInteger
%{perl_vendorarch}/auto/Math/BigInteger/BigInteger.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/BigInteger/BigInteger.so
%{_mandir}/man3/*
