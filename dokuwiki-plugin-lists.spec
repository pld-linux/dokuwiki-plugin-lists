%define		plugin		lists
Summary:	DokuWiki Lists Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20080328
Release:	1
License:	GPL v3+
Group:		Applications/WWW
Source0:	http://dev.mwat.de/dw/syntax_plugin_lists.zip
# Source0-md5:	3048488fcfe5b1c62edf6357eb9cad58
URL:		http://www.dokuwiki.org/plugin:actionlink
Requires:	dokuwiki >= 20050713
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin functionally replaces (and enhances) DokuWiki's builtin
handling of un/ordered lists.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/syntax.php
%{plugindir}/*.css
