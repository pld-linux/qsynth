Summary:	Qt front-end to fluidsynth
Summary(pl):	Oparta o Qt nak³adka na fluidsynth
Name:		qsynth
Version:	0.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
# Source0-md5:	b13e8810652a4dfac8888d7669ddef5d
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://qsynth.sf.net/
BuildRequires:	fluidsynth-devel >= 1.0.0
BuildRequires:	qt-devel >= 3.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QSynth is a fluidsynth GUI front-end application.

%description -l pl
QSynth jest nak³adk± graficzn± na fluidsynth.

%prep
%setup -q
%patch -p1
perl -pi -e "s,QTDIR/include,QTDIR/include/qt,g" configure.in

%build
QTDIR=%{_prefix}
CFLAGS="$CFLAGS -I%{_includedir}/qt"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/qt"
export CFLAGS CPPFLAGS QTDIR

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.xpm
