Name: monitorix
Version: 3.13.1
Release: alt1

Summary: A free, open source, lightweight system monitoring tool
Group: Monitoring
License: GPLv2
Url: https://github.com/mikaku/Monitorix

Packager: Andrey Limachko <liannnix@altlinux.org>

#Source0: https://github.com/mikaku/Monitorix/archive/refs/tags/v%version.tar.gz
#Source1: monitorix.conf
Source: %name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: perl
#Requires: perl(IO/Socket/SSL.pm)

%description
Monitorix is a free, open source and lightweight system monitoring tool
designed to monitor as many services and system resources as possible. It has
been created to be used under production Linux/UNIX servers, but due to its
simplicity and small size may also be used on embedded devices as well.

%prep
%setup -n %name-%version

%install
%make_install DESTDIR=%buildroot install-systemd-all

%files
%doc Changes README README.md README.nginx docs/
%_libexecdir/*
%_localstatedir/*
%_bindir/*
%_man5dir/*
%_man8dir/*



%changelog
* Sun Oct 03 2021 Andrey Limachko <liannnix@altlinux.org> 3.13.1-alt1
Initial build

