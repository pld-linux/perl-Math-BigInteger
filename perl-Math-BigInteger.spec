%include	/usr/lib/rpm/macros.perl
Summary:	Math-BigInteger perl module
Summary(pl):	Modu³ perla Math-BigInteger
Name:		perl-Math-BigInteger
Version:	1.0
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-BigInteger-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-12
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Math-BigInteger module gives access to Eric Young's bignum library. 

%description -l pl
Modu³ Math-BigInteger umo¿liwia dostêp do biblioteki bignum Erica Younga.

%prep
%setup -q -n Math-BigInteger-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/Math/BigInteger/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/BigInteger
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/Math/BigInteger.pm

%dir %{perl_sitearch}/auto/Math/BigInteger
%{perl_sitearch}/auto/Math/BigInteger/.packlist
%{perl_sitearch}/auto/Math/BigInteger/BigInteger.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/BigInteger/BigInteger.so

%{_mandir}/man3/*
