%global tl_name simplified-latex
%global tl_revision 20620

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Simplified Introduction to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/simplified-latex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An accessible introduction for the beginner.

