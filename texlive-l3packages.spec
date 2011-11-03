# revision 24257
# category Package
# catalog-ctan /macros/latex/contrib/l3packages
# catalog-date 2011-10-10 01:01:54 +0200
# catalog-license lppl1.3
# catalog-version SVN 2900
Name:		texlive-l3packages
Version:	0.2900
Release:	1
Summary:	High-level LaTeX3 concepts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3packages
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3packages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3packages.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3packages.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bundle holds prototype implementations of concepts for a
LaTeX designer interface, to be used with the experimental
LaTeX kernel as programming tools and kernel support. Packages
provided in this release are: - l3keys2e, which makes the
facilities of the kernel module l3keys available for use by
LaTeX 2e packages; - xfrac, which provides flexible split-level
fractions; - xparse, which provides a high-level interface for
declaring document commands; and - xtemplate, which provides a
means of defining generic functions using a key-value syntax.
All the files of the bundle are also available in the
Subversion (SVN) repository of the LaTeX3 Project. The bundle
on CTAN is based on a snapshot of the SVN repository on 2011-
10-09.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/l3packages/l3keys2e/l3keys2e.sty
%{_texmfdistdir}/tex/latex/l3packages/xfrac/xfrac.sty
%{_texmfdistdir}/tex/latex/l3packages/xparse/xparse.sty
%{_texmfdistdir}/tex/latex/l3packages/xtemplate/xtemplate.sty
%doc %{_texmfdistdir}/doc/latex/l3packages/README
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
