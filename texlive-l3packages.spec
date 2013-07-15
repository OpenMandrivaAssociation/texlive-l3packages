# revision 27899
# category Package
# catalog-ctan /macros/latex/contrib/l3packages
# catalog-date 2012-10-03 16:32:18 +0200
# catalog-license lppl1.3
# catalog-version SVN 4249
Name:		texlive-l3packages
Epoch:		1
Version:	SVN4249
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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
on CTAN is based on a snapshot of the SVN repository on 2012-
09-30.

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


%changelog
* Tue Oct 30 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN4249-1
+ Revision: 821204
- Update to latest release.

* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3990-1
+ Revision: 812335
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3570-1
+ Revision: 804864
- Update to latest release.

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:SVN3471-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3471-1
+ Revision: 783039
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3341-1
+ Revision: 779592
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:SVN3331-1
+ Revision: 772115
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3209-1
+ Revision: 770207
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3109-1
+ Revision: 762637
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3036-2
+ Revision: 753071
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3036-1
+ Revision: 743257
- texlive-l3packages

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2966-1
+ Revision: 739799
- texlive-l3packages

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2900-1
+ Revision: 718798
- texlive-l3packages
- texlive-l3packages
- texlive-l3packages
- texlive-l3packages

