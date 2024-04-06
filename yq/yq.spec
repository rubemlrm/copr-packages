Name:           yq
Version:        4.43.1
Release:        1%{?dist}
Summary:        A lightweight and portable command-line YAML, JSON and XML processor.yq uses jq like syntax but works with yaml files as well as json, xml, properties, csv and tsv. 

License: MIT
URL: https://github.com/mikefarah/yq
Source0: https://github.com/mikefarah/yq/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  make, git, go, wget, binutils
Requires: bash

%description
Portable command-line YAML processor

%prep
%autosetup -n yq-%{version}
export VERSION=%{version}

make build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{_builddir}/yq-%{version}/dist/local/yq %{buildroot}/%{_bindir}/yq


%files
%{_bindir}/yq


%changelog
%autochangelog

