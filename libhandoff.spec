#
Summary:	GPE widget library
Name:		libhandoff
Version:	0.0.0.9128
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	c5dab6c926b791451cc9f896c584a828
URL:		http://gpe.linuxtogo.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE widget library.

%package devel
Summary:	Header files for libhandoff
Group:		Development/Libraries

%description devel
Header files for libhandoff.

%package static
Summary:	Static libhandoff library
Summary(pl.UTF-8):	Statyczna biblioteka libhandoff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libhandoff library.

%description static -l pl.UTF-8
Statyczna biblioteka libhandoff.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root)    %{_libdir}/libhandoff.so.0.0.0


%files devel
%defattr(644,root,root,755)
%{_includedir}/handoff.h
%{_libdir}/libhandoff.la
%{_pkgconfigdir}/libhandoff.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhandoff.a
