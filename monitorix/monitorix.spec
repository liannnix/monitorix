Name: monitorix
Version: 3.13.1
Release: alt1

Summary: A free, open source, lightweight system monitoring tool
Group: Monitoring
License: GPLv2
Url: https://github.com/mikaku/Monitorix

Source: %name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Module-Build

BuildRequires: perl
BuildRequires: perl(CGI.pm)
BuildRequires: perl(Config/General.pm)
BuildRequires: perl(MailTools.pm)
BuildRequires: perl(MIME/Lite.pm)
BuildRequires: perl(DBI.pm)
BuildRequires: perl(XML/Simple.pm)
BuildRequires: perl(XML/LibXML.pm)
BuildRequires: perl(HTTP/Server/Simple.pm)
BuildRequires: perl(IO/Socket/SSL.pm)
BuildRequires: perl(RRDs.pm)

Requires: perl
Requires: perl(CGI.pm)
Requires: perl(Config/General.pm)
Requires: perl(MailTools.pm)
Requires: perl(MIME/Lite.pm)
Requires: perl(DBI.pm)
Requires: perl(XML/Simple.pm)
Requires: perl(XML/LibXML.pm)
Requires: perl(HTTP/Server/Simple.pm)
Requires: perl(IO/Socket/SSL.pm)
Requires: perl(RRDs.pm)
Requires: rrd-utils

%description
Monitorix is a free, open source and lightweight system monitoring tool
designed to monitor as many services and system resources as possible. It has
been created to be used under production Linux/UNIX servers, but due to its
simplicity and small size may also be used on embedded devices as well.

%prep
%setup -n %name-%version

%install
%make_install DOCDIR=%_defaultdocdir/%name-%version LIBDIR=%perl_vendor_archlib DESTDIR=%buildroot install-systemd-all

%files
%doc COPYING Changes README README.md README.nginx
%doc docs/htpasswd.pl docs/monitorix-alert.sh docs/monitorix-apache.conf docs/monitorix-lighttpd.conf
%config %_logrotatedir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_libexecdir/*
%_localstatedir/*
%_bindir/*
%perl_vendor_archlib
%_mandir/*

%changelog
* Sun Oct 03 2021 Andrey Limachko <liannnix@altlinux.org> 3.13.1-alt1
Initial build

