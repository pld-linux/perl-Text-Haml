#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Haml
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Haml - Haml Perl implementation
Name:		perl-Text-Haml
Version:	0.990110
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/V/VT/VTI/Text-Haml-0.990110.tar.gz
# Source0-md5:	b3f422b25582c019fa667d5c8be49047
URL:		http://search.cpan.org/dist/Text-Haml/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Haml implements Haml
http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html specification.

Text::Haml passes specification tests written by Norman Clarke
http://github.com/norman/haml-spec and supports only cross-language Haml
features. Do not expect Ruby specific things to work.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/Haml
%{_mandir}/man3/*
