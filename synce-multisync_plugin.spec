Summary:	Plugin SynCE for MultiSync
Summary(pl):	Wtyczka SynCE do MultiSynca
Name:		synce-multisync_plugin
Version:	0.9.0
Release:	1
License:	MIT
Vendor:		The SynCE Project
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	0273cac4d2bce299aec8a51b08101985
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	multisync-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-rra-devel >= 0.9.0
Requires:	synce-rra >= 0.9.0
ExcludeArch:	%{x8664} alpha ia64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is allows synchronization of address book data with
Windows CE 3.0 (Pocket PC) or later.

%description -l pl
Ta wtyczka dodaje mo¿liwo¶æ synchronizacji danych programu multisync z
Pocket PC (z Windows CE 3.0 lub nowszym) poprzez SynCE.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-multisync-include=%{_includedir}/multisync
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/multisync/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE TODO
%attr(755,root,root) %{_libdir}/multisync/lib*.so*
%{_datadir}/synce/*.glade
