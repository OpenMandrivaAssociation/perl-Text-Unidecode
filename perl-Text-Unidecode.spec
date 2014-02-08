%define upstream_name    Text-Unidecode
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Represent Unicode data in US-ASCII characters
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-4mdv2012.0
+ Revision: 765762
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-3
+ Revision: 764288
- rebuilt for perl-5.14.x

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2
+ Revision: 655236
- rebuild for updated spec-helper

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 461712
- import perl-Text-Unidecode


* Fri Nov 06 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
