# revision 34268
# category Package
# catalog-ctan /macros/latex/contrib/l3packages
# catalog-date 2014-06-10 18:54:52 +0200
# catalog-license lppl1.3
# catalog-version SVN 5015
Name:		texlive-l3packages
Epoch:		1
Version:	SVN5015
Release:	3
Summary:	High-level LaTeX3 concepts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3packages
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3packages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3packages.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3packages.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle holds prototype implementations of concepts for a
LaTeX designer interface, to be used with the experimental
LaTeX kernel as programming tools and kernel support. Packages
provided in this release are: l3keys2e, which makes the
facilities of the kernel module l3keys available for use by
LaTeX 2e packages; xfrac, which provides flexible split-level
fractions; xparse, which provides a high-level interface for
declaring document commands; and xtemplate, which provides a
means of defining generic functions using a key-value syntax.
All the files of the bundle are also available in the
Subversion (SVN) repository of the LaTeX3 Project. The bundle
on CTAN is based on a snapshot of the SVN repository on; it
should be used with copies of the l3kernel at SVN version 2544
or later.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/l3packages/l3keys2e/l3keys2e.sty
%{_texmfdistdir}/tex/latex/l3packages/xfrac/xfrac.sty
%{_texmfdistdir}/tex/latex/l3packages/xparse/xparse.sty
%{_texmfdistdir}/tex/latex/l3packages/xtemplate/xtemplate.sty
%doc %{_texmfdistdir}/doc/latex/l3packages/README
%doc %{_texmfdistdir}/doc/latex/l3packages/l3keys2e/l3keys2e-demo.tex
%doc %{_texmfdistdir}/doc/latex/l3packages/l3keys2e/l3keys2e.pdf
%doc %{_texmfdistdir}/doc/latex/l3packages/xfrac/xfrac.pdf
%doc %{_texmfdistdir}/doc/latex/l3packages/xparse/xparse.pdf
%doc %{_texmfdistdir}/doc/latex/l3packages/xtemplate/xtemplate.pdf
#- source
%doc %{_texmfdistdir}/source/latex/l3packages/l3keys2e/l3keys2e.dtx
%doc %{_texmfdistdir}/source/latex/l3packages/l3keys2e/l3keys2e.ins
%doc %{_texmfdistdir}/source/latex/l3packages/xfrac/xfrac.dtx
%doc %{_texmfdistdir}/source/latex/l3packages/xfrac/xfrac.ins
%doc %{_texmfdistdir}/source/latex/l3packages/xparse/xparse.dtx
%doc %{_texmfdistdir}/source/latex/l3packages/xparse/xparse.ins
%doc %{_texmfdistdir}/source/latex/l3packages/xtemplate/xtemplate.dtx
%doc %{_texmfdistdir}/source/latex/l3packages/xtemplate/xtemplate.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
