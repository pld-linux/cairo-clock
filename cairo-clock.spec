Summary:	Analog clock displaying the system-time
Summary(pl.UTF-8):	Zegar analogowy wyświetlający czas systemowy
Name:		cairo-clock
Version:	0.3.3
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://macslow.thepimp.net/projects/cairo-clock/%{name}_%{version}-1.tar.gz
# Source0-md5:	2517b92e8ceea3dbb7df5d6c24d3d215
Patch0:		%{name}-glade.patch
Patch1:		%{name}-desktop.patch
URL:		http://macslow.thepimp.net/?page_id=23
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	librsvg-devel >= 1:2.14.0
BuildRequires:	pango-devel >= 1:1.10.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
Requires:	cairo >= 1.2.0
Requires:	glib2 >= 1:2.8.0
Requires:	gtk+2 >= 2:2.10.0
Requires:	libglade2 >= 1:2.6.0
Requires:	librsvg >= 1:2.14.0
Requires:	pango >= 1:1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's an analog clock displaying the system-time. "So what?", you
might say, "There are about 1.023.493 of those already out there!".
Indeed there are and probably some more, but this one is a bit
different. It leverages the new visual features offered by
Xorg 6.9/7.0 in combination with a compositing-manager (like compiz),
gtk+ 2.10.x, cairo 1.2.0 and librsvg 2.14.0 to produce a time-display
with pretty-pixels.

%description -l pl.UTF-8
To jest zegar analogowy wyświetlający czas systemowy. "I co z tego?" -
można zapytać - "Jest już około 1023493 takich programów!". Owszem,
jest pewnie jeszcze więcej, ale ten jest trochę inny. Wykorzystuje
nowe możliwości wyświetlania oferowane przez Xorg 6.9/7.0 w połączeniu
z zarządcą składania (np. compiz), gtk+ 2.10.x, cairo 1.2.0 i librsvg
2.14.0 w celu stworzenia wyświetlacza z ładnymi pikselami.

%prep
%setup -q
#%patch0 -p1
%patch -P1 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
