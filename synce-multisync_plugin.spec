Summary:	Plugin SynCE for MultiSync
Summary(pl):	Plugin SynCE do MultiSync
Name:		synce-multisync_plugin
Version:	0.9.0
Release:	0.2
License:	MIT
Vendor:		The SynCE Project
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	0273cac4d2bce299aec8a51b08101985
URL:		http://synce.sourceforge.net/
BuildRequires:	synce-devel = %{version}
BuildRequires:	multisync-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
Requires:	synce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is allows synchronization of address book data with
Windows CE 3.0 (Pocket PC) or later

%description -l pl
Plugin dodaje mo¿liwo¶æ synchronizacji danych programu multisync z
Pocket PC poprzez SynCE

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	-with-multisync-include=%{_includedir}/multisync
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/multisync/*
%{_datadir}/synce/glade/*
