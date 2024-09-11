#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : ki18n
Version  : 6.5.0
Release  : 96
URL      : https://download.kde.org/stable/frameworks/6.5/ki18n-6.5.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.5/ki18n-6.5.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.5/ki18n-6.5.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: ki18n-data = %{version}-%{release}
Requires: ki18n-lib = %{version}-%{release}
Requires: ki18n-license = %{version}-%{release}
Requires: ki18n-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : python3-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KI18n
There's two libraries provided, KI18n for Gettext-based text internationalization,
and KI18nLocaleData for access to data about countries and timezones.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n ki18n-6.5.0
cd %{_builddir}/ki18n-6.5.0
pushd ..
cp -a ki18n-6.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723220287
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723220287
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ki18n
cp %{_builddir}/ki18n-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ki18n/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ki18n-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ki18n/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ki18n-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ki18n/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ki18n-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/ki18n/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/ki18n-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ki18n/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/ki18n-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ki18n/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/ki18n-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ki18n/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/ki18n-%{version}/docs/locale-data-qml-api.md.license %{buildroot}/usr/share/package-licenses/ki18n/28ba3ebe1aa04fad742c69eb685e2a5376e9276f || :
cp %{_builddir}/ki18n-%{version}/src/localedata/qgis/generate-geographic-data.qgs.license %{buildroot}/usr/share/package-licenses/ki18n/5ca60da87c5035ecdea20354a6f3fd079ac47c20 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ki18n6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ca/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/ca@valencia/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/fi/LC_SCRIPTS/ki18n6/general.pmap
/usr/share/locale/fi/LC_SCRIPTS/ki18n6/general.pmapc
/usr/share/locale/fi/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/gd/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/ja/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/ko/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/nb/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/nn/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/nn/LC_SCRIPTS/ki18n6/skjermelement.pmap
/usr/share/locale/nn/LC_SCRIPTS/ki18n6/skjermelement.pmapc
/usr/share/locale/ru/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/sr/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/sr/LC_SCRIPTS/ki18n6/trapnakron.pmap
/usr/share/locale/sr/LC_SCRIPTS/ki18n6/trapnakron.pmapc
/usr/share/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/trapnakron.pmap
/usr/share/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/trapnakron.pmapc
/usr/share/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/trapnakron.pmap
/usr/share/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/trapnakron.pmapc
/usr/share/locale/sr@latin/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/locale/sr@latin/LC_SCRIPTS/ki18n6/trapnakron.pmap
/usr/share/locale/sr@latin/LC_SCRIPTS/ki18n6/trapnakron.pmapc
/usr/share/locale/uk/LC_SCRIPTS/ki18n6/ki18n6.js
/usr/share/qlogging-categories6/ki18n.categories
/usr/share/qlogging-categories6/ki18n.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KI18n/KLazyLocalizedString
/usr/include/KF6/KI18n/KLocalization
/usr/include/KF6/KI18n/KLocalizedContext
/usr/include/KF6/KI18n/KLocalizedString
/usr/include/KF6/KI18n/KLocalizedTranslator
/usr/include/KF6/KI18n/KuitSetup
/usr/include/KF6/KI18n/ki18n_export.h
/usr/include/KF6/KI18n/ki18n_version.h
/usr/include/KF6/KI18n/klazylocalizedstring.h
/usr/include/KF6/KI18n/klocalization.h
/usr/include/KF6/KI18n/klocalizedcontext.h
/usr/include/KF6/KI18n/klocalizedstring.h
/usr/include/KF6/KI18n/klocalizedtranslator.h
/usr/include/KF6/KI18n/kuitsetup.h
/usr/include/KF6/KI18nLocaleData/KCountry
/usr/include/KF6/KI18nLocaleData/KCountrySubdivision
/usr/include/KF6/KI18nLocaleData/KTimeZone
/usr/include/KF6/KI18nLocaleData/kcountry.h
/usr/include/KF6/KI18nLocaleData/kcountrysubdivision.h
/usr/include/KF6/KI18nLocaleData/ki18nlocaledata_export.h
/usr/include/KF6/KI18nLocaleData/ktimezone.h
/usr/lib64/cmake/KF6I18n/KF6I18nConfig.cmake
/usr/lib64/cmake/KF6I18n/KF6I18nConfigVersion.cmake
/usr/lib64/cmake/KF6I18n/KF6I18nMacros.cmake
/usr/lib64/cmake/KF6I18n/KF6I18nTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6I18n/KF6I18nTargets.cmake
/usr/lib64/cmake/KF6I18n/build-pofiles.cmake
/usr/lib64/cmake/KF6I18n/build-tsfiles.cmake
/usr/lib64/cmake/KF6I18n/kf6i18nuic.cmake
/usr/lib64/cmake/KF6I18n/ts-pmap-compile.py
/usr/lib64/libKF6I18n.so
/usr/lib64/libKF6I18nLocaleData.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6I18n.so.6.5.0
/V3/usr/lib64/libKF6I18nLocaleData.so.6.5.0
/V3/usr/lib64/qt6/plugins/kf6/ktranscript.so
/V3/usr/lib64/qt6/qml/org/kde/i18n/localeData/libki18nlocaledataqmlplugin.so
/usr/lib64/libKF6I18n.so.6
/usr/lib64/libKF6I18n.so.6.5.0
/usr/lib64/libKF6I18nLocaleData.so.6
/usr/lib64/libKF6I18nLocaleData.so.6.5.0
/usr/lib64/qt6/plugins/kf6/ktranscript.so
/usr/lib64/qt6/qml/org/kde/i18n/localeData/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/i18n/localeData/ki18nlocaledataqmlplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/i18n/localeData/libki18nlocaledataqmlplugin.so
/usr/lib64/qt6/qml/org/kde/i18n/localeData/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ki18n/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ki18n/28ba3ebe1aa04fad742c69eb685e2a5376e9276f
/usr/share/package-licenses/ki18n/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/ki18n/5ca60da87c5035ecdea20354a6f3fd079ac47c20
/usr/share/package-licenses/ki18n/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/ki18n/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ki18n/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/ki18n/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ki18n6.lang
%defattr(-,root,root,-)

