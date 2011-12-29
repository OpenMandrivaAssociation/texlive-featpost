# revision 24738
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/featpost
# catalog-date 2011-11-24 18:09:37 +0100
# catalog-license gpl
# catalog-version 0.8.2
Name:		texlive-featpost
Version:	0.8.2
Release:	1
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
%{_texmfdistdir}/metapost/featpost/featpost3Dplus2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/COMPILE.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/acmaglev.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/ahoraesglobal.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/aledlogo.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/aledlogo.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/anglinerigorouscircle.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/antimattermeteor.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/bananadimmer.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/borderframetest.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/brownellips.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/bstr.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/bughunt.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/bughunt.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cartaxes.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cartaxes.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/closingbox.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cmykropes.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cone.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/conegetready.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/conicurv.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/crossingline.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/crossingline.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/crossingline.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicfacecentered.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicfigures.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicfigures.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicfigures.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructurefcc.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructures.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructures.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructures.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructures.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructures.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cubicstructures.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/cylimple.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/daliasensor.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/deperspective.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/deperspective.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/deperspective.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/deperspective.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/doitnow.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/downloadicon.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/eemcsblabla.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/electricpotential.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/electricpotential.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/electricpotential.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/electricpotential.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/ellipticprism.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/embroncordada.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/emptylines.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/experimental.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fakehole.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fakehole.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fallinthewind.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/featpostlogo.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/ffcbob.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fieldlines.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fieldlinesnorma.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fieldlinesnorma.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fieldlinesnormapaper.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fieldlinesnormapaper.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fieldlinesnormapaperwork.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis1prex.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis1prex.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis1prex.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.8
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prex.9
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prey.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prey.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/fis3prey.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/frustum.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/galvanometro-inducao.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/gausslawframe.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/geombasic.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/geomcasq.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/geometricaverage.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/geomfiguei.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/geomfreder.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/geommine.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/globe.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/gnupost3Dlogo.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/graphene.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/graphexample.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/halfcirclesfear.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/hermitespliknot.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/hexagonaltrimesh.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/hiddenlinegraph.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/hiddensurface.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/hiddensurfaces.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/inductionbob.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/integerbars.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/integratorfigures.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/integratorfigures.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/intersection2D.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/joinedemptylines.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/kindofcube.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/kindofcube.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/kindofcuber.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/labelconstruct.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/labelinspace.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/lasermachine.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/lcurvature.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/lcurvature.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/magneticflux.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/magneticflux.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mainmemtest.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/matricskoc.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/metalcharge.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mptoolcone.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mypatent.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mypatent.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mypatent.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mypatent.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mypatentpieces.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/mysquaresectionbar.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nembends.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nembiaxi.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nemdirector.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nemquira.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nemquirapitch.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nemsaddl.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nemuniax.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/newexperimental.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nsmetica.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/nurbstobeziern.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/optica.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/par3Dplotexamples.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/par3Dplotexamples.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/parafuso.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/parafuso.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/parafuso.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/parafuso.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/parafusoprojxy.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/pathernon.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/pathofstraightline.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/perspec.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/photorefer.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/photorefer.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/photoreverse.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planescava.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planintersection.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpau.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpau.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpht.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planphtnonrec.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln0.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln0.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln0.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln0.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln0.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.8
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln1.9
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.8
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln2.9
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln3.9
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.7
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.8
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln4.9
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/planpln5.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/polyhedr.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/polyhedr.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/polyhedr.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/positivecharge.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/quartertorus.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/redplanet.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/resistcircuit.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolipsoid.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolipsoid.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolvers.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolvers.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolvers.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolvers.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolvers.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/revolvers.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rigorcubo.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rigorouscircle.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rigorouscone.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rigorousdiscSD.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rigorousdiscoptions.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rigorousfearpath.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rmnbob.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rotatnlc.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rungekuttasecond.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/rungekuttasecond.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sal.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sal.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/saturn.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sfearschem.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sharpraytrace.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sharpraytrace.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sharpraytrace.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/sharpraytrace.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/signalvertexSD.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/simplecar.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/simplecarparam.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/simplexperiment.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/slingshot.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/smC.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/spatialhalfsfear.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/spherample.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/splineperspective.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/splineperspective.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/splineperspective.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/splineperspective.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/splineperspective.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/spltwiben.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/squareanglines.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/stageforthree.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/stageforthree.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/stageforthree.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/steamcamera.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tangency2D.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tangencypoint.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tdarrow.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tetrapodes.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tetrapodes.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tetrapodes.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/thearchicon.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/thethreekindsofperspec.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/thethreekindsofperspec.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/thethreekindsofperspec.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/torus.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/torus.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/torus.3
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/torus.4
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/torus.5
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/torus.6
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/trajectoryline.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/trajectoryline.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/triangulartrimesh.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/troncoconedef.0
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tropicalglobe.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/troysfear.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tshirtfig.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/tuftescatter.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/twistflat.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/twistnlc.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/twistroundbiax.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/twocyclestogether.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/twoholes.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/twoupcones.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/unperfection.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/unperfectionremoved.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/vanallenbelt.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/vanallenbelt.2
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/verygoodcone.1
%doc %{_texmfdistdir}/doc/metapost/featpost/allps/xraycamera.1
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/FeatPostExemplifier.ps.bz2
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.aux
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.log
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.nav
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.out
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.snm
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.toc
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostdocsource.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.aux
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.log
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.nav
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.out
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.snm
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.toc
%doc %{_texmfdistdir}/doc/metapost/featpost/example/acmaglev.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ahoraesglobal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/aledlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/anglinerigorouscircle.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/antimattermeteor.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bananadimmer.log
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bananadimmer.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bananadimmer.mp~
%doc %{_texmfdistdir}/doc/metapost/featpost/example/borderframetest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/brownellips.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bstr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bughunt.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cartaxes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/closingbox.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cmykropes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/conegetready.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/conicurv.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/crossingline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicfacecentered.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicfigures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicstructurefcc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicstructures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cylimple.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/daliasensor.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/deperspective.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/doitnow.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/downloadicon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/eemcsblabla.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/electricpotential.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ellipticprism.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/embroncordada.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/emptylines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/experimental.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fakehole.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fallinthewind.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/featpostlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ffcbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fieldlines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fieldlinesnorma.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fieldlinesnormapaper.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fieldlinesnormapaperwork.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fis1prex.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fis3prex.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fis3prey.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/frustum.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/galvanometro-inducao.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/gausslawframe.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/geombasic.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/geomcasq.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/geometricaverage.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/geomfiguei.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/geomfreder.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/geommine.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/globe.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/gnupost3Dlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/graphene.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/graphexample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/halfcirclesfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hermitespliknot.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hexagonaltrimesh.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hiddenlinegraph.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hiddensurface.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hiddensurfaces.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/inductionbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/integerbars.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/integratorfigures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/intersection2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/joinedemptylines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/kindofcube.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/kindofcuber.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/labelconstruct.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/labelinspace.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/lasermachine.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/lcurvature.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/magneticflux.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mainmemtest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/matricskoc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/metalcharge.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mptoolcone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mpxerr.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mypatent.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mypatentpieces.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mysquaresectionbar.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nembends.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nembiaxi.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemdirector.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemquira.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemquirapitch.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemsaddl.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemuniax.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/newexperimental.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nsmetica.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nurbstobeziern.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/optica.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/par3Dplotexamples.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/parafuso.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/parafusoprojxy.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/pathernon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/pathofstraightline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/perspec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/photorefer.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/photoreverse.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planescava.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planintersection.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpau.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpht.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planphtnonrec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpln0.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpln1.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpln2.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpln3.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpln4.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpln5.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/polyhedr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/positivecharge.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/quartertorus.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/redplanet.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/resistcircuit.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/revolipsoid.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/revolvers.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/revolvers.mp~
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorcubo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorouscircle.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorouscone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorousdiscSD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorousdiscoptions.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorousfearpath.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rmnbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rotatnlc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rungekuttasecond.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/saturn.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sfearschem.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sharpraytrace.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/signalvertexSD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/simplecar.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/simplecarparam.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/simplexperiment.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/slingshot.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/smC.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/spatialhalfsfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/spherample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/splineperspective.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/spltwiben.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/squareanglines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/stageforthree.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/steamcamera.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tangency2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tangencypoint.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tdarrow.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tetrapodes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/thearchicon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/thethreekindsofperspec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/torus.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/trajectoryline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/triangulartrimesh.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/troncoconedef.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tropicalglobe.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/troysfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tshirtfig.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tuftescatter.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twistflat.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twistnlc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twistroundbiax.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twocyclestogether.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twoholes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twoupcones.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/unperfection.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/unperfectionremoved.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/vanallenbelt.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/verygoodcone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/xraycamera.mp

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
