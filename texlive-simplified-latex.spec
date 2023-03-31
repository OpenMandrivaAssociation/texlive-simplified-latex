Name:		texlive-simplified-latex
Version:	20620
Release:	2
Summary:	A Simplified Introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/simplified-latex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simplified-latex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
