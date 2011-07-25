Summary:	Library to detect iPods
Summary(pl.UTF-8):	Biblioteka do wykrywania iPodów
Name:		libipoddevice
Version:	0.5.3
Release:	4
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.banshee.fm/legacy/libipoddevice/%{name}-%{version}.tar.gz
# Source0-md5:	b72471b15253a1c779d4ca9991a17fd8
Patch0:		%{name}-sgutils.patch
URL:		http://download.banshee.fm/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	libgtop-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sg3_utils-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hal >= 0.5.7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libipoddevice is a device-specific layer for the Apple iPod.
libipoddevice provides iPod-specific HAL event notification to
applications, and along with objects representing an iPod, which gives
the application access to properties and features of an iPod.

%description -l pl.UTF-8
libipoddevice to specyficzna dla urządzenia warstwa dla urządzeń Apple
iPod. Zapewnia wysyłanie powiadomień o specyficznych dla iPoda
zdarzeniach HAL do aplikacji wraz z obiektami reprezentującymi iPoda,
co daje aplikacji dostęp do właściwości i możliwości iPoda.

%package libs
Summary:	Shared libipoddevice library
Summary(pl.UTF-8):	Biblioteka współdzielona libipoddevice
Group:		Libraries
Requires:	glib2 >= 1:2.6.0
Requires:	hal-libs >= 0.5.7.1
Requires:	libgtop >= 2.12.0

%description libs
Shared libipoddevice library.

%description libs -l pl.UTF-8
Biblioteka współdzielona libipoddevice.

%package devel
Summary:	Header files for libipoddevice library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libipoddevice
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71
Requires:	glib2-devel >= 1:2.6.0
Requires:	hal-devel >= 0.5.7.1

%description devel
This is the package containing the header files for libipoddevice
library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libipoddevice.

%package static
Summary:	Static libipoddevice library
Summary(pl.UTF-8):	Statyczna biblioteka libipoddevice
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libipoddevice library.

%description static -l pl.UTF-8
Statyczna biblioteka libipoddevice.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	EJECT_PATH=/usr/bin/eject
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ipod
%attr(755,root,root) %{_libdir}/hal/hal-ipod-info
%{_datadir}/hal/fdi/policy/20thirdparty/20-ipod-info.fdi

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libipoddevice.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libipoddevice.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libipoddevice.so
%{_libdir}/libipoddevice.la
%{_includedir}/ipoddevice
%{_pkgconfigdir}/ipoddevice.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libipoddevice.a
