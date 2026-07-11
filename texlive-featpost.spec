%global tl_name featpost
%global tl_revision 35346

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.8
Release:	%{tl_revision}.1
Summary:	MetaPost macros for 3D
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/featpost
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/featpost.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/featpost.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These macros allow the production of three-dimensional schemes
containing: angles, circles, cylinders, cones and spheres, among other
things.

