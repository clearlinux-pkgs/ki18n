#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : ki18n
Version  : 5.77.0
Release  : 45
URL      : https://download.kde.org/stable/frameworks/5.77/ki18n-5.77.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.77/ki18n-5.77.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.77/ki18n-5.77.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: ki18n-data = %{version}-%{release}
Requires: ki18n-lib = %{version}-%{release}
Requires: ki18n-license = %{version}-%{release}
Requires: ki18n-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : python3
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtdeclarative-dev

%description
# KI18n
KDE Gettext-based UI text internationalization
## Introduction
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

%package data
Summary: data components for the ki18n package.
Group: Data

%description data
data components for the ki18n package.


%package dev
Summary: dev components for the ki18n package.
Group: Development
Requires: ki18n-lib = %{version}-%{release}
Requires: ki18n-data = %{version}-%{release}
Provides: ki18n-devel = %{version}-%{release}
Requires: ki18n = %{version}-%{release}

%description dev
dev components for the ki18n package.


%package lib
Summary: lib components for the ki18n package.
Group: Libraries
Requires: ki18n-data = %{version}-%{release}
Requires: ki18n-license = %{version}-%{release}

%description lib
lib components for the ki18n package.


%package license
Summary: license components for the ki18n package.
Group: Default

%description license
license components for the ki18n package.


%package locales
Summary: locales components for the ki18n package.
Group: Default

%description locales
locales components for the ki18n package.


%prep
%setup -q -n ki18n-5.77.0
cd %{_builddir}/ki18n-5.77.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607966072
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607966072
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ki18n
cp %{_builddir}/ki18n-5.77.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ki18n/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/ki18n-5.77.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ki18n/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/ki18n-5.77.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/ki18n/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/ki18n-5.77.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ki18n/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/ki18n-5.77.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ki18n/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/ki18n-5.77.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ki18n/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang ki18n5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ca/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/ca@valencia/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/fi/LC_SCRIPTS/ki18n5/general.pmap
/usr/share/locale/fi/LC_SCRIPTS/ki18n5/general.pmapc
/usr/share/locale/fi/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/gd/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/ja/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/ko/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/nb/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/nn/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/nn/LC_SCRIPTS/ki18n5/skjermelement.pmap
/usr/share/locale/nn/LC_SCRIPTS/ki18n5/skjermelement.pmapc
/usr/share/locale/ru/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/sr/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/sr/LC_SCRIPTS/ki18n5/trapnakron.pmap
/usr/share/locale/sr/LC_SCRIPTS/ki18n5/trapnakron.pmapc
/usr/share/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/trapnakron.pmap
/usr/share/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/trapnakron.pmapc
/usr/share/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/trapnakron.pmap
/usr/share/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/trapnakron.pmapc
/usr/share/locale/sr@latin/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/locale/sr@latin/LC_SCRIPTS/ki18n5/trapnakron.pmap
/usr/share/locale/sr@latin/LC_SCRIPTS/ki18n5/trapnakron.pmapc
/usr/share/locale/uk/LC_SCRIPTS/ki18n5/ki18n5.js
/usr/share/qlogging-categories5/ki18n.categories
/usr/share/qlogging-categories5/ki18n.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KI18n/KLocalizedContext
/usr/include/KF5/KI18n/KLocalizedString
/usr/include/KF5/KI18n/KLocalizedTranslator
/usr/include/KF5/KI18n/KuitMarkup
/usr/include/KF5/KI18n/KuitSetup
/usr/include/KF5/KI18n/ki18n_export.h
/usr/include/KF5/KI18n/klocalizedcontext.h
/usr/include/KF5/KI18n/klocalizedstring.h
/usr/include/KF5/KI18n/klocalizedtranslator.h
/usr/include/KF5/KI18n/kuitmarkup.h
/usr/include/KF5/KI18n/kuitsetup.h
/usr/include/KF5/ki18n_version.h
/usr/lib64/cmake/KF5I18n/KF5I18nConfig.cmake
/usr/lib64/cmake/KF5I18n/KF5I18nConfigVersion.cmake
/usr/lib64/cmake/KF5I18n/KF5I18nMacros.cmake
/usr/lib64/cmake/KF5I18n/KF5I18nTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5I18n/KF5I18nTargets.cmake
/usr/lib64/cmake/KF5I18n/build-pofiles.cmake
/usr/lib64/cmake/KF5I18n/build-tsfiles.cmake
/usr/lib64/cmake/KF5I18n/kf5i18nuic.cmake
/usr/lib64/cmake/KF5I18n/ts-pmap-compile.py
/usr/lib64/libKF5I18n.so
/usr/lib64/qt5/mkspecs/modules/qt_KI18n.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5I18n.so.5
/usr/lib64/libKF5I18n.so.5.77.0
/usr/lib64/qt5/plugins/kf5/ktranscript.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ki18n/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ki18n/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/ki18n/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/ki18n/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/ki18n/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ki18n5.lang
%defattr(-,root,root,-)

