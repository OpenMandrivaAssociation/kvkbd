
Name:           kvkbd
BuildRequires:  libxslt-devel task-kde4-devel
License:        GPLv2+
Url:            http://kde-apps.org/content/show.php/Kvkbd+-+KDE4?content=94374
Group:          System/GUI/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A virtual keyboard for KDE
Version:        0.6
Release:        %mkrel 1
Source:         94374-kvkbd-0.6.tar.gz
Patch1:         fix-loginhelper.diff

%description
Kvkbd is a virtual keyboard for KDE, it contains many feature like system tray and dock support, autodetection and on the fly change of the keyboard layout, scripting with DBus, etc.
 
%prep
%setup -n %{name}-%{version} -q
%patch1

%build
  %cmake_kde4
  %make

%install
install -d %{buildroot}/%{_bindir}/kvkbd
install -d %{buildroot}/%{_datadir}/applications/kvkbd.desktop
# install -d %{buildroot}/%{_datadir}/kvkbd
install -d %{buildroot}/%{_docdir}/HTML/en/kvkbd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/kvkbd
%{_datadir}/applications/kvkbd.desktop
# %{_datadir}/applications/kvkbd
%lang(en) %{_docdir}/HTML/en/kvkbd

