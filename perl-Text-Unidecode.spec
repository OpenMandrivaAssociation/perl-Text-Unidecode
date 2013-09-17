%define modname	Text-Unidecode
%define modver	0.04

Summary:	Represent Unicode data in US-ASCII characters
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
It often happens that you have non-Roman text data in Unicode, but you
can't display it -- usually because you're trying to show it to a user via
an application that doesn't support Unicode, or because the fonts you need
aren't accessible. You could represent the Unicode characters as "???????"
or "\15BA\15A0\1610...", but that's nearly useless to the user who actually
wants to read what the text says.

What Text::Unidecode provides is a function, 'unidecode(...)' that takes
Unicode data and tries to represent it in US-ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at _transliteration_ -- i.e.,
conveying, in Roman letters, the pronunciation expressed by the text in
some other writing system. (See the example in the synopsis.)

Unidecode's ability to transliterate is limited by two factors:

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{perl_vendorlib}/*
%{_mandir}/man3/*

