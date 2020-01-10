Name: hyphen-ku
Summary: Kurdish hyphenation rules
Version: 1.71.2
Release: 6%{?dist}
Source: http://extensions.services.openoffice.org/e-files/2445/12/kitandin.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/kitandin
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
Requires: hyphen

%description
Kurdish hyphenation rules.

%prep
%setup -q -c -n hyphen-ku

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ku.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_ku_TR.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen
ku_TR_aliases="ku_SY"
for lang in $ku_TR_aliases; do
        ln -s hyph_ku_TR.dic hyph_$lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ku.txt
%{_datadir}/hyphen/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.71.2-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 31 2010 Caolan McNamara <caolanm@redhat.com> - 1.71.2-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Caolan McNamara <caolanm@redhat.com> - 1.60-1
- latest version

* Fri Jun 12 2009 Caolan McNamara <caolanm@redhat.com> - 1.00-1
- latest version

* Thu May 28 2009 Caolan McNamara <caolanm@redhat.com> - 0.21-1
- initial version
