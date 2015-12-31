Name:           ros-indigo-baxter-maintenance-msgs
Version:        1.2.0
Release:        0%{?dist}
Summary:        ROS baxter_maintenance_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://sdk.rethinkrobotics.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Messages and Services required for use with maintenance procedures with the
Baxter Research Robot from Rethink Robotics.

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
* Thu Dec 31 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.2.0-0
- Autogenerated by Bloom

* Mon May 18 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.1.1-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.1.0-1
- Autogenerated by Bloom

* Mon Feb 02 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.1.0-0
- Autogenerated by Bloom

