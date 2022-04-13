%define _disable_rebuild_configure 1
#define gi_major 3.0
#define girname %mklibname %{name}-gir %{gi_major}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define busname org.gnome.Photos

Summary:	Access, organize and share your photos
Name:		gnome-photos
Version:	42.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0: 	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch1:         0001-Fix-build-failure-due-to-undefined-M_PI-constant.patch

URL:		http://www.gnome.org/
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(babl)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(gegl-0.4)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(grilo-0.3)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgfbgraph-0.2) >= 0.2.3
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(tracker-sparql-3.0)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(libdazzle-1.0)
BuildRequires:	pkgconfig(gexiv2)
BuildRequires:	pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(libjpeg)
Requires:	librsvg
Requires:	adwaita-icon-theme

%description
Access, organize and share your photos with GNOME 3.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

find %{buildroot} -name '*.la' -delete

%files -f %{name}.lang
%doc AUTHORS NEWS README ARTISTS COPYING
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_bindir}/%{name}
%{_datadir}/applications/%{busname}.desktop
%{_iconsdir}/*/*/*/*.*
%{_datadir}/metainfo/%{busname}.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Photos.service
%{_datadir}/gnome-shell/search-providers/%{busname}.search-provider.ini
%{_libexecdir}/gnome-photos-thumbnailer
%{_libdir}/gnome-photos/libgnome-photos.so
