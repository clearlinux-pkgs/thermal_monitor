#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thermal_monitor
Version  : 1.8
Release  : 7
URL      : https://github.com/intel/thermal_daemon/archive/v1.8.tar.gz
Source0  : https://github.com/intel/thermal_daemon/archive/v1.8.tar.gz
Summary  : The "Linux Thermal Daemon" program from 01.org
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0
Requires: thermal_monitor-bin = %{version}-%{release}
Requires: thermal_monitor-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : gettext
BuildRequires : mesa-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(libxml-2.0)

%description
Thermal Daemon monitors and controls platform temperature.

%package bin
Summary: bin components for the thermal_monitor package.
Group: Binaries
Requires: thermal_monitor-license = %{version}-%{release}

%description bin
bin components for the thermal_monitor package.


%package license
Summary: license components for the thermal_monitor package.
Group: Default

%description license
license components for the thermal_monitor package.


%prep
%setup -q -n thermal_daemon-1.8
cd %{_builddir}/thermal_daemon-1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
pushd tools/thermal_monitor
%qmake -config ltcg -config fat-static-lto  ThermalMonitor.pro
test -r config.log && cat config.log
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604355829
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/thermal_monitor
cp %{_builddir}/thermal_daemon-1.8/COPYING %{buildroot}/usr/share/package-licenses/thermal_monitor/b3aebbdebf056cbf1cb73b76edf8ea105c37239d
cp %{_builddir}/thermal_daemon-1.8/tools/thermal_monitor/qcustomplot/GPL.txt %{buildroot}/usr/share/package-licenses/thermal_monitor/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd tools/thermal_monitor
%make_install
popd
## install_append content
install -D -m0755 tools/thermal_monitor/ThermalMonitor %{buildroot}/usr/bin/ThermalMonitor
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ThermalMonitor

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/thermal_monitor/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/thermal_monitor/b3aebbdebf056cbf1cb73b76edf8ea105c37239d
