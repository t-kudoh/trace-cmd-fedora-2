#%global checkout 20130723git07f0eee2
# git tag
%global git_commit trace-cmd-v2.2.1

Name: trace-cmd
Version: 2.2.1
Release: 2%{?dist}
License: GPLv2 and LGPLv2
Summary: A user interface to Ftrace

Group: Development/Tools
URL: http://git.kernel.org/?p=linux/kernel/git/rostedt/trace-cmd.git;a=summary
# Upstream does not provide tarballs.
# To generate:
# git clone git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git
# cd trace-cmd
# git archive --prefix=trace-cmd-%%{version}/ -o trace-cmd-%%{version}.tar.gz %%{git_commit}
Source0: trace-cmd-%{version}.tar.gz
Source1: kernelshark.desktop
Patch1: trace-cmd-2.1.0-plugin-dir.patch

BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: mlocate
# needed for the GUI parts
BuildRequires: libxml2-devel
BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils

%description
trace-cmd is a user interface to Ftrace. Instead of needing to use the
debugfs directly, trace-cmd will handle of setting of options and
tracers and will record into a data file.

%package -n kernelshark
Summary: GUI analysis for Ftrace data captured by trace-cmd
Group: Development/Tools
Requires: trace-cmd%{_isa} = %{version}-%{release}

%description -n kernelshark
Kernelshark is the GUI frontend for analyzing data produced by
'trace-cmd extract'

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build
# MANPAGE_DOCBOOK_XSL define is hack to avoid using locate
MANPAGE_DOCBOOK_XSL=`rpm -ql docbook-style-xsl | grep manpages/docbook.xsl`
make V=1 CFLAGS="%{optflags} -D_GNU_SOURCE" MANPAGE_DOCBOOK_XSL=$MANPAGE_DOCBOOK_XSL prefix=%{_prefix} all doc gui


%install
make V=1 DESTDIR=%{buildroot} prefix=%{_prefix} install install_doc install_gui
find %{buildroot}%{_mandir} -type f | xargs chmod u-x,g-x,o-x
find %{buildroot}%{_datadir} -type f | xargs chmod u-x,g-x,o-x
install -dm 755 %{buildroot}/%{_datadir}/applications
install -pm 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/kernelshark.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kernelshark.desktop

%files
%doc COPYING COPYING.LIB README
%{_bindir}/trace-cmd
%{_libdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n kernelshark
%{_bindir}/trace-view
%{_bindir}/trace-graph
%{_bindir}/kernelshark
%{_datadir}/kernelshark
%{_datadir}/applications/kernelshark.desktop


%changelog
* Wed Jul 24 2013 Jon Stanley <jonstanley@gmail.com> - 2.2.1-2
- Remove addition to %%files - not needed with Makefile patch

* Tue Jul 23 2013 Dwight Engen <dwight.engen@oracle.com> - 2.2.1-1
- Update to 2.2.1

* Wed Feb 13 2013 Jon Stanley <jonstanley@gmail.com> - 2.1.0-1
- Update to latest upstream

* Thu Sep 13 2012 Jon Stanley <jonstanley@gmail.com> - 1.2-4.20120606git8266dff
- Remove %%defattr

* Thu Sep 06 2012 Jon Stanley <jonstanley@gmail.com> - 1.2-3.20120606git8266dff
- More review fixups

* Tue Aug 28 2012 Jon Stanley <jonstanley@gmail.com> - 1.2-2.20120606git8266dff
- Rebase to git snapshot so it builds
- Fix license tag per review
- Move plugin dir per review

* Mon Aug 27 2012 Jon Stanley <jonstanley@gmail.com> - 1.2-1
- Rebase to 1.2
- Makefile now supports CFLAGS, drop patch

* Sat Feb 19 2011 Jon Stanley <jonstanley@gmail.com> - 1.0.5-1
- Rebase to 1.0.5
- Add Makefile patch to support passing RPM_OPT_FLAGS
- Add kernelshark subpackage
- Initial Fedora version

* Mon Jul 5 2010 John Kacur <jkacur@redhat.com> - 1.0.4-7
- Rebasing to trace-cmd-1.0.4

* Wed Jun 16 2010 John Kacur <jkacur@redhat.com>
- Rebasing to trace-cmd-1.0.2
- Added parse-events-Do-not-fail-on-FORMAT-TOO-BIG-event-err.patch
- Added trace-cmd-Prevent-latency-tracer-plugins-from-doing-.patch
- Added trace-cmd-Prevent-print_graph_duration-buffer-overfl.patch

* Wed Jun 9 2010 John Kacur <jkacur@redhat.com>
- Added trace-cmd-Makefile-EXTRAVERSION-should-be-set-withou.patch
- Added trace-cmd-Makefile-use-a-substitution-reference.patch
- add-DESTDIR-to-make.patch
- Related: rhbz599507

* Fri Jun 4 2010 John Kacur <jkacur@redhat.com>
- Updating to trace-cmd-1.0.1
- Related: rhbz599507

* Wed Apr 21 2010 John Kacur <jkacur@redhat.com>
- Using trick from William Cohen to avoid the "locate" problem.

* Fri Apr 16 2010 John Kacur <jkacur@redhat.com>
- Update the source to the 1.0.0 version
- Many fixes to the spec file.

* Mon Apr 12 2010 William Cohen <wcohen@redhat.com>
- Include manpages in the package.

* Fri Apr 9 2010 John Kacur <jkacur@redhat.com>
- disabled #patch01
- Updated the trace-cmd source
- Changed version to 0.7.0
- Added bogus patch to satisfy rpm requirements
- Related:bz519630

* Mon Mar 15 2010 John Kacur <jkacur@redhat.com>
- disabled trace-cmd_rusage.patch
- Updated the trace-cmd source
- Related:bz519630

* Fri Nov 16 2007 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.0-1%{?dist}
- Initial packaging
- Added a patch to display rusage information
