Name:           lttng-ust
Version:        2.6.2
Release:        1%{?dist}
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

%package        java
Summary:        Development files for %{name} JUL support
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    java
The %{name}-java package contains libraries and class files needed to instrument applications that use %{name}'s Java Util Logging backend.

%prep
%setup -q

%build
%configure --disable-static --docdir=%{_docdir}/%{name}  --disable-java-agent-all
V=1 make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -vf $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_mandir}/man3/lttng-ust.3.gz
%{_mandir}/man3/lttng-ust-cyg-profile.3.gz
%{_mandir}/man3/lttng-ust-dl.3.gz
%{_defaultdocdir}/%{name}/README.md
%{_defaultdocdir}/%{name}/ChangeLog
%{_libdir}/liblttng-ust-ctl.so.*
%{_libdir}/liblttng-ust-cyg-profile-fast.so.*
%{_libdir}/liblttng-ust-cyg-profile.so.*
%{_libdir}/liblttng-ust-dl.so.*
%{_libdir}/liblttng-ust-fork.so.*
%{_libdir}/liblttng-ust-libc-wrapper.so.*
%{_libdir}/liblttng-ust-pthread-wrapper.so.*
%{_libdir}/liblttng-ust.so.*
%{_libdir}/liblttng-ust-tracepoint.so.*

%files devel
%{_mandir}/man1/lttng-gen-tp.1.gz
%{_includedir}/*
%{_libdir}/liblttng-ust-ctl.so
%{_libdir}/liblttng-ust-cyg-profile-fast.so
%{_libdir}/liblttng-ust-cyg-profile.so
%{_libdir}/liblttng-ust-dl.so
%{_libdir}/liblttng-ust-fork.so
%{_libdir}/liblttng-ust-libc-wrapper.so
%{_libdir}/liblttng-ust-pthread-wrapper.so
%{_libdir}/liblttng-ust.so
%{_libdir}/liblttng-ust-tracepoint.so
%{_libdir}/pkgconfig/lttng-ust*.pc
%{_defaultdocdir}/%{name}/examples/README
%{_defaultdocdir}/%{name}/examples/demo/*
%{_defaultdocdir}/%{name}/examples/easy-ust/*
%{_defaultdocdir}/%{name}/examples/gen-tp/*
%{_defaultdocdir}/%{name}/examples/hello-static-lib/*
%{_defaultdocdir}/%{name}/examples/demo-tracef/*
%{_bindir}/lttng-gen-tp

#%files java
#%{_defaultdocdir}/%{name}/java-agent.txt
#%{_defaultdocdir}/%{name}/examples/java-jul/*
#%{_datadir}/java/*
#%{_libdir}/liblttng-ust-jul-jni.so*
#%{_libdir}/liblttng-ust-java.so*

%changelog
* Mon Jun 22 2015 Michael Jeanson <mjeanson@efficios.com> 2.6.2-1
    - Initial revision.
