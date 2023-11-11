Name:           kubectx
Version:        0.9.5
Release:        1%{?dist}
Summary:        The Kubernetes context manager

License: Apache License 2.0
URL: https://github.com/ahmetb/kubectx
Source0: https://github.com/ahmetb/kubectx/archive/refs/tags/v%{version}.tar.gz

Requires: bash

%description
Kubernetes context manager for bash and zsh.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
install -Dm 755 -p %{_builddir}/%{name}-%{version}/kubectx %{_builddir}/%{name}-%{version}/kubens -t "%{buildroot}/usr/bin"

# completion
install -Dm 644 -p %{_builddir}/%{name}-%{version}/completion/kubectx.bash "%{buildroot}%{_datadir}/bash-completion/completions/kubectx"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/completion/kubens.bash "%{buildroot}%{_datadir}/bash-completion/completions/kubens"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/completion/_kubectx.zsh "%{buildroot}%{_datadir}/zsh/site-functions/_kubectx"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/completion/_kubens.zsh "%{buildroot}%{_datadir}/zsh/site-functions/_kubens"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/completion/kubectx.fish "%{buildroot}%{_datadir}/fish/vendor_completions.d/kubectx.fish"
install -Dm 644 -p %{_builddir}/%{name}-%{version}/completion/kubens.fish "%{buildroot}%{_datadir}/fish/vendor_completions.d/kubens.fish"


%files
%{_bindir}/%{name}
%{_bindir}/kubens
%{_datadir}/bash-completion/completions/kubectx
%{_datadir}/bash-completion/completions/kubens
%{_datadir}/zsh/site-functions/_kubectx
%{_datadir}/zsh/site-functions/_kubens
%{_datadir}/fish/vendor_completions.d/kubectx.fish
%{_datadir}/fish/vendor_completions.d/kubens.fish

%changelog
* Sat Nov 11 2023 Rubem Mota <rubemmota89@gmail.com>
- Fixed building workflow
* Sat Sep 09 2023 Rubem Mota <rubemmota89@gmail.com>
- Updated to version v0.9.5
* Tue Feb 12 2022 Rubem Mota <rubemmota89@gmail.com>
- Added First version install of kubectx and kubens
