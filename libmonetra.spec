%define	major 7
%define libname %mklibname monetra %{major}
%define develname %mklibname monetra -d

Summary:	Library to allow credit card processing through MCVE
Name:		libmonetra
Version:	7.0.0
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://www.mainstreetsoftworks.com/
Source0:	ftp://ftp.mcve.com/pub/libmonetra/%{name}-%{version}.tar.gz
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{libname}
Summary:	Library to allow credit card processing through MCVE
Group:          System/Libraries

%description -n	%{libname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname monetra 5 -d}

%description -n	%{develname}
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
rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
