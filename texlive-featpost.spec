Name:		texlive-featpost
Version:	0.6.7
Release:	1
Summary:	MetaPost macros for 3D
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/featpost
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/featpost.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/featpost.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
These macros allow the production of three-dimensional schemes
containing: angles, circles, cylinders, cones and spheres,
among other things.

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
%{_texmfdistdir}/metapost/featpost/featpost.mp
%{_texmfdistdir}/metapost/featpost/featpost3Dplus2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/README.ctan
%doc %{_texmfdistdir}/doc/metapost/featpost/README.featpost
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/dosome.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/eps2j.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/fpost
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/insertinputcommands.sed
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/insertinputcommands.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/laproof
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/lbproof
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/lcproof
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/makelogo.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/maketugboatart.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/nontextualpng.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/procedurenames.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/remfi.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/removeinputcommand.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/replacetext.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/bashscript/simpleviewer.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/doclicense.txt
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featexamples.html
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpost.1.gz
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpost.sgml
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/tug2004.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bugtrack/bughunt.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bugtrack/gstr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/highmemory/hiddenlinegraph.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/highmemory/mainmemtest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/highmemory/par3Dplotexamples.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/borderframetest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/conegetready.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/doitnow.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/electricpotential.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/emptylines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/experimental.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/fieldlines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/fis3prey.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/frustum.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/geom_casq.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/geom_freder.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/graphexample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/lcurvature.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/mptoolcone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/nembends.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/nemdirector.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/nemquira.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/nemquirapitch.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/nemuniax.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/pathernon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/planpht.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/rigorcubo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/rmnbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/sal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/sfearschem.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/signalvertexSD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/spherample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/squareanglines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/troncoconedef.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/twistnlc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/twistroundbiax.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/twocyclestogether.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/repeated/twoupcones.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/anglinerigorouscircle.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/cartaxes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/conicurv.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/cubicfacecentered.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/cubicfigures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/cylimple.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/downloadicon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/eemcsblabla.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/embroncordada.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/fakehole.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/featpostlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/ffcbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/fieldlinesnorma.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/fis1prex.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/fis3prex.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/geombasic.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/geomfiguei.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/geommine.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/globe.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/halfcirclesfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/hexagonaltrimesh.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/hiddensurface.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/hiddensurfaces.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/inductionbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/joinedemptylines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/kindofcube.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/labelconstruct.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/labelinspace.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/magneticflux.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/nembiaxi.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/nemsaddl.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/nsmetica.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/parafuso.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/pathofstraightline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/photoreverse.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/polyhedr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/positivecharge.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/resistcircuit.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/rigorouscircle.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/rigorouscone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/rigorousdiscSD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/rigorousdiscoptions.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/rigorousfearpath.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/rotatnlc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/saturn.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/sharpraytrace.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/simplecar.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/simplecarparam.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/spatialhalfsfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/spltwiben.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/stageforthree.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/tangencypoint.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/tdarrow.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/thearchicon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/thethreekindsofperspec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/torus.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/trajectoryline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/triangulartrimesh.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/tropicalglobe.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/tshirtfig.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/tuftescatter.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/twistflat.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/twoholes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/unperfection.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/unperfectionremoved.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/vanallenbelt.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/verygoodcone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/standard/xraycamera.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/cone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/ellipticprism.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/intersection2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/kindofcube.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/newexperimental.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/perspec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/planintersection.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/revolvers.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tug04/tangency2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/galrey/galrey.rc
%doc %{_texmfdistdir}/doc/metapost/featpost/galrey/galrey.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/galrey/galrey.tpl
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/cbxSmall.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/hiddenlinegraph1.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/mymetapostbackground.jpeg
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/mymetapostclearback.jpeg
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/par3Dplotexamples1.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/par3Dplotexamples2.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/jpeg/planpau2.jpeg
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/linuxdoc-sgml.sty
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/logofeatpost.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/ltugboat.cls
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/macroMan.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/mflogohack.sty
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/null.sty
%doc %{_texmfdistdir}/doc/metapost/featpost/latex/qwertz.sty
%doc %{_texmfdistdir}/doc/metapost/featpost/macro/README.macro
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/cylimple.1.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/globe.1.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/rigorouscone.1.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/rigorousfearpath.1.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/rotatnlc.1.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/stageforthree.2.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/torus.5.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/torus.6.png
%doc %{_texmfdistdir}/doc/metapost/featpost/nontextualpng/triangulartrimesh.1.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/border140.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/borderframetest.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/composite.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/downloadicon.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/experfilminifram.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/featpost2.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/inifram.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/lcdistortsallinifram.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/metapostlace.png
%doc %{_texmfdistdir}/doc/metapost/featpost/png/myicon.png
%doc %{_texmfdistdir}/doc/metapost/featpost/typesetinspace/README.mpy
%doc %{_texmfdistdir}/doc/metapost/featpost/typesetinspace/example.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/typesetinspace/exampleminimal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/typesetinspace/makempy.pl
%doc %{_texmfdistdir}/doc/metapost/featpost/typesetinspace/mp-grph.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/typesetinspace/mp-tool.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/xcmd/README.xcmd
%doc %{_texmfdistdir}/doc/metapost/featpost/xcmd/xmpost

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
