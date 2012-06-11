# revision 26049
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/featpost
# catalog-date 2012-04-16 18:59:36 +0200
# catalog-license gpl
# catalog-version 0.8.6
Name:		texlive-featpost
Version:	0.8.6
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
%{_texmfdistdir}/metapost/featpost/featpost.mp
%{_texmfdistdir}/metapost/featpost/featpost3Dplus2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/COMPILE.sh
%doc %{_texmfdistdir}/doc/metapost/featpost/README
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/Exemplifier.ps.bz2
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostbeamer.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostdocsource.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/featpostmanual.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/lastfiguretest.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/lastfiguretest.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropaganda.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropaganda.tex
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/3.eps
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/3.jpeg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/3.pgm
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/CompanionsCollection.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/Diagram1.dia
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/Diagram1.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/KnuthCollection.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/dia.png
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/fekslatexmp.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/intersection2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/metapostpropaganda.png
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/minimal-1.mps
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/minimal-1.pdf
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/minimal.jpeg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/minimal.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/minimal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/minimal.png
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/pifpaf.jpeg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/pifpafphoto.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/pifpafpropaganda.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/recursives.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/sriyantrafinal-1.svg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/sriyantrafinal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/todo.jpg
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/workflow-from-mpman-charts.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/doc/metapostpropagandafiles/xfig.png
%doc %{_texmfdistdir}/doc/metapost/featpost/example/38.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/CAT.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/DebianSwirlsmallEdited.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/EBcrossed.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/LED.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/acmaglev.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/acoplanv.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ahoraesglobal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/aledlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/allfigs.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/allgreatideas.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/anglinerigorouscircle.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/antimattermeteor.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/avalzero.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/badshreeyantra.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/balllauncher.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bananadimmer.log
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bananadimmer.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/brownellips.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bstr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/bughunt.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/buildcyclebug.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/canschemes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cap29res.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/caratk3edit.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cartaxes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/casadopessoal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cellevolve.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cinemwork.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/closingbox.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cmykropes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/conegetready.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/conicurv.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/convergingspirals.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/crossingline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cruztuga.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicfacecentered.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicfigures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicstructurefcc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cubicstructures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/cylimple.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/daliasensor.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/decorstatement.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/defaultcmr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/deperspective.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/derivondatriang.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/diameters.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/directfonts.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/doitnow.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/downloadicon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/durgayantra.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/eemcsblabla.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/electricpotential.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/electrospiral.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ellipticextrusionpress.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ellipticprism.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ellipticproperties.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/elliptictable.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ellipticthing.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/embroncordada.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/emptylines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/equilatrianglelines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/esteveslogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/experimental.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/experimental2Dsetup.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/f1aula03.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/f1aula05.mp
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
%doc %{_texmfdistdir}/doc/metapost/featpost/example/fis3prex7.mp
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
%doc %{_texmfdistdir}/doc/metapost/featpost/example/gnupost.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/gnupost3Dlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/goldenellipse.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/graphene.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/graphexample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/graphs.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/halfcirclesfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hap.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/heatfromroom.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hermitespliknot.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hexacylon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hexagonaltrimesh.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hiddenlinegraph.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hiddensurface.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/hiddensurfaces.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/iamsorrykarl.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/inductionbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/integerbars.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/integratorfigures.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/jd44.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/joinedemptylines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/kindofcube.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/kindofcuber.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/kopptrammel.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/labelconstruct.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/labelinspace.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/lamarquejaune.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/lasermachine.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/latexboxes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/lawofcosines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/lcurvature.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ledlogo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/loglogpaper.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/logofontest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/magneticflux.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mainmemtest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/manjusha.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/matricskoc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mce-lng.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/metalcharge.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/micromu.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/milimetricpaper.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mpfields.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mptoolcone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/muslimpattern.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mypatent.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mypatentpieces.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/mysquaresectionbar.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/naoestacionar.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nembends.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nembiaxi.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemdirector.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemquira.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemquirapitch.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemsaddl.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nemuniax.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/newcommunism.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/newexperimental.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nosimples.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nosuspension.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nsmetica.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nulldefectanglexample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/nurbstobeziern.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/onebigword.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/optest.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/optica.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/par3Dplotexamples.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/parafuso.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/parafusoprojxy.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/pathernon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/pathofstraightline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/perspec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/photorefer.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/photoreverse.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/pifpaf.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/pixelgrid.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/plaintangency.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planintersection.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/planpht.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/polyhedr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/positivecharge.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/potenciadecicloeliptico.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/probtodooterr.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/profaux.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/project.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/qap.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/quartertorus.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/redplanet.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/reeditedgoodquestionmark.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/resistcircuit.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/revolipsoid.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/revolvers.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorcubo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorouscircle.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorouscone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorousdiscSD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorousdiscoptions.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rigorousfearpath.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rmnbob.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/roadincline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rodarolaremplaninc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ropepatterns.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rotatnlc.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rothexagrid.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/rungekuttasecond.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sal.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sap.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/saturn.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sfearschem.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sharpraytrace.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/signalvertexSD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/simplecar.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/simplecarparam.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/simplexperiment.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/sincityredesigned.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/slingshot.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/smC.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/some2Dvecs.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/spatialhalfsfear.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/spherample.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/splineperspective.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/spltwiben.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/squareanglines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/stageforthree.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/statement.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/statethreelines.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/steamcamera.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/strength1defect.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/symbol.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tangency2D.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tangencypoint.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tdarrow.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/telemira.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tete.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tetrapodes.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/theHURD.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/thearchicon.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/thethreekindsofperspec.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/thunderproblem.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tiposdetrans.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tiposdetransb.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/tiposdetranst.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/torus.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/trajectoryline.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/trianglecenterofmass.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/triangulartrimesh.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/trig.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/trigonometry.mp
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
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twoplustwo.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/twoupcones.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ubhtransients.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ultraeye.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/ultraimprovertex.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/unperfection.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/unperfectionremoved.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/vanallenbelt.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/verygoodcone.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/wwfpmp.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/xcmplaca2buraquads.mp
%doc %{_texmfdistdir}/doc/metapost/featpost/example/xraycamera.mp

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
