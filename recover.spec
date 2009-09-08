%define name recover
%define version 1.3c
%define release %mkrel 7
%define prefix %{_prefix}
%define summary Utility for recovering a lost file

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	%{summary}
License:	GPL
Group:		File tools
Url:		http://recover.sourceforge.net/linux/recover/
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
requires:	e2fsprogs

%description
Recover is a utility which automates some steps as described in the 
Ext2fs-Undeletion howto. 
(http://pobox.com/~aaronc/tech/e2-undel/howto.txt) in order to recover a 
lost file. Our goal is to make it as easy as possible to undelete a 
file (ie. a GTK and/or Qt interface). Right now, there is only a console 
version.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch

%build
%make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1*


