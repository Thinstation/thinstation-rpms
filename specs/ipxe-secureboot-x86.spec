Name:           ipxe-secureboot-x86
Version:        2.0.0
Release:        1%{?dist}
Summary:        Signed iPXE Secure Boot loader pair for x86_64
License:        GPL-2.0-or-later
URL:            https://ipxe.org/
Source0:        ipxe-secureboot-x86.tar.gz
BuildArch:      noarch

%description
Official signed iPXE Secure Boot loader pair for x86_64. The shim and
snponly payload are packaged unchanged from the upstream iPXE release bundle.

%prep
%setup -q -c -T
tar -xzf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/ipxe/secureboot
cp -a ipxeboot/x86_64-sb/shimx64.efi %{buildroot}%{_datadir}/ipxe/secureboot/
cp -a ipxeboot/x86_64-sb/snponly.efi %{buildroot}%{_datadir}/ipxe/secureboot/
ln -s shimx64.efi %{buildroot}%{_datadir}/ipxe/secureboot/snponly-shim.efi

%files
%dir %{_datadir}/ipxe/secureboot
%{_datadir}/ipxe/secureboot/shimx64.efi
%{_datadir}/ipxe/secureboot/snponly.efi
%{_datadir}/ipxe/secureboot/snponly-shim.efi

%changelog
* Mon Sep 28 2026 ThinStation Project <build@thinstation.org> - 2.0.0-1
- Package official signed iPXE Secure Boot loader pair unchanged
