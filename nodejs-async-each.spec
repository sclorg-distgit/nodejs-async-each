%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name async-each

# Tests disabled because it will not work yet
%global enable_tests 0

Summary:       Ultra-simple async parallel forEach function for JavaScript
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.0
Release:       5%{?dist}
License:       MIT
URL:           https://github.com/paulmillr/async-each
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}nodejs(async)
%endif

%description
Ultra-simple, 35-lines-of-code async parallel forEach function for JavaScript.

We don't need junky 30K async libs. Really.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%doc CHANGELOG.md README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-5
- Clean up

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Rebuilt with updated metapackage

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Enable scl macros

* Mon Dec 14 2015 Troy Dawson <tdawson@redhat.com> - 1.0.0-1
- Initial package
