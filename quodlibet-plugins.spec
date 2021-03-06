#
Summary:	Quod Libet plugins
Summary(pl.UTF-8):	Wtyczki dla Quod Libet
Name:		quodlibet-plugins
Version:	3.0.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://quodlibet.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	52cffd62915cba963d6b902c9cdae927
URL:		http://code.google.com/p/quodlibet/
BuildRequires:	rpm-pythonprov
BuildRequires:	python-modules >= 2.6
Requires:	python-modules >= 2.6
Requires:	python-pygtk-gtk
Requires:	quodlibet >= 2.9.91
Suggests:	python-CDDB
Suggests:	python-dbus
Suggests:	python-gnome-vfs
Suggests:	python-gstreamer
Suggests:	python-musicbrainz2
Suggests:	python-mutagen
Suggests:	python-pycairo
Suggests:	python-pygtk-pango
Suggests:	python-pyinotify
Suggests:	python-zeitgeist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quod Libet is a GTK+-based audio player written in Python.

This package provides various plugins for the player.

%description -l pl.UTF-8
Quod Libet to oparty na GTK+ odtwarzacz dźwięku napisany w Pythonie.

Ten pakiet dostarcza różne wtyczki dla tego odtwarzacza.

%prep
%setup -q
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/quodlibet/plugins

cp -r editing events playorder songsmenu $RPM_BUILD_ROOT%{py_sitedir}/quodlibet/plugins

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/quodlibet/plugins/editing
%{py_sitedir}/quodlibet/plugins/editing/*.py
%{py_sitedir}/quodlibet/plugins/editing/*.py[co]
%dir %{py_sitedir}/quodlibet/plugins/events
%{py_sitedir}/quodlibet/plugins/events/*.py
%{py_sitedir}/quodlibet/plugins/events/*.py[co]
%dir %{py_sitedir}/quodlibet/plugins/playorder
%{py_sitedir}/quodlibet/plugins/playorder/*.py
%{py_sitedir}/quodlibet/plugins/playorder/*.py[co]
%dir %{py_sitedir}/quodlibet/plugins/songsmenu
%{py_sitedir}/quodlibet/plugins/songsmenu/*.py
%{py_sitedir}/quodlibet/plugins/songsmenu/*.py[co]
