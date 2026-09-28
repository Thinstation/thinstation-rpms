%global commit d4fb57727826ee43fb6d58ca6b837509e96202c7

Name:           gtkdialog
Version:        0.8.5
Release:        1%{?dist}
Summary:        Create GTK dialogs from shell scripts

License:        GPL-2.0-or-later
URL:            https://github.com/puppylinux-woof-CE/gtkdialog
Source0:        %{url}/archive/%{commit}/gtkdialog-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gthread-2.0)

%description
gtkdialog provides a simple XML-like language for creating GTK user
interfaces from shell scripts. ThinStation uses it for interactive dialogs.

%prep
%autosetup -n gtkdialog-%{commit}

%build
%meson -Dgtkver=2 -Ddocs=false
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gtkdialog
%{_datadir}/icons/hicolor/32x32/apps/gtkdialog.png

%changelog
* Mon Sep 28 2026 ThinStation Project <build@thinstation.org> - 0.8.5-1
- Build current gtkdialog with GTK2 and GCC 14+ compatibility fixes
