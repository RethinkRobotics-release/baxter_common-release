Name:           ros-hydro-baxter-description
Version:        1.0.1
Release:        1%{?dist}
Summary:        ROS baxter_description package

Group:          Development/Libraries
License:        BSD
URL:            http://www.rethinkrobotics.com/sdk
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-hydro-catkin

%description
Description of Baxter Research Robot from Rethink Robotics. This package
contains the URDF and meshes describing Baxter.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Sep 10 2014 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.1-1
- Autogenerated by Bloom

* Wed Sep 10 2014 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.0.1-0
- Autogenerated by Bloom

