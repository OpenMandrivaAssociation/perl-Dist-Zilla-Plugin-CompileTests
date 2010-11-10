%define upstream_name    Dist-Zilla-Plugin-CompileTests
%define upstream_version 1.103030

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Common tests to check syntax of your modules
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More) >= 0.940.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an extension of the Dist::Zilla::Plugin::InlineFiles manpage,
providing the following files:

* t/00-compile.t - a standard test to check syntax of bundled modules

This test will find all modules and scripts in your dist, and try to
compile them one by one. This means it's a bit slower than loading them all
at once, but it will catch more errors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
