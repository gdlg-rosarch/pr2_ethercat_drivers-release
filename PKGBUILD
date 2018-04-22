# Script generated with Bloom
pkgdesc="ROS - This stack contains drivers for the ethercat system and the peripherals that connect to it: motor control boards, fingertip sensors, texture projector, hand accelerometer."
url='http://ros.org/wiki/pr2_ethercat_drivers'

pkgname='ros-kinetic-pr2-ethercat-drivers'
pkgver='1.8.18_2'
pkgrel=1
arch=('any')
license=('BSD'
'GPL'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-ethercat-hardware'
'ros-kinetic-fingertip-pressure'
)

conflicts=()
replaces=()

_dir=pr2_ethercat_drivers
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_ethercat_drivers $srcdir/pr2_ethercat_drivers
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

