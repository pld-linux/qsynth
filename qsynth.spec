Summary:	Qt front-end to fluidsynth
Summary(pl.UTF-8):	Oparta o Qt nakładka na fluidsynth
Name:		qsynth
Version:	0.5.4
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
# Source0-md5:	bf82058d2ddaff989f9d1dfc58016bab
Patch0:		%{name}-soundfont_dir.patch
Patch1:		desktop_install.patch
URL:		http://qsynth.sourceforge.net/qsynth-index.html
BuildRequires:	Qt5Core-devel >= 5.1.0
BuildRequires:	Qt5Gui-devel >= 5.1.0
BuildRequires:	Qt5Widgets-devel >= 5.1.0
BuildRequires:	Qt5X11Extras-devel >= 5.1.0
BuildRequires:	cmake >= 2.6
BuildRequires:	fluidsynth-devel >= 2.0.0
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QSynth is a fluidsynth GUI front-end application.

%description -l pl.UTF-8
QSynth jest nakładką graficzną na fluidsynth.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mkdir -p build
cd build

%cmake \
	..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/appdata,%{_mandir}/man1}

cd build

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd ..

install -m 644 src/appdata/*.xml  $RPM_BUILD_ROOT%{_datadir}/appdata
install -m 644 qsynth.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %{name} --with-qm --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/appdata/*.xml
%{_pixmapsdir}/qsynth.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
