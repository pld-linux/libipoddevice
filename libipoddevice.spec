Summary:	Library to detect iPods
Summary(pl.UTF-8):	Biblioteka do wykrywania iPodów
Name:		libipoddevice
Version:	0.5.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://banshee-project.org/files/libipoddevice/%{name}-%{version}.tar.gz
# Source0-md5:	b72471b15253a1c779d4ca9991a17fd8
URL:		http://banshee-project.org/Libipoddevice
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	libgtop-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
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
libipoddevice to specyficzna dla urządzenia warstwa dla urządzeń
Apple iPod. Zapewnia wysyłanie powiadomień o specyficznych dla iPoda
zdarzeniach HAL do aplikacji wraz z obiektami reprezentującymi iPoda,
co daje aplikacji dostęp do właściwości i możliwości iPoda.

%package libs
Summary:	Shared libipoddevice library
Summary(pl.UTF-8):	Biblioteka współdzielona libipoddevice
Group:		Libraries

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
Requires:	hal-devel >= 0.5.7.1

%description devel
This is the package containing the header files for libipoddevice
library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libipoddevice.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%{_libdir}/hal/hal-ipod-info
%{_datadir}/hal/fdi/policy/20thirdparty/20-ipod-info.fdi

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libipoddevice.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libipoddevice.so
%{_libdir}/libipoddevice.la
%{_includedir}/ipoddevice
%{_pkgconfigdir}/ipoddevice.pc
