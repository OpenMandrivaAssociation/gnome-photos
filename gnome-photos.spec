%define _disable_rebuild_configure 1
#define gi_major 3.0
#define girname %mklibname %{name}-gir %{gi_major}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define busname org.gnome.Photos

Summary:	Access, organize and share your photos
Name:		gnome-photos
Version:	3.18.2
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
URL:		http://www.gnome.org/
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(babl)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(gegl-0.3)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(grilo-0.2)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgfbgraph-0.2)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(tracker-control-1.0)
BuildRequires:	pkgconfig(tracker-sparql-1.0)
BuildRequires:	pkgconfig(libgdata)
Requires:	librsvg
Requires:	adwaita-icon-theme

%description
Access, organize and share your photos with GNOME 3.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-schemas-compile
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

find %{buildroot} -name '*.la' -delete

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_bindir}/%{name}
%{_datadir}/applications/%{busname}.desktop
%{_iconsdir}/*/*/*/*.*
%{_datadir}/appdata/%{busname}.appdata.xml
%{_datadir}/dbus-1/services/%{busname}.service
%{_datadir}/gnome-shell/search-providers/%{busname}.search-provider.ini


%changelog
* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796302
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 743190
- Second Mageia 5 Mass Rebuild

* Thu Sep 25 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 724591
- new version 3.14.0
- new version 3.13.92
- new version 3.13.91

  + umeabot <umeabot>
    - Mageia 5 Mass Rebuild

* Wed Jul 23 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 656039
- new version 3.13.4

* Sun May 04 2014 wally <wally> 3.12.1-2.mga5
+ Revision: 619944
- require adwaita-icon-theme instead of old gnome-icon-theme
- clean BRs

* Tue Apr 15 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 615118
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607840
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604409
- new version 3.11.92

* Wed Mar 05 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599973
- new version 3.11.91

* Thu Feb 20 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 595171
- new version 3.11.90

* Thu Feb 06 2014 ovitters <ovitters> 3.11.5-1.mga5
+ Revision: 584617
- new version 3.11.5

* Wed Feb 05 2014 ovitters <ovitters> 3.11.4-1.mga5
+ Revision: 583903
- new version 3.11.4

* Wed Nov 20 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 551977
- new version 3.10.2

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 542211
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 497099
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 483916
- new version 3.10.0
- dropped merged patch 1

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480953
- add patch to fix desktop file
- new version 3.9.92

* Mon Sep 02 2013 ennael <ennael> 3.9.91-2.mga4
+ Revision: 474377
- Rebuild against new gnome-desktop3

* Mon Sep 02 2013 ovitters <ovitters> 3.9.91-1.mga4
+ Revision: 474344
- new version 3.9.91

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468795
- new version 3.9.90

* Thu Aug 01 2013 dams <dams> 3.9.5.1-1.mga4
+ Revision: 462306
- adds 'grilo-0.2' as BR

  + ovitters <ovitters>
    - new version 3.9.5.1
    - new version 3.9.5

* Fri Jul 26 2013 dams <dams> 3.9.4-1.mga4
+ Revision: 458376
- new version 3.9.4

* Mon May 27 2013 ovitters <ovitters> 3.8.2-1.mga4
+ Revision: 428692
- imported package gnome-photos

