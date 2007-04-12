%define	major 5
%define libname	%mklibname monetra %{major}

Summary:	Library to allow credit card processing through MCVE
Name:		libmonetra
Version:	5.2
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://www.mainstreetsoftworks.com/
Source0:	ftp://ftp.mcve.com/pub/libmonetra/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{libname}
Summary:	Library to allow credit card processing through MCVE
Group:          System/Libraries

%description -n	%{libname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

This package contains the static %{name} library and its header
files.

%prep

%setup -q -n %{name}-%{version}

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal-1.7; autoconf; automake-1.7 --add-missing --copy

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


