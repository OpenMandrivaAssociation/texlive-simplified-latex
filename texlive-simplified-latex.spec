# revision 20620
# category Package
# catalog-ctan /info/simplified-latex
# catalog-date 2010-11-29 22:48:23 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-simplified-latex
Version:	20101129
Release:	1
Summary:	A Simplified Introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/simplified-latex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An accessible introduction for the beginner.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/simplified-latex/README
%doc %{_texmfdistdir}/doc/latex/simplified-latex/simplified-intro.pdf
%doc %{_texmfdistdir}/doc/latex/simplified-latex/source.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
