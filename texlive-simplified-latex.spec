# revision 20620
# category Package
# catalog-ctan /info/simplified-latex
# catalog-date 2010-11-29 22:48:23 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-simplified-latex
Version:	20101129
Release:	10
Summary:	A Simplified Introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/simplified-latex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
An accessible introduction for the beginner.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/simplified-latex/README
%doc %{_texmfdistdir}/doc/latex/simplified-latex/simplified-intro.pdf
%doc %{_texmfdistdir}/doc/latex/simplified-latex/source.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101129-2
+ Revision: 756029
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101129-1
+ Revision: 719539
- texlive-simplified-latex
- texlive-simplified-latex
- texlive-simplified-latex
- texlive-simplified-latex

