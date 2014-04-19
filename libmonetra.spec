%define major 7
%define libname %mklibname monetra %{major}
%define libmcve %mklibname mcve %{major}
%define devname %mklibname monetra -d

Summary:	Library to allow credit card processing through MCVE
Name:		libmonetra
Version:	7.13.0
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://www.mainstreetsoftworks.com/
Source0:	ftp://ftp.mcve.com/pub/libmonetra/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)

%description
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library to allow credit card processing through MCVE
Group:		System/Libraries

%description -n %{libname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%files -n %{libname}
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/libmonetra.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libmcve}
Summary:	Library to allow credit card processing through MCVE
Group:		System/Libraries
Conflicts:	%{_lib}monetra7 < 7.7.0

%description -n %{libmcve}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%files -n %{libmcve}
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/libmcve.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libmcve} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

This package contains development library and its header files.

%files -n %{devname}
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf
%configure2_5x --disable-static
%make

%install
%makeinstall_std

