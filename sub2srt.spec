
%define name	sub2srt
%define version	0.5.3
%define rel	3

Summary:	Convert subtitles from .sub to subviewer .srt format
Name:		%name
Version:	%version
Release:	%mkrel %rel
URL:		http://www.robelix.com/sub2srt/
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


