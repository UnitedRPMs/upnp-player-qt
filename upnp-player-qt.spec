#
# spec file for package upnp-player-qt
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%global debug_package %{nil}
# 
%define _legacy_common_support 1

%global commit0 85b9df8b7ad8a23d850ea12d2a3d3f6ed8006939
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           upnp-player-qt
Version:        0.2
Release:        1%{dist}
Summary:        Upnp layer build with Qt5
License:        LGPLv3
Group:		System Environment/Daemons
URL:            https://gitlab.com/homeautomationqt/upnp-player-qt

Source0:	https://gitlab.com/homeautomationqt/upnp-player-qt/-/archive/%{commit0}/upnp-player-qt-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  cmake
BuildRequires:	extra-cmake-modules
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(KF5Declarative) 
BuildRequires:	kdsoap-devel

%description
Upnp layer build with Qt5.

%package        devel
Summary:        Development package for upnp-player-qt
Requires:       %{name} = %{version}-%{release}

%description  devel
Development package for upnp-player-qt.


%prep
%autosetup -n %{name}-%{commit0}

%build
%cmake_kf5 -DBUILD_TESTING=OFF .
%make_build

%install
%make_install

# unstripped-binary-or-object fix
chmod 0755 %{buildroot}/%{_bindir}/binaryLight
chmod 0755 %{buildroot}/%{_bindir}/upnpWebSocketClient
chmod 0755 %{buildroot}/%{_bindir}/upnpWebSocketProxy
chmod 0755 %{buildroot}/%{_libdir}/libupnpQt.so.0.1.0
chmod 0755 %{buildroot}/%{_libdir}/libupnpQtBase.so.0.1.0
chmod 0755 %{buildroot}/%{_libdir}/libupnpQtWebSocket.so.0.1.0


%files 
%{_bindir}/binaryLight
%{_bindir}/upnpWebSocketClient
%{_bindir}/upnpWebSocketProxy
%{_libdir}/libupnpQt.so.*
%{_libdir}/libupnpQtBase.so.*
%{_libdir}/libupnpQtWebSocket.so.*
   
%files devel
%{_libdir}/libupnpQt.so
%{_libdir}/libupnpQtBase.so
%{_libdir}/libupnpQtWebSocket.so
%{_libdir}/cmake/UPNPQT/
%{_includedir}/KF5/UPNPQTBASE/
%{_includedir}/KF5/UPNPQTWEBSOCKET/
%{_includedir}/KF5/UPNPQT/


   
%changelog

* Sat May 02 2020 David Va <davidva AT tuta DOT io> 0.2-1
- Initial build
