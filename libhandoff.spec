Summary:	Facilitate limiting a program to a single instance per user
Summary(pl.UTF-8):	Biblioteka ograniczająca program do jednej instancji dla użytkownika
Name:		libhandoff
Version:	0.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	8ec44fda9476391ed372f835d5358fe8
Patch0:		%{name}-link.patch
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Facilitate limiting a program to a single instance per user.

%description -l pl.UTF-8
Biblioteka ograniczająca program do jednej instancji dla użytkownika.

%package devel
Summary:	Header files for libhandoff
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libhandoff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description devel
Header files for libhandoff.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libhandoff.

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
%setup -q
%patch -P0 -p1

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
%attr(755,root,root) %{_libdir}/libhandoff.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhandoff.so
%{_libdir}/libhandoff.la
%{_includedir}/handoff.h
%{_pkgconfigdir}/libhandoff.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhandoff.a
