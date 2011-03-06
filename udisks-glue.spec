Summary:	udisks-glue is a tool that can associate udisks events to user-defined actions
Name:		udisks-glue
Version:	1.3.0
Release:	2
License:	distributable (with modifications properly marked if any)
Group:		Applications
Source0:	https://github.com/downloads/fernandotcl/udisks-glue/%{name}-%{version}.tar.gz
# Source0-md5:	a784b3ad113db62efee548d8c0aa32eb
Source1:	%{name}.conf
URL:		http://github.com/fernandotcl/udisks-glue
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	libconfuse-devel
BuildRequires:	pkg-config
Requires:	udisks
Suggests:	k3b
Suggests:	libnotify
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
udisks-glue is a tool that can associate udisks events to user-defined
actions. Udisks-glue should eventually offer the most useful features
found in the aforementioned projects. As of now, however, only the
most basic functionality is available (mounting and unmounting
removable media).

If you want to use default configuration, you should install libnotify
and k3b (the package suggests these).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/udisks-glue.conf
%doc ChangeLog INSTALL LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/udisks-glue.1*
