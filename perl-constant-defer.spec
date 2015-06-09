#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	constant
%define		pnam	defer
%include	/usr/lib/rpm/macros.perl
Summary:	constant::defer -- constant subs with deferred value calculation
Name:		perl-constant-defer
Version:	6
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/constant/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6af9912fa420340e9e171ac81f450492
URL:		http://search.cpan.org/dist/constant-defer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
constant::defer creates a subroutine which on the first call runs given
code to calculate its value, and on any subsequent calls just returns that
value, like a constant.  The value code is discarded once run, allowing it
to be garbage collected.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/constant
%{perl_vendorlib}/constant/defer.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
