%define repoDir  %{name}-%{version}

Name:           aura-kde-theme
Version:        1.0.0
Release:        1%{?dist}
Summary:        Aura theme

License:        GPLv3+
URL:            https://github.com/yeyushengfan258/Aura-kde.git

BuildArch:      noarch

%description
Aura kde is a light clean theme for KDE Plasma desktop.

%prep
rm -rf %{repoDir}
git clone %{url} %{repoDir}
cd %{repoDir}

%install
cd %{repoDir}
bash install.sh


%changelog
