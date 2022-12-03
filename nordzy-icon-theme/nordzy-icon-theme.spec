Name:           nordzy-icon
Version:        1.7.6
Release:        1%{?dist}
Summary:        Nordzy Icons

License: Apache License 2.0
URL: https://github.com/alvatip/Nordzy-icon
Source0: https://github.com/alvatip/Nordzy-icon/archive/refs/tags/%{version}.tar.gz

Requires: bash, hicolor-icon-theme, gtk-update-icon-cache
BuildRequires: gtk-update-icon-cache
BuildArch:      noarch

%description
Nordzy is a free and open source icon theme for Linux desktops using the Nord color palette from Arctic Ice Studio and based on WhiteSur Icon Theme and Numix Icon Theme

%prep
%autosetup -n Nordzy-icon-%{version}


%install
mkdir -p "%{buildroot}%{_datadir}icons"
install -dm755 "%{buildroot}%{_datadir}icons"
echo %{_builddir}
%{_builddir}/Nordzy-icon-%{version}/install.sh -d "%{buildroot}%{_datadir}/icons" -t all


%files
%{_datadir}/icons

%changelog
* Tue Mar 27 2022 Rubem Mota <rubemmota89@gmail.com>
- Added First version install of icons
* Tue Dec 03 Rubem Mota <rubemmota89@gmail.com>
- Updated act package to version 1.7.6
