#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       harbour-systemmonitor

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    System Monitor
Version:    0.6
Release:    25
Group:      Qt/Qt
License:    LICENSE
URL:        http://thecust.net/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-systemmonitor.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(keepalive)
BuildRequires:  desktop-file-utils

%description
System Monitor allows you to aggregate and graph system performance data.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5  \
    VERSION='%{version}-%{release}'

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%pre
# >> pre
su nemo -c "systemctl --user stop %{name}d"
exit 0
# << pre

%preun
# >> preun
su nemo -c "systemctl --user disable %{name}d"
su nemo -c "systemctl --user stop %{name}d"
# << preun

%post
# >> post
su nemo -c "systemctl --user daemon-reload"
su nemo -c "systemctl --user enable %{name}d"
su nemo -c "systemctl --user start %{name}d"
# << post

%postun
# >> postun
su nemo -c "systemctl --user daemon-reload"
# << postun

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_libdir}/systemd/user/%{name}d.service
# >> files
# << files
