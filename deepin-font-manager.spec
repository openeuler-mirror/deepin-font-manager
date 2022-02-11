%define libname libdeepin-font-manager

Name:           deepin-font-manager
Version:        5.6.23
Release:        2
Summary:        Deepin Font Manager is used to install and uninstall font file for users with bulk install function
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-qtbase-QPainterPath.patch

BuildRequires: gcc-c++
BuildRequires: qt5-devel

BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(dde-file-manager)
BuildRequires: qt5-qtbase-private-devel

%description
%{summary}.

%package -n %{libname}
Summary:        %{summary}
%description -n %{libname}
%{summary}.

%package -n %{libname}-devel
Summary:        %{summary}
%description -n %{libname}-devel
%{summary}.


%prep
%autosetup -p1

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../ DAPP_VERSION=%{version} DEFINES+="VERSION=%{version}"
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/dde-file-manager/plugins/previews/libdeepin-font-preview-plugin.so
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/applications/%{name}.desktop


%files -n %{libname}
%{_libdir}/%{libname}.so.*
%{_datadir}/deepin-font-manager/CONTENTS.txt

%files -n %{libname}-devel
%{_includedir}/%{name}/
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Feb 11 2022 liweigang <liweiganga@uniontech.com> - 5.6.23-2
- fix build error

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.6.23-1 
- Update 5.6.23

* Wed Sep 9 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.1-2 
- fix compile error
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init
