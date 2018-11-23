%define _disable_rebuild_configure 1
#define gi_major 3.0
#define girname %mklibname %{name}-gir %{gi_major}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define busname org.gnome.Photos

Summary:	Access, organize and share your photos
Name:		gnome-photos
Version:	3.30.1
Release:	1
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
BuildRequires:	pkgconfig(gegl-0.4)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(grilo-0.3)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libexif)
#Temporary disabled
BuildRequires:	pkgconfig(libgfbgraph-0.2) >= 0.2.3
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(tracker-control-2.0)
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:	pkgconfig(libdazzle-1.0)
BuildRequires:	pkgconfig(gexiv2)
BuildRequires:	pkgconfig(geocode-glib-1.0)
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
