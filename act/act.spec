Name:           act-cli
Version:        0.2.26
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
%autosetup -n act-%{version}
export VERSION=%{version}

make build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{_builddir}/act-%{version}/dist/local/act %{buildroot}/%{_bindir}/act


%files
%{_bindir}/act


%changelog
* Thu Feb 10 2022 Rubem Mota <rubemmota89@gmail.com>
- First commit with act-cli
* Thu Feb 11 2022 Rubem Mota <rubemmota89@gmail.com>
- Updated spec file because of conflicting package name
* Thu Mar 26 2022 Rubem Mota <rubemmota89@gmail.com>
- Updated act package to version 0.2.26
