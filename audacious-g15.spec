Name:                   audacious-g15
Version:                2.5.7
Release:                %mkrel 2
Summary:                Very simple spectrum analyser and oscilloscope for audacious
License:                GPLv2+
Group:                  Sound
URL:                    https://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15daemon-audacious-%{version}.tar.bz2
Patch: g15daemon-audacious-2.5.7-fix-build.patch
Provides:               g15daemon-audacious = %{version}-%{release}
Requires:               audacious-plugins
BuildRequires:          audacious-devel
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A very simple spectrum analyzer and oscilloscope for audacious.
Improvements and patches are welcome.

This plugin depends on glib devel and audacious devel packages.

%prep
%setup -q -n g15daemon-audacious-%{version}
%patch -p1

%build
%{configure2_5x} --disable-static
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} %{buildroot}%{_libdir}/audacious/Visualization/*.la

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS README
%defattr(-,root,root,0755)
%{_libdir}/audacious/Visualization/libg15daemon_audacious_spectrum.so
