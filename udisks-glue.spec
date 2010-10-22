Summary:	udisks-glue is a tool that can associate udisks events to user-defined actions
Name:		udisks-glue
Version:	1.1.1
Release:	0.2
License:	distributable (with modifications properly marked if any)
Group:		Applications
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.xz
# Source0-md5:	48600ae617938db28377bcbcd4998e36
Source1:	%{name}.conf
Patch0:		makefile.patch
URL:		http://github.com/fernandotcl/udisks-glue
BuildRequires:	libconfuse-devel
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
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
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	MYCFLAGS="%{rpmcflags}" \
	MYLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install man/udisks-glue.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/udisks-glue.conf
%doc README LICENSE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/udisks-glue.1*
