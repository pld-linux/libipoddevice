Summary:	Shared library to detect iPods
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
BuildRequires:	dbus-glib-devel
BuildRequires:	hal-devel >= 0.5.6
BuildRequires:	libgtop-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	sg3_utils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libipoddevice is a device-specific layer for the Apple iPod.
libipoddevice provides iPod-specific HAL event notification to
applications, and along with objects representing an iPod, which gives
the application access to properties and features of an iPod.

%package devel
Summary:	Header files for libipoddevice library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71
Requires:	hal-devel >= 0.5.7.1

%description devel
This is the package containing the header files for libipoddevice
library.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ipod
%attr(755,root,root) %{_libdir}/libipoddevice.so.*.*.*
%{_libdir}/hal/hal-ipod-info
%{_datadir}/hal/fdi/policy/20thirdparty/20-ipod-info.fdi

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libipoddevice.so
%{_libdir}/libipoddevice.la
%{_pkgconfigdir}/ipoddevice.pc
%{_includedir}/ipoddevice
