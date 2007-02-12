Summary:	Analog clock displaying the system-time
Summary(pl.UTF-8):	Zegar analogowy wyświetlający czas systemowy
Name:		cairo-clock
Version:	0.3.2
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://macslow.thepimp.net/projects/cairo-clock/%{name}-%{version}.tar.bz2
# Source0-md5:	6af19fc0df603f92e4f99c3bb5fb78cb
Patch0:		%{name}-glade.patch
URL:		http://macslow.thepimp.net/?page_id=23
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	librsvg-devel >= 1:2.13.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's an analog clock displaying the system-time. "So what?", you
might say, "There are about 1.023.493 of those already out there!".
Indeed there are and probably some more, but this one is a bit
different. It leverages the new visual features offered by
Xorg 6.9/7.0 in combination with a compositing-manager (e.g. like
xcompmgr), gtk+ 2.8.x, cairo 1.0.2 and librsvg 2.13.93 to produce
a time-display with pretty-pixels.

%description -l pl.UTF-8
To jest zegar analogowy wyświetlający czas systemowy. "I co z tego?" -
można zapytać - "Jest już około 1023493 takich programów!". Owszem,
jest pewnie jeszcze więcej, ale ten jest trochę inny. Wykorzystuje
nowe możliwości wyświetlania oferowane przez Xorg 6.9/7.0 w połączeniu
z zarządcą składania (np. xcompmgr), gtk+ 2.8.x, cairo 1.0.2 i librsvg
2.13.93 w celu stworzenia wyświetlacza z ładnymi pikselami.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
