Name:    libvibrant
Version: 1
Release: 1
Summary: libvibrant

Source0: CMakeLists.txt

License: GPL-3

Requires(post): info
Requires(preun): info

Requires: cmake

BuildArch: noarch

%description
Script to install libvibrant.

%install
mkdir -p build
cmake ..
make install

%post

%preun

%files
%{_bindir}/CMakeLists.txt

%changelog
