%define		ocaml_ver	1:3.09.2
Summary:	Thread-safe Str replacement
Summary(pl.UTF-8):	Wielowątkowy zastępca modułu Str
Name:		ocaml-xstr
Version:	0.2.1
Release:	8
License:	BSD
Group:		Libraries
URL:		http://www.ocaml-programming.de/packages/
Source0:	http://www.ocaml-programming.de/packages/xstr-%{version}.tar.gz
# Source0-md5:	81598c438d6ab5c5d544ea7cc6ed8a34
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package implements frequent string operations: searching,
replacing, splitting, matching. It is independent from the Str
library, and can replace Str in many cases. Unlike Str, xstr is
thread-safe. xstr does not implement regular expressions in general,
but an important subset.

%description -l pl.UTF-8
Pakiet ten implementuje częste operacje na łańcuchach znaków:
szukanie, zamianę, dzielenie i dopasowywanie wzorca. Jest niezależny
od biblioteki Str, i może ją w wielu wypadkach zastąpić. W
przeciwieństwie do Str można go używać w programach wielowątkowych.
Xstr nie implementuje wyrażeń regularnych w całości, tylko pewien
ważny podzbiór.

%package devel
Summary:	Thread-safe Str replacement - development part
Summary(pl.UTF-8):	Wielowątkowy zastępca modułu Str - cześć programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
This package implements frequent string operations: searching,
replacing, splitting, matching. It is independent from the Str
library, and can replace Str in many cases. Unlike Str, xstr is
thread-safe. xstr does not implement regular expressions in general,
but an important subset.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Pakiet ten implementuje częste operacje na łańcuchach znaków:
szukanie, zamianę, dzielenie i dopasowywanie wzorca. Jest niezależny
od biblioteki Str, i może ją w wielu wypadkach zastąpić. W
przeciwieństwie do Str można go używać w programach wielowątkowych.
Xstr nie implementuje wyrażeń regularnych w całości, tylko pewien
ważny podzbiór.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%prep
%setup -q -n xstr

%build
sed -e 's/-g//; s/\*.cmxa/& \*.cmx/' Makefile > Makefile.tmp
mv -f Makefile.tmp Makefile
%{__make} all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/xstr
OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml %{__make} install
echo 'directory = "+xstr"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/xstr/META
mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/xstr/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/xstr/META

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README *.mli
%{_libdir}/ocaml/xstr/*.cm[ixa]*
%{_libdir}/ocaml/xstr/*.a
%{_libdir}/ocaml/site-lib/xstr
