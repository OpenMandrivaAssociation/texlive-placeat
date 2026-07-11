%global tl_name placeat
%global tl_revision 45145

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1d1
Release:	%{tl_revision}.1
Summary:	Absolute content positioning
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/placeat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/placeat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/placeat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/placeat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands so that the user of LuaLaTeX may position
arbitrary content at any position specified by absolute coordinates on
the page. The package draws a grid on each page of the document, to aid
positioning (the grid may be disabled, for 'final copy' using the
command \placeatsetup).

