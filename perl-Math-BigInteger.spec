#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	BigInteger
Summary:	Math::BigInteger - arbitrary length integer extension module for Perl
Summary(pl.UTF-8):	Math::BigInteger - moduł rozszerzenia liczb całkowitych dowolnej długości
Name:		perl-Math-BigInteger
Version:	1.01
Release:	22
# if used in a product, Systemics should be given attribution
License:	free use, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4aa79e070f3f5f8e7f01443fdc03b8e
Patch0:		%{name}-Fputc_to_fputc.patch
URL:		http://search.cpan.org/dist/Math-BigInteger/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInteger module gives access to Eric Young's bignum library.
This provides a faster alternative to the Math::BigInt library.

%description -l pl.UTF-8
Moduł Math::BigInteger umożliwia dostęp do biblioteki bignum Erica
Younga. Jest to szybsza alternatywa dla biblioteki Math::BigInt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Math/BigInteger/BigInteger.so
%{_mandir}/man3/*
