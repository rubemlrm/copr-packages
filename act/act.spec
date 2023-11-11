Name:           act-cli
Version:        0.2.53
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
* Sat Nov 11 2023 Rubem Mota <rubemmota89@gmail.com>
* Updated act package to version 0.2.53
* Sat Sep 01 2023 Rubem Mota <rubemmota89@gmail.com>
* Updated act package to version 0.2.50
* Sat Aug 26 2023 Rubem Mota <rubemmota89@gmail.com>
* Updated act package to version 0.2.49
* Sun Mar 05 2023 Rubem Mota <rubemmota89@gmail.com>
* Updated act package to version 0.2.43
* Sat Feb 25 2023 Rubem Mota <rubemmota89@gmail.com>
* Updated act package to version 0.2.42
* Thu Jan 19 2023 Rubem Mota <rubemmota89@gmail.com>
- Updated act package to version 0.2.40
* Fri Dec 03 2022 Rubem Mota <rubemmota89@gmail.com>
- Updated act package to version 0.2.34
* Fri Mar 26 2022 Rubem Mota <rubemmota89@gmail.com>
- Updated act package to version 0.2.26
* Fri Feb 11 2022 Rubem Mota <rubemmota89@gmail.com>
- Updated spec file because of conflicting package name
* Thu Feb 10 2022 Rubem Mota <rubemmota89@gmail.com>
- First commit with act-cli
