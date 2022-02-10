Name:           act
Version:        0.2.25
Release:        1%{?dist}
Summary:        Run your github workflows locally

License: MIT
URL: https://github.com/nektos/act
Source0: https://github.com/nektos/act/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make, git, go, wget, binutils
Requires: bash

%description
Run your GitHub Actions locally!

%prep
%autosetup -n %{name}-%{version}
export VERSION=%{version}

make build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/dist/local/%{name} %{buildroot}/%{_bindir}/%{name}


%files
%{_bindir}/%{name}


%changelog
* Thu Feb 10 2022 Rubem Mota <rubemmota89@gmail.com>
- teste
