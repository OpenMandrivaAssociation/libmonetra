%define	major 7
%define libname %mklibname monetra %{major}
%define develname %mklibname monetra -d

Summary:	Library to allow credit card processing through MCVE
Name:		libmonetra
Version:	7.0.5
Release:	%mkrel 3
Group:		System/Libraries
License:	BSD
URL:		http://www.mainstreetsoftworks.com/
Source0:	ftp://ftp.mcve.com/pub/libmonetra/%{name}-%{version}.tar.gz
BuildRequires:	autoconf2.5
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
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 7.0.5-3mdv2011.0
+ Revision: 609758
- rebuild

* Tue Apr 20 2010 Funda Wang <fwang@mandriva.org> 7.0.5-2mdv2010.1
+ Revision: 536955
- rebuild

* Sun Dec 27 2009 Oden Eriksson <oeriksson@mandriva.com> 7.0.5-1mdv2010.1
+ Revision: 482802
- 7.0.5

* Tue May 19 2009 Oden Eriksson <oeriksson@mandriva.com> 7.0.4-1mdv2010.0
+ Revision: 377610
- 7.0.4
- fix build

* Wed Apr 01 2009 Oden Eriksson <oeriksson@mandriva.com> 7.0.0-3mdv2009.1
+ Revision: 363368
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 7.0.0-2mdv2009.0
+ Revision: 267919
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 06 2008 Oden Eriksson <oeriksson@mandriva.com> 7.0.0-1mdv2009.0
+ Revision: 201821
- 7.0.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2-2mdv2008.0
+ Revision: 83686
- new devel naming


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 5.2-1mdv2007.0
+ Revision: 93722
- Import libmonetra

* Sat Feb 04 2006 Oden Eriksson <oeriksson@mandriva.com> 5.2-1mdk
- initial Mandriva package

