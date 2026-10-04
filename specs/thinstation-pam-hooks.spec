Name:           thinstation-pam-hooks
Version:        1.0.0
Release:        1%{?dist}
Summary:        ThinStation PAM session hook module
License:        GPL-2.0-or-later
URL:            https://github.com/Thinstation/thinstation-rpms
Source0:        pam_hooks.c

BuildRequires:  gcc
BuildRequires:  pam-devel
Requires:       pam

%description
Small PAM module used by ThinStation to invoke a configured session helper on
PAM session open and close. The module passes "open" or "close" followed by
the authenticated PAM username to the configured helper command.

%prep
cp %{SOURCE0} pam_hooks.c

%build
%{__cc} %{build_cflags} -fPIC -shared -Wl,-z,relro -Wl,-z,now \
    -o pam_hooks.so pam_hooks.c -lpam

%install
install -Dpm 0755 pam_hooks.so %{buildroot}%{_libdir}/security/pam_hooks.so

%files
%{_libdir}/security/pam_hooks.so

%changelog
* Sun Oct 04 2026 ThinStation Project <build@thinstation.org> - 1.0.0-1
- Replace legacy in-tree PAM hook binary with reproducible RPM build
