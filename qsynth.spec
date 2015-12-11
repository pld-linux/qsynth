Summary:	Qt front-end to fluidsynth
Summary(pl.UTF-8):	Oparta o Qt nakładka na fluidsynth
Name:		qsynth
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
# Source0-md5:	47f9a2784082372689db9bf220afd63f
Patch0:		%{name}-soundfont_dir.patch
URL:		http://qsynth.sourceforge.net/qsynth-index.html
BuildRequires:	Qt5Core-devel >= 5.1.0
BuildRequires:	Qt5Gui-devel >= 5.1.0
BuildRequires:	Qt5Widgets-devel >= 5.1.0
BuildRequires:	Qt5X11Extras-devel >= 5.1.0
BuildRequires:	autoconf
BuildRequires:	fluidsynth-devel >= 1.0.0
BuildRequires:	qt4-qmake
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

%find_lang %{name} --with-qm --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/*.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/appdata/*.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
