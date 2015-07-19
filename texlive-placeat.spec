# revision 33526
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-placeat
Version:	20140620
Release:	4
Summary:	TeXLive placeat package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive placeat package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/placeat/placeat.lua
%{_texmfdistdir}/tex/lualatex/placeat/placeat.sty
%doc %{_texmfdistdir}/doc/lualatex/placeat/README
%doc %{_texmfdistdir}/doc/lualatex/placeat/placeat.pdf
%doc %{_texmfdistdir}/doc/lualatex/placeat/placeat.tex
#- source
%doc %{_texmfdistdir}/source/lualatex/placeat/placeat.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
