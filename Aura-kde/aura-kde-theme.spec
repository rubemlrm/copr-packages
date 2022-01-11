%define repoDir  %{name}-%{version}

Name:           aura-kde-theme
Version:        1.0.0
Release:        1%{?dist}
Summary:        Aura theme

License:        GPLv3+
URL:            https://github.com/yeyushengfan258/Aura-kde.git
Source0: master.tar.gz

BuildArch:      noarch

%description
Aura kde is a light clean theme for KDE Plasma desktop.

%prep
%autosetup

%install
ls
bash install.sh


%changelog
%changelog
* Tue Jan 11 2022 Rubem Mota <rubemmota89@gmail.com> 1.0.0-1
- new package built with tito
