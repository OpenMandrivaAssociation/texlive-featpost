Name:		texlive-featpost
Version:	0.8.8
Release:	2
Summary:	MetaPost macros for 3D
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/featpost
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/featpost.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/featpost.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These macros allow the production of three-dimensional schemes
containing: angles, circles, cylinders, cones and spheres,
among other things.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/featpost
%doc %{_texmfdistdir}/doc/metapost/featpost

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
