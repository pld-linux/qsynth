Summary:	Qt front-end to fluidsynth
Summary(pl):	Oparta o Qt nak³adka na fluidsynth
Name:		qsynth
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
# Source0-md5:	869bc10613a1437856f5890f5baf6b80
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://qsynth.sf.net/
BuildRequires:	autoconf
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

%build
QTDIR=%{_prefix}
CFLAGS="$CFLAGS -I%{_includedir}/qt"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/qt"
export CFLAGS CPPFLAGS QTDIR
%{__autoconf}
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
