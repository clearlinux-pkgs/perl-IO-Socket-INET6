#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-INET6
Version  : 2.73
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-2.73.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-2.73.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-inet6-perl/libio-socket-inet6-perl_2.72-2.debian.tar.xz
Summary  : '[ DEPRECATED!! ] Object interface for AF_INET/AF_INET6 domain sockets'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-IO-Socket-INET6-license = %{version}-%{release}
Requires: perl-IO-Socket-INET6-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Socket6)

%description
IO::Socket::INET6
1. Abstract
IO::Socket::INET6 provides an object interface to creating and using sockets
in both AF_INET|AF_INET6 domain. It is built upon the IO::Socket interface and
inherits all the methods defined by IO::Socket.

%package dev
Summary: dev components for the perl-IO-Socket-INET6 package.
Group: Development
Provides: perl-IO-Socket-INET6-devel = %{version}-%{release}
Requires: perl-IO-Socket-INET6 = %{version}-%{release}

%description dev
dev components for the perl-IO-Socket-INET6 package.


%package license
Summary: license components for the perl-IO-Socket-INET6 package.
Group: Default

%description license
license components for the perl-IO-Socket-INET6 package.


%package perl
Summary: perl components for the perl-IO-Socket-INET6 package.
Group: Default
Requires: perl-IO-Socket-INET6 = %{version}-%{release}

%description perl
perl components for the perl-IO-Socket-INET6 package.


%prep
%setup -q -n IO-Socket-INET6-2.73
cd %{_builddir}
tar xf %{_sourcedir}/libio-socket-inet6-perl_2.72-2.debian.tar.xz
cd %{_builddir}/IO-Socket-INET6-2.73
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Socket-INET6-2.73/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Socket-INET6
cp %{_builddir}/IO-Socket-INET6-2.73/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Socket-INET6/38e94f89ec602e1a6495ef7c30477d01aeefedc9
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Socket-INET6/77c9a481e6b50f1c0997b69f7a44b5fa63673a28
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::INET6.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Socket-INET6/38e94f89ec602e1a6495ef7c30477d01aeefedc9
/usr/share/package-licenses/perl-IO-Socket-INET6/77c9a481e6b50f1c0997b69f7a44b5fa63673a28

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
