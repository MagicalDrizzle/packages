Name:           proton-vpn-qt-app
Version:        1.10.6
Release:        1%{?dist}
Summary:        Qt GUI frontend for the ProtonVPN Linux CLI.

License:        GPL-3.0-only
URL:            https://github.com/wheat32/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Packager:       Mizuki Nguyen <tcbnmzk@proton.me>

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)

Recommends:     curl
Recommends:     libnatpmp
Requires:       proton-vpn-cli

%description
A Qt GUI frontend for the Proton VPN Linux CLI.

* One-click connect/disconnect with a large power button and system tray controls
* Automatic connection detection on launch using protonvpn status, with active server
  and public IP display
* Background polling every 15 seconds — detects external state changes (CLI disconnect,
  reconnect, or location switch) and updates the UI without any user action
* Secure login with interactive 2FA support and inline validation
* Confirmation dialog when quitting while the VPN is active — leave it running or
  disconnect cleanly
* Single-instance protection to prevent duplicate launches
* Proton-inspired dark theme with KDE Breeze (when available) or Fusion styling
* Informational banners for CLI version mismatches and pre-release builds

%prep
%autosetup
%find_lang %{name} --with-qt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/metainfo/io.github.wheat32.ProtonVPNQt.metainfo.xml

%changelog
* Fri Sep 18 2026 Mizuki Nguyen <tcbnmzk@proton.me> - 1.10.6-1
- Initial package
