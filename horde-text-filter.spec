%define prj    Horde_Text_Filter

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-text-filter
Version:       0.0.2
Release:       4
Summary:       Horde Text Filter API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      horde-util
Requires:      horde-text-rest
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Text_Filter:: class provides common methods for fitering and
converting text.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Text
%dir %{peardir}/Horde/Text/Filter
%{peardir}/Horde/Text/Filter.php
%{peardir}/Horde/Text/Filter/bbcode.php
%{peardir}/Horde/Text/Filter/cleanascii.php
%{peardir}/Horde/Text/Filter/dimsignature.php
%{peardir}/Horde/Text/Filter/emails.php
%{peardir}/Horde/Text/Filter/emoticons.php
%{peardir}/Horde/Text/Filter/environment.php
%{peardir}/Horde/Text/Filter/highlightquotes.php
%{peardir}/Horde/Text/Filter/html2text.php
%{peardir}/Horde/Text/Filter/linkurls.php
%{peardir}/Horde/Text/Filter/rst.php
%{peardir}/Horde/Text/Filter/simplemarkup.php
%{peardir}/Horde/Text/Filter/space2html.php
%{peardir}/Horde/Text/Filter/tabs2spaces.php
%{peardir}/Horde/Text/Filter/text2html.php
%{peardir}/Horde/Text/Filter/words.php
%{peardir}/Horde/Text/Filter/xss.php
%dir %{peardir}/tests/Horde_Text_Filter
%dir %{peardir}/tests/Horde_Text_Filter/tests
%{peardir}/tests/Horde_Text_Filter/tests/Filter_emails.phpt
%{peardir}/tests/Horde_Text_Filter/tests/Filter_environment.phpt
%{peardir}/tests/Horde_Text_Filter/tests/Filter_html2text.phpt
%{peardir}/tests/Horde_Text_Filter/tests/Filter_html2text2.phpt
%{peardir}/tests/Horde_Text_Filter/tests/Filter_space2html.phpt


%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 564102
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 523023
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 509375
- removed Buildrequires: hoder-framework
- replaced PreReq with Requires(pre)
- import horde-text-filter


