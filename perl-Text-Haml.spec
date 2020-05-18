#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Haml
Summary:	Text::Haml - Haml Perl implementation
Summary(pl.UTF-8):	Text::Haml - implementacja Haml dla Perla
Name:		perl-Text-Haml
Version:	0.990118
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Haml-%{version}.tar.gz
# Source0-md5:	7f0b65b62e2515a46425ca35bf2b4808
URL:		http://search.cpan.org/dist/Text-Haml/
BuildRequires:	perl-Module-Build >= 0.38
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-Section-Simple
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Haml implements Haml specification:
<http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html>.

Text::Haml passes specification tests written by Norman Clarke
<http://github.com/norman/haml-spec> and supports only cross-language
Haml features. Do not expect Ruby specific things to work.

%description -l pl.UTF-8
Text::Haml implementuje specyfikację Haml:
<http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html>.

Text::Haml przechodzi testy specifikacji napisane przez Normana
Clarke'a (<http://github.com/norman/haml-spec>) i obsługuje tylko
cechy Hamla wspólne dla wielu języków - nie należy się spodziewać, że
elementy specyficzne dla języka Ruby będą działać.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
%{perl_vendorlib}/Text/Haml.pm
%{_mandir}/man3/Text::Haml.3pm*
