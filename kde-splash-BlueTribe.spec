
%define		_splash		BlueTribe

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=11573&id=1
Source0:	http://www.kde-look.org/content/files/11573-BlueTribe.tar.bz2
# Source0-md5:	dbfe91b1e960c7af6a35cc0a201c119c
URL:		http://www.kde-look.org/content/show.php?content=11573
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple KDE artwork in blue, with simple white KDE3 text.

%description -l pl
Proste elementy graficzne KDE w odcieniach niebieskich z bia³ym
napisem KDE3.

%prep
%setup -q -n %{_splash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
