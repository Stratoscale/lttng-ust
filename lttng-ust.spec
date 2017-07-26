Name:           lttng-ust
Version:        2.9.1
Release:        1%{?dist}
Summary:        LTTng Userspace Tracer library
Requires:       liburcu >= 0.8.4

Group:          Development/Libraries
License:        LGPLv2.1, MIT and GPLv2
URL:            http://www.lttng.org/ust
Source0:        http://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2
BuildRequires:  libtool, autoconf, automake, pkgconfig, liburcu-devel >= 0.8.4, java-1.7.0-openjdk-devel, log4j

%description
LTTng userspace tracer.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header to instrument applications using %{name}.

%package        java
Summary:        Development files for %{name} Java UST support
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}, java-1.7.0-openjdk
Obsoletes:      %{name}-java-old

%description    java
The %{name}-java package contains libraries and class files needed to instrument java applications.

%package        java-agent
Summary:        Development files for %{name} JUL and log4j support
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}, java-1.7.0-openjdk, log4j

%description    java-agent
The %{name}-java-agent package contains libraries and class files needed to instrument applications that use %{name}'s Java Util Logging and log4j backends.

%package -n     python33-lttngust
%global scl_python python33
%global scl %{scl_python}
%global _scl_root /opt/rh/%{scl_python}/root
%global __python %{_scl_root}%{__python}
%global scl_prefix %{scl_python}-
%global __python_requires %{%{scl_python}_python_requires}
%global __python_provides %{%{scl_python}_python_provides}
%global __os_install_post %{python33_os_install_post}
%global python_sitearch %{_scl_root}/%{_libdir}/python3.3/site-packages
%global python_sitelib %{_scl_root}/usr/lib/python3.3/site-packages
Summary:        Python bindings for LTTng UST
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}, python33
BuildRequires:  python33-scldevel, python33-python-devel

%description -n python33-lttngust
The python3-lttngust package contains libraries needed to instrument applications that use %{name}'s Python logging backend.


%prep
%setup -q

%build
PYTHON=%{python33__python3}
PYTHON_CONFIG="/opt/rh/python33/root/bin/python3-config"
PYTHON_PREFIX="/opt/rh/python33/root/"
source /opt/rh/python33/enable
export CLASSPATH="$(build-classpath log4j)"
%configure --docdir=%{_docdir}/%{name} --enable-jni-interface --enable-java-agent-all --enable-python-agent
make %{?_smp_mflags} V=1

%install
PYTHON=%{python33__python3}
PYTHON_CONFIG="/opt/rh/python33/root/bin/python3-config"
PYTHON_PREFIX="/opt/rh/python33/root/"
source /opt/rh/python33/enable
make install DESTDIR=$RPM_BUILD_ROOT
rm -vf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/java/liblttng-ust-jul.jar

# Copy the installed Python files to the SCL Python path
mkdir -p ${RPM_BUILD_ROOT}%{python_sitelib}/
mv ${RPM_BUILD_ROOT}/usr/lib/python3.3/site-packages/* ${RPM_BUILD_ROOT}%{python_sitelib}/


%check
PYTHON=%{python33__python3}
PYTHON_CONFIG="/opt/rh/python33/root/bin/python3-config"
PYTHON_PREFIX="/opt/rh/python33/root/"
source /opt/rh/python33/enable
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
%{_libdir}/liblttng-ust-fd.so.*

%files devel
%{_mandir}/man1/lttng-gen-tp.1.gz
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/lttng-ust*.pc
%{_defaultdocdir}/%{name}/examples/README
%{_defaultdocdir}/%{name}/examples/demo/*
%{_defaultdocdir}/%{name}/examples/easy-ust/*
%{_defaultdocdir}/%{name}/examples/gen-tp/*
%{_defaultdocdir}/%{name}/examples/hello-static-lib/*
%{_defaultdocdir}/%{name}/examples/demo-tracef/*
%{_defaultdocdir}/%{name}/examples/clock-override/*
%{_defaultdocdir}/%{name}/examples/demo-tracelog/*
%{_defaultdocdir}/%{name}/examples/getcpu-override/*
%{_defaultdocdir}/%{name}/examples/python/*
%{_defaultdocdir}/%{name}/examples/cmake-multiple-shared-libraries/*
%{_bindir}/lttng-gen-tp

%files java
%{_datadir}/java/liblttng-ust-java.jar
%{_libdir}/liblttng-ust-java.so*

%files java-agent
%{_defaultdocdir}/%{name}/java-agent.txt
%{_defaultdocdir}/%{name}/examples/java-jul/*
%{_defaultdocdir}/%{name}/examples/java-log4j/*
%{_datadir}/java/lttng-ust-agent*.jar
%{_datadir}/java/liblttng-ust-agent.jar
%{_libdir}/liblttng-ust-jul-jni.so*
%{_libdir}/liblttng-ust-log4j-jni.so*
%{_libdir}/liblttng-ust-context-jni.so*

%files -n python33-lttngust
%{python_sitelib}/lttngust-%{version}-py3.3.egg-info
%{python_sitelib}/lttngust/*

%changelog
* Tue Jun 20 2017 Michael Jeanson <mjeanson@efficios.com> 2.9.1-1
    - Updated to 2.9.1

* Wed Dec 07 2016 Michael Jeanson <mjeanson@efficios.com> 2.9.0-1
    - Updated to 2.9.0

* Tue Aug 30 2016 Michael Jeanson <mjeanson@efficios.com> 2.8.1-1
    - Updated to 2.8.1

* Wed Jun 08 2016 Michael Jeanson <mjeanson@efficios.com> 2.8.0-1
    - Updated to 2.8.0

* Thu Apr 21 2016 Michael Jeanson <mjeanson@efficios.com> 2.7.2-1
    - Updated to 2.7.2

* Thu Jan 14 2016 Michael Jeanson <mjeanson@efficios.com> 2.7.1-1
    - Updated to 2.7.1

* Tue Nov 10 2015 Michael Jeanson <mjeanson@efficios.com> 2.7.0-1
    - Updated to 2.7.0
    - Dropped java-old subpackage

* Thu Jun 25 2015 Michael Jeanson <mjeanson@efficios.com> 2.6.2-2
    - Split java package in subpackages
    - Add log4j support to java-agent package

* Mon Jun 22 2015 Michael Jeanson <mjeanson@efficios.com> 2.6.2-1
    - Initial revision.
