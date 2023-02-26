Name:           betterlockscreen
Version:        4.0.4
Release:        1%{?dist}
Summary:        The Kubernetes context manager

License: Apache License 2.0
URL: https://github.com/betterlockscreen/betterlockscreen
Source0: https://github.com/betterlockscreen/betterlockscreen/archive/refs/tags/v%{version}.tar.gz

Requires: bash bc feh i3lock-color imagemagick xrandr xdpyinfo

%description
Kubernetes context manager for bash and zsh.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
install -Dm 755 -p %{_builddir}/%{name}-%{version}/%{name} -t "%{buildroot}/usr/bin"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/system/%{name}@.service -t "%{buildroot}/usr/lib/systemd/system/"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/examples/%{name}rc -t "%{buildroot}%{_docdir}/betterlockscreen/examples/"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/LICENSE -t "%{buildroot}/usr/share/licenses/%{name}"


%files

%{_bindir}/betterlockscreen
%{_docdir}/betterlockscreen/examples/%{name}rc
/usr/lib/systemd/system/betterlockscreen@.service
/usr/share/licenses/betterlockscreen/LICENSE

%changelog
* Sat Feb 25 2023 Rubem Mota <rubemmota89@gmail.com>
- Added First version of betterlockscreen
