Name:           ros-indigo-ethercat-hardware
Version:        1.8.13
Release:        1%{?dist}
Summary:        ROS ethercat_hardware package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ethercat_hardware
Source0:        %{name}-%{version}.tar.gz

Requires:       log4cxx-devel
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-eml
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-pr2-hardware-interface
Requires:       ros-indigo-pr2-msgs
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-roscpp
BuildRequires:  log4cxx-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-eml
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-pr2-hardware-interface
BuildRequires:  ros-indigo-pr2-msgs
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-roscpp

%description
Package for creating a hardware interface to the robot using the EtherCAT motor
controller/driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.8.13-1
- Autogenerated by Bloom

* Tue Jan 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.8.13-0
- Autogenerated by Bloom

