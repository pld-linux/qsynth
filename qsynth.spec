Summary:	Qt front-end to fluidsynth
Summary(pl.UTF-8):   Oparta o Qt nakładka na fluidsynth
Name:		qsynth
Version:	0.2.5
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
# Source0-md5:	24a1ce00876a79a409fa28d0e8b3221f
Source1:	%{name}.desktop
URL:		http://qsynth.sourceforge.net/qsynth-index.html
BuildRequires:	autoconf
BuildRequires:	fluidsynth-devel >= 1.0.0
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.1.1
BuildRequires:	sed >= 4.0
# because of EA in fluidsynth
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QSynth is a fluidsynth GUI front-end application.

%description -l pl.UTF-8
QSynth jest nakładką graficzną na fluidsynth.

%prep
%setup -q

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
install icons/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
