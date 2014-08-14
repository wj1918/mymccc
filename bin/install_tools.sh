#!/bin/sh
#
# install required tools 
#

install_glib2()
{
    # install glib-2.0
    RPM=glib2-2.26.1-3.el6.x86_64.rpm
    curl -0 http://mirror.centos.org/centos/6/os/x86_64/Packages/$RPM > $RPM
    rpm2cpio $RPM | cpio -idmv
    rm $RPM
    RPM=glib2-devel-2.26.1-3.el6.x86_64.rpm
    curl -0 http://mirror.centos.org/centos/6/os/x86_64/Packages/$RPM > $RPM
    rpm2cpio $RPM | cpio -idmv
    rm $RPM
    PCDIR=usr/lib64/pkgconfig
    cd $PCDIR
    newdir=$(echo $RUN_DIR |sed 's/\//\\\//g')usr
    sed -i "s/\/usr/$newdir/g" *.pc
}

install_libtool()
{
    #build libtool
    cd  $RUN_DIR/build
    rm  libtool-2.4.2.tar.gz 
    wget  http://ftpmirror.gnu.org/libtool/libtool-2.4.2.tar.gz 
    tar xfz libtool-2.4.2.tar.gz 
    cd libtool-2.4.2 
    ./configure --prefix=$RUN_DIR/usr
    make
    make install
}

install_mdbtool()
{
    # build mdbtool
    cd  $RUN_DIR/build
    git clone https://github.com/wj1918/mdbtools.git 
    cd mdbtools
    export ACLOCAL_PATH=`aclocal --print-ac-dir`:$RUN_DIR/usr/share/aclocal
    libtoolize
    autoreconf -i -f
    ./configure --disable-gmdb2 --disable-scrollkeeper --disable-man --prefix=$RUN_DIR/usr
    make
    make install
}

cleanup()
{
    if [[ -r build ]] ; then
	rm -rf build
    fi
    mkdir build
    rm -rf usr lib64 etc
}

RUN_DIR=$OPENSHIFT_DATA_DIR
if [ -f $OPENSHIFT_DATA_DIR/server.conf ]
  then
    . $OPENSHIFT_DATA_DIR/server.conf
fi

PATH=$RUN_DIR/usr/bin:$PATH

if [[ ! -f $RUN_DIR/usr/bin/mdb-schema ]]; then
    cd $RUN_DIR
    cleanup

    install_glib2

    PKG_CONFIG_PATH=$RUN_DIR/usr/lib64/pkgconfig

    install_libtool
    install_mdbtool

    echo "done."
fi 
