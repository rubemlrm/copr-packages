Name:           numix-kde-theme
Version:        0.0.1
Release:        1%{?dist}
Summary:        Numix KDE Theme

License: Apache License 2.0
URL: https://github.com/numixproject/numix-kde-theme
Source0: https://github.com/numixproject/numix-kde-theme/archive/refs/heads/master.tar.gz
BuildArch: noarch
Requires: bash

%description
A modern flat theme with a combination of light and dark elements.

%install
mkdir -p %{buildroot}%{_datadir}/plasma/
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme/Numix
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel/org.numixproject.kde
cp -r %{_builddir}/%{name}/plasma %{_builddir}/%{name}/color-schemes %{buildroot}%{_datadir}

%files
%{_datadir}/color-schemes/Numix.colors
%{_datadir}/plasma/desktoptheme/Numix
%{_datadir}/plasma/look-and-feel/org.numixproject.kde

%changelog
* Tue Feb 28 2022 Rubem Mota <rubemmota89@gmail.com>
- Added First version install of theme
