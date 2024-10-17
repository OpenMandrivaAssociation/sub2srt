
%define name	sub2srt
%define version	0.5.3
%define rel	3

Summary:	Convert subtitles from .sub to subviewer .srt format
Name:		%name
Version:	%version
Release:	%mkrel %rel
URL:		https://www.robelix.com/sub2srt/
Group:		Video
Source0:	http://www.robelix.com/sub2srt/download/%name-%version.tar.bz2
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
sub2srt is a simple tool to convert 2 common subtitle formats (microdvd
and subrip - both are known as ".sub") to subviewer ".srt" format.

%prep
%setup -q

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%{name}




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5.3-3mdv2010.0
+ Revision: 434140
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.5.3-2mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 05 2007 Anssi Hannula <anssi@mandriva.org> 0.5.3-2mdv2007.0
+ Revision: 104554
- rebuild
- Import sub2srt

* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 0.5.3-1mdk
- initial Mandriva package

