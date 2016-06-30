%global strato_ver 1

Name:           lttng-ust
Version:        2.8.1
Release:        1.s%{strato_ver}%{?dist}
Summary:        LTTng Userspace Tracer library
Requires:       liburcu >= 0.8.4

Group:          Development/Libraries
License:        LGPLv2.1, MIT and GPLv2
URL:            http://www.lttng.org/ust
Source0:        http://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2
BuildRequires:  libtool, autoconf, automake, pkgconfig, liburcu-devel >= 0.8.4

%description
LTTng userspace tracer.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header to instrument applications using %{name}.

%prep
%setup -q

%build
%configure --disable-static --docdir=%{_docdir}/%{name}  --disable-java-agent-all
V=1 make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -vf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -vf $RPM_BUILD_ROOT/%{_datadir}/java/liblttng-ust-jul.jar

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_mandir}/man3/lttng-ust.3.gz
%{_mandir}/man3/lttng-ust-cyg-profile.3.gz
%{_mandir}/man3/lttng-ust-dl.3.gz
%{_mandir}/man3/do_tracepoint.3.gz
%{_mandir}/man3/tracef.3.gz
%{_mandir}/man3/tracelog.3.gz
%{_mandir}/man3/tracepoint.3.gz
%{_mandir}/man3/tracepoint_enabled.3.gz
%{_defaultdocdir}/%{name}/README.md
%{_defaultdocdir}/%{name}/ChangeLog
%{_defaultdocdir}/%{name}/java-agent.txt
%{_libdir}/liblttng-ust-ctl.so.*
%{_libdir}/liblttng-ust-cyg-profile-fast.so.*
%{_libdir}/liblttng-ust-cyg-profile.so.*
%{_libdir}/liblttng-ust-dl.so.*
%{_libdir}/liblttng-ust-fork.so.*
%{_libdir}/liblttng-ust-libc-wrapper.so.*
%{_libdir}/liblttng-ust-pthread-wrapper.so.*
%{_libdir}/liblttng-ust.so.*
%{_libdir}/liblttng-ust-tracepoint.so.*
%{_libdir}/liblttng-ust-python-agent.so.*

%files devel
%{_mandir}/man1/lttng-gen-tp.1.gz
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_defaultdocdir}/%{name}/examples/README
%{_defaultdocdir}/%{name}/examples/demo/*
%{_defaultdocdir}/%{name}/examples/easy-ust/*
%{_defaultdocdir}/%{name}/examples/gen-tp/*
%{_defaultdocdir}/%{name}/examples/hello-static-lib/*
%{_defaultdocdir}/%{name}/examples/demo-tracef/*
%{_defaultdocdir}/%{name}/examples/clock-override/*
%{_defaultdocdir}/%{name}/examples/demo-tracelog/*
%{_defaultdocdir}/%{name}/examples/getcpu-override/*
%{_bindir}/lttng-gen-tp

%changelog
* Thu Jun 30 2016 Rafael Buchbinder <rafi@stratoscale.com> 2.8.1-1
    - Update to strato 2.8.1
* Thu Jun 09 2016 Michael Jeanson <mjeanson@efficios.com> 2.8.0-1
    - Update to 2.8.0

* Fri Apr 22 2016 Michael Jeanson <mjeanson@efficios.com> 2.7.2-1
    - Update to 2.7.2

* Fri Jan 15 2016 Michael Jeanson <mjeanson@efficios.com> 2.7.1-1
    - Update to 2.7.1

* Fri Nov 13 2015 Michael Jeanson <mjeanson@efficios.com> 2.7.0-1
    - Update to 2.7.0

* Wed Jul 08 2015 Michael Jeanson <mjeanson@efficios.com> 2.6.2-3
    - Drop legacy java package

* Thu Jun 25 2015 Michael Jeanson <mjeanson@efficios.com> 2.6.2-2
    - Split java package in subpackages
    - Add log4j support to java-agent package

* Mon Jun 22 2015 Michael Jeanson <mjeanson@efficios.com> 2.6.2-1
    - Initial revision.
