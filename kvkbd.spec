# Probably there's a strip hidden somewhere in the makefiles - we get an
# empty debuginfo package...
%define debug_package %nil

Name:           kvkbd
BuildRequires:  libxslt-devel task-kde4-devel
BuildRequires:	pkgconfig(xi) pkgconfig(xtst)
License:        GPLv2+
Url:            http://kde-apps.org/content/show.php/Kvkbd+-+KDE4?content=94374
Group:          Graphical desktop/KDE 
Summary:        A virtual keyboard for KDE
Version:        0.6
Release:        2
Source:         94374-kvkbd-0.6.tar.gz
Patch0:		kvkbd-0.6-compile.patch
Patch1:         fix-loginhelper.diff

%description
Kvkbd is a virtual keyboard for KDE, it contains many feature like
system tray and dock support, auto-detection and on the fly change
of the keyboard layout, scripting with DBus, etc.
 
%prep
%setup -n %{name}-%{version} -q
%apply_patches

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}/%{_bindir}/kvkbd
install -d %{buildroot}/%{_datadir}/applications/kvkbd.desktop
install -d %{buildroot}/%{_docdir}/HTML/en/kvkbd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/kvkbd
%{_datadir}/applications/kvkbd.desktop
%lang(en) %{_docdir}/HTML/en/kvkbd



%changelog
* Tue Apr 19 2011 Zombie Ryushu <ryushu@mandriva.org> 0.6-1mdv2011.0
+ Revision: 655906
- initial build of kvkbd
- imported package kvkbd


* Fri Jan 29 2010 llunak@novell.com
- adjust requirements and filelist
* Mon Jun 29 2009 llunak@novell.com
- Initial version 0.6
