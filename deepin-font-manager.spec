# %define libname libdeepin-font-manager
%define pkgrelease  1
%if 0%{?openeuler}
%define specrelease %{pkgrelease}
%else
## allow specrelease to have configurable %%{?dist} tag in other distribution
%define specrelease %{pkgrelease}%{?dist}
%endif

Name:           deepin-font-manager
Version:        5.8.7
Release:        %{specrelease}
Summary:        Deepin Font Manager is used to install and uninstall font file for users with bulk install function
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-devel

BuildRequires: dtkwidget-devel
Buildrequires: dtkcore-devel
BuildRequires: dtkgui-devel
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(dde-file-manager)
BuildRequires: deepin-gettext-tools
BuildRequires: gtest-devel
BuildRequires: gmock-devel
BuildRequires: qt5-qtbase-private-devel

%description
%{summary}.

# %package -n %{libname}
# Summary:        %{summary}
# %description -n %{libname}
# %{summary}.
# 
# %package -n %{libname}-devel
# Summary:        %{summary}
# %description -n %{libname}-devel
# %{summary}.


%prep
%autosetup -p1

%build
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
sed -i "s|lib/${CMAKE_LIBRARY_ARCHITECTURE}|lib64|" ./deepin-font-preview-plugin/CMakeLists.txt
mkdir build && pushd build 
%cmake -DCMAKE_BUILD_TYPE=Release ../  -DAPP_VERSION=%{version} -DVERSION=%{version} 
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
%{_datadir}/deepin-manual/manual-assets/application/deepin-font-manager/font-manager/*
%{_datadir}/deepin-font-manager/contents.txt


%changelog
* Mon Jul 18 2022 konglidong <konglidong@uniontech.com> - 5.8.7-1
- update to 5.8.7

* Fri Feb 11 2022 liweigang <liweiganga@uniontech.com> - 5.6.23-2
- fix build error

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.6.23-1 
- Update 5.6.23

* Wed Sep 9 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.1-2 
- fix compile error
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init
