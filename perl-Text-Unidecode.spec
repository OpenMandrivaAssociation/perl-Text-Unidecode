%define upstream_name    Text-Unidecode
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*


