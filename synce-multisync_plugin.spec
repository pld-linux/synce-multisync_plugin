# NOTE: obsoleted in favour of libopensync02-plugin-synce-rra.spec
Summary:	SynCE plugin for MultiSync
Summary(pl.UTF-8):	Wtyczka SynCE do MultiSynca
Name:		synce-multisync_plugin
Version:	0.9.0
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	0273cac4d2bce299aec8a51b08101985
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libglade2-devel >= 2.0
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

%description -l pl.UTF-8
Ta wtyczka dodaje możliwość synchronizacji danych programu multisync z
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/multisync/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE TODO
%attr(755,root,root) %{_libdir}/multisync/libsynce_plugin.so*
# dir shared among some synce apps
%dir %{_datadir}/synce
%{_datadir}/synce/synce_multisync_plugin.glade
