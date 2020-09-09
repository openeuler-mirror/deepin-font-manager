%bcond_with check

%global with_debug 1
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif
Name:           deepin-font-manager
Version:        5.6.1
Release:        2
Summary:        Deepin Font Manager is used to install and uninstall font file for users with bulk install function.
License:        GPLv3+
URL:            https://uos-packages.deepin.com/uos/pool/main/d/deepin-font-manager/
Source0:        %{name}-%{version}.orig.tar.xz


BuildRequires:  qt5-qtbase-devel libqtxdg-devel libqtxdg
BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  freetype-devel
BuildRequires:  freetype
BuildRequires:  fontconfig-devel
BuildRequires:  fontconfig
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  dde-file-manager-devel
BuildRequires:  lightdm-gtk-greeter

%description
Deepin Font Manager is used to install and uninstall font file for users with bulk install function.


%prep
%autosetup

%build
export PATH=$PATH:/usr/lib64/qt5/bin
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd


%files
%{_bindir}/deepin-font-manager
%{_bindir}/dfont-install
%{_bindir}/dfont-uninstall
%{_libdir}/*
%{_includedir}/%{name}
%{_datadir}/*
%license LICENSE
%doc README.md


%changelog
* Wed Sep 9 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.1-2 
- fix compile error
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init
