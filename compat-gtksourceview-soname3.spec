#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-gtksourceview-soname3
Version  : 3.24.7
Release  : 37
URL      : https://download.gnome.org/sources/gtksourceview/3.24/gtksourceview-3.24.7.tar.xz
Source0  : https://download.gnome.org/sources/gtksourceview/3.24/gtksourceview-3.24.7.tar.xz
Summary  : Source code editing widget
Group    : Development/Tools
License  : LGPL-2.1
Requires: compat-gtksourceview-soname3-data = %{version}-%{release}
Requires: compat-gtksourceview-soname3-lib = %{version}-%{release}
Requires: compat-gtksourceview-soname3-license = %{version}-%{release}
Requires: compat-gtksourceview-soname3-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-golang
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : vala
BuildRequires : vala-bin
BuildRequires : vala-dev
BuildRequires : valgrind
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: cve-2017-14108.patch

%description
General Information
===================
This is version 3.24.7 of GtkSourceView.

%package data
Summary: data components for the compat-gtksourceview-soname3 package.
Group: Data

%description data
data components for the compat-gtksourceview-soname3 package.


%package dev
Summary: dev components for the compat-gtksourceview-soname3 package.
Group: Development
Requires: compat-gtksourceview-soname3-lib = %{version}-%{release}
Requires: compat-gtksourceview-soname3-data = %{version}-%{release}
Provides: compat-gtksourceview-soname3-devel = %{version}-%{release}
Requires: compat-gtksourceview-soname3 = %{version}-%{release}

%description dev
dev components for the compat-gtksourceview-soname3 package.


%package doc
Summary: doc components for the compat-gtksourceview-soname3 package.
Group: Documentation

%description doc
doc components for the compat-gtksourceview-soname3 package.


%package lib
Summary: lib components for the compat-gtksourceview-soname3 package.
Group: Libraries
Requires: compat-gtksourceview-soname3-data = %{version}-%{release}
Requires: compat-gtksourceview-soname3-license = %{version}-%{release}

%description lib
lib components for the compat-gtksourceview-soname3 package.


%package license
Summary: license components for the compat-gtksourceview-soname3 package.
Group: Default

%description license
license components for the compat-gtksourceview-soname3 package.


%package locales
Summary: locales components for the compat-gtksourceview-soname3 package.
Group: Default

%description locales
locales components for the compat-gtksourceview-soname3 package.


%prep
%setup -q -n gtksourceview-3.24.7
cd %{_builddir}/gtksourceview-3.24.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586223820
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1586223820
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-gtksourceview-soname3
cp %{_builddir}/gtksourceview-3.24.7/COPYING %{buildroot}/usr/share/package-licenses/compat-gtksourceview-soname3/caeb68c46fa36651acf592771d09de7937926bb3
%make_install
%find_lang gtksourceview-3.0

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GtkSource-3.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gtksourceview-3.0/language-specs/R.lang
/usr/share/gtksourceview-3.0/language-specs/abnf.lang
/usr/share/gtksourceview-3.0/language-specs/actionscript.lang
/usr/share/gtksourceview-3.0/language-specs/ada.lang
/usr/share/gtksourceview-3.0/language-specs/ansforth94.lang
/usr/share/gtksourceview-3.0/language-specs/asp.lang
/usr/share/gtksourceview-3.0/language-specs/automake.lang
/usr/share/gtksourceview-3.0/language-specs/awk.lang
/usr/share/gtksourceview-3.0/language-specs/bennugd.lang
/usr/share/gtksourceview-3.0/language-specs/bibtex.lang
/usr/share/gtksourceview-3.0/language-specs/bluespec.lang
/usr/share/gtksourceview-3.0/language-specs/boo.lang
/usr/share/gtksourceview-3.0/language-specs/c.lang
/usr/share/gtksourceview-3.0/language-specs/cg.lang
/usr/share/gtksourceview-3.0/language-specs/changelog.lang
/usr/share/gtksourceview-3.0/language-specs/chdr.lang
/usr/share/gtksourceview-3.0/language-specs/cmake.lang
/usr/share/gtksourceview-3.0/language-specs/cobol.lang
/usr/share/gtksourceview-3.0/language-specs/cpp.lang
/usr/share/gtksourceview-3.0/language-specs/cpphdr.lang
/usr/share/gtksourceview-3.0/language-specs/csharp.lang
/usr/share/gtksourceview-3.0/language-specs/css.lang
/usr/share/gtksourceview-3.0/language-specs/csv.lang
/usr/share/gtksourceview-3.0/language-specs/cuda.lang
/usr/share/gtksourceview-3.0/language-specs/d.lang
/usr/share/gtksourceview-3.0/language-specs/def.lang
/usr/share/gtksourceview-3.0/language-specs/desktop.lang
/usr/share/gtksourceview-3.0/language-specs/diff.lang
/usr/share/gtksourceview-3.0/language-specs/docbook.lang
/usr/share/gtksourceview-3.0/language-specs/dosbatch.lang
/usr/share/gtksourceview-3.0/language-specs/dot.lang
/usr/share/gtksourceview-3.0/language-specs/dpatch.lang
/usr/share/gtksourceview-3.0/language-specs/dtd.lang
/usr/share/gtksourceview-3.0/language-specs/dtl.lang
/usr/share/gtksourceview-3.0/language-specs/eiffel.lang
/usr/share/gtksourceview-3.0/language-specs/erlang.lang
/usr/share/gtksourceview-3.0/language-specs/fcl.lang
/usr/share/gtksourceview-3.0/language-specs/forth.lang
/usr/share/gtksourceview-3.0/language-specs/fortran.lang
/usr/share/gtksourceview-3.0/language-specs/fsharp.lang
/usr/share/gtksourceview-3.0/language-specs/gap.lang
/usr/share/gtksourceview-3.0/language-specs/gdb-log.lang
/usr/share/gtksourceview-3.0/language-specs/genie.lang
/usr/share/gtksourceview-3.0/language-specs/glsl.lang
/usr/share/gtksourceview-3.0/language-specs/go.lang
/usr/share/gtksourceview-3.0/language-specs/groovy.lang
/usr/share/gtksourceview-3.0/language-specs/gtk-doc.lang
/usr/share/gtksourceview-3.0/language-specs/gtkrc.lang
/usr/share/gtksourceview-3.0/language-specs/haddock.lang
/usr/share/gtksourceview-3.0/language-specs/haskell-literate.lang
/usr/share/gtksourceview-3.0/language-specs/haskell.lang
/usr/share/gtksourceview-3.0/language-specs/haxe.lang
/usr/share/gtksourceview-3.0/language-specs/html.lang
/usr/share/gtksourceview-3.0/language-specs/idl-exelis.lang
/usr/share/gtksourceview-3.0/language-specs/idl.lang
/usr/share/gtksourceview-3.0/language-specs/imagej.lang
/usr/share/gtksourceview-3.0/language-specs/ini.lang
/usr/share/gtksourceview-3.0/language-specs/j.lang
/usr/share/gtksourceview-3.0/language-specs/jade.lang
/usr/share/gtksourceview-3.0/language-specs/java.lang
/usr/share/gtksourceview-3.0/language-specs/javascript.lang
/usr/share/gtksourceview-3.0/language-specs/json.lang
/usr/share/gtksourceview-3.0/language-specs/julia.lang
/usr/share/gtksourceview-3.0/language-specs/kotlin.lang
/usr/share/gtksourceview-3.0/language-specs/language.dtd
/usr/share/gtksourceview-3.0/language-specs/language.rng
/usr/share/gtksourceview-3.0/language-specs/language2.rng
/usr/share/gtksourceview-3.0/language-specs/latex.lang
/usr/share/gtksourceview-3.0/language-specs/lex.lang
/usr/share/gtksourceview-3.0/language-specs/libtool.lang
/usr/share/gtksourceview-3.0/language-specs/llvm.lang
/usr/share/gtksourceview-3.0/language-specs/logcat.lang
/usr/share/gtksourceview-3.0/language-specs/lua.lang
/usr/share/gtksourceview-3.0/language-specs/m4.lang
/usr/share/gtksourceview-3.0/language-specs/makefile.lang
/usr/share/gtksourceview-3.0/language-specs/mallard.lang
/usr/share/gtksourceview-3.0/language-specs/markdown.lang
/usr/share/gtksourceview-3.0/language-specs/matlab.lang
/usr/share/gtksourceview-3.0/language-specs/maxima.lang
/usr/share/gtksourceview-3.0/language-specs/mediawiki.lang
/usr/share/gtksourceview-3.0/language-specs/meson.lang
/usr/share/gtksourceview-3.0/language-specs/modelica.lang
/usr/share/gtksourceview-3.0/language-specs/mxml.lang
/usr/share/gtksourceview-3.0/language-specs/nemerle.lang
/usr/share/gtksourceview-3.0/language-specs/netrexx.lang
/usr/share/gtksourceview-3.0/language-specs/nsis.lang
/usr/share/gtksourceview-3.0/language-specs/objc.lang
/usr/share/gtksourceview-3.0/language-specs/objj.lang
/usr/share/gtksourceview-3.0/language-specs/ocaml.lang
/usr/share/gtksourceview-3.0/language-specs/ocl.lang
/usr/share/gtksourceview-3.0/language-specs/octave.lang
/usr/share/gtksourceview-3.0/language-specs/ooc.lang
/usr/share/gtksourceview-3.0/language-specs/opal.lang
/usr/share/gtksourceview-3.0/language-specs/opencl.lang
/usr/share/gtksourceview-3.0/language-specs/pascal.lang
/usr/share/gtksourceview-3.0/language-specs/perl.lang
/usr/share/gtksourceview-3.0/language-specs/php.lang
/usr/share/gtksourceview-3.0/language-specs/pig.lang
/usr/share/gtksourceview-3.0/language-specs/pkgconfig.lang
/usr/share/gtksourceview-3.0/language-specs/po.lang
/usr/share/gtksourceview-3.0/language-specs/prolog.lang
/usr/share/gtksourceview-3.0/language-specs/protobuf.lang
/usr/share/gtksourceview-3.0/language-specs/puppet.lang
/usr/share/gtksourceview-3.0/language-specs/python.lang
/usr/share/gtksourceview-3.0/language-specs/python3.lang
/usr/share/gtksourceview-3.0/language-specs/rpmspec.lang
/usr/share/gtksourceview-3.0/language-specs/rst.lang
/usr/share/gtksourceview-3.0/language-specs/ruby.lang
/usr/share/gtksourceview-3.0/language-specs/rust.lang
/usr/share/gtksourceview-3.0/language-specs/scala.lang
/usr/share/gtksourceview-3.0/language-specs/scheme.lang
/usr/share/gtksourceview-3.0/language-specs/scilab.lang
/usr/share/gtksourceview-3.0/language-specs/sh.lang
/usr/share/gtksourceview-3.0/language-specs/sml.lang
/usr/share/gtksourceview-3.0/language-specs/sparql.lang
/usr/share/gtksourceview-3.0/language-specs/sql.lang
/usr/share/gtksourceview-3.0/language-specs/sweave.lang
/usr/share/gtksourceview-3.0/language-specs/swift.lang
/usr/share/gtksourceview-3.0/language-specs/systemverilog.lang
/usr/share/gtksourceview-3.0/language-specs/t2t.lang
/usr/share/gtksourceview-3.0/language-specs/tcl.lang
/usr/share/gtksourceview-3.0/language-specs/tera.lang
/usr/share/gtksourceview-3.0/language-specs/texinfo.lang
/usr/share/gtksourceview-3.0/language-specs/thrift.lang
/usr/share/gtksourceview-3.0/language-specs/toml.lang
/usr/share/gtksourceview-3.0/language-specs/vala.lang
/usr/share/gtksourceview-3.0/language-specs/vbnet.lang
/usr/share/gtksourceview-3.0/language-specs/verilog.lang
/usr/share/gtksourceview-3.0/language-specs/vhdl.lang
/usr/share/gtksourceview-3.0/language-specs/xml.lang
/usr/share/gtksourceview-3.0/language-specs/xslt.lang
/usr/share/gtksourceview-3.0/language-specs/yacc.lang
/usr/share/gtksourceview-3.0/language-specs/yaml.lang
/usr/share/gtksourceview-3.0/styles/classic.xml
/usr/share/gtksourceview-3.0/styles/cobalt.xml
/usr/share/gtksourceview-3.0/styles/kate.xml
/usr/share/gtksourceview-3.0/styles/oblivion.xml
/usr/share/gtksourceview-3.0/styles/solarized-dark.xml
/usr/share/gtksourceview-3.0/styles/solarized-light.xml
/usr/share/gtksourceview-3.0/styles/styles.rng
/usr/share/gtksourceview-3.0/styles/tango.xml
/usr/share/vala/vapi/gtksourceview-3.0.deps
/usr/share/vala/vapi/gtksourceview-3.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gtksourceview-3.0/gtksourceview/completion-providers/words/gtksourcecompletionwords.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksource.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceautocleanups.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcebuffer.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcecompletion.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcecompletioncontext.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcecompletioninfo.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcecompletionitem.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcecompletionproposal.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcecompletionprovider.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceencoding.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcefile.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcefileloader.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcefilesaver.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcegutter.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcegutterrenderer.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcegutterrendererpixbuf.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcegutterrenderertext.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcelanguage.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcelanguagemanager.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcemap.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcemark.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcemarkattributes.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceprintcompositor.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceregion.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcesearchcontext.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcesearchsettings.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcespacedrawer.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcestyle.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcestylescheme.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcestyleschemechooser.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcestyleschemechooserbutton.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcestyleschemechooserwidget.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcestyleschememanager.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcetag.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourcetypes.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceundomanager.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceutils.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceversion.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceview-enumtypes.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceview-typebuiltins.h
/usr/include/gtksourceview-3.0/gtksourceview/gtksourceview.h
/usr/lib64/libgtksourceview-3.0.so
/usr/lib64/pkgconfig/gtksourceview-3.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceBuffer.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletion.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletionContext.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletionInfo.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletionItem.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletionProposal.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletionProvider.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceCompletionWords.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceEncoding.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceFile.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceFileLoader.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceFileSaver.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceGutter.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceGutterRenderer.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceGutterRendererPixbuf.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceGutterRendererText.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceLanguage.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceLanguageManager.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceMap.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceMark.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceMarkAttributes.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourcePrintCompositor.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceRegion.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceSearchContext.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceSearchSettings.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceSpaceDrawer.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceStyle.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceStyleScheme.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceStyleSchemeChooser.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceStyleSchemeChooserButton.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceStyleSchemeChooserWidget.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceStyleSchemeManager.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceTag.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceUndoManager.html
/usr/share/gtk-doc/html/gtksourceview-3.0/GtkSourceView.html
/usr/share/gtk-doc/html/gtksourceview-3.0/annotation-glossary.html
/usr/share/gtk-doc/html/gtksourceview-3.0/api-index-full.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch01.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch02.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch03.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch04.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch05.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch06.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch07.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch08.html
/usr/share/gtk-doc/html/gtksourceview-3.0/ch09.html
/usr/share/gtk-doc/html/gtksourceview-3.0/gtksourceview-3.0-GtkSourceUtils.html
/usr/share/gtk-doc/html/gtksourceview-3.0/gtksourceview-3.0-Version-Information.html
/usr/share/gtk-doc/html/gtksourceview-3.0/gtksourceview-3.0.devhelp2
/usr/share/gtk-doc/html/gtksourceview-3.0/home.png
/usr/share/gtk-doc/html/gtksourceview-3.0/index.html
/usr/share/gtk-doc/html/gtksourceview-3.0/lang-reference.html
/usr/share/gtk-doc/html/gtksourceview-3.0/lang-tutorial.html
/usr/share/gtk-doc/html/gtksourceview-3.0/left-insensitive.png
/usr/share/gtk-doc/html/gtksourceview-3.0/left.png
/usr/share/gtk-doc/html/gtksourceview-3.0/object-tree.html
/usr/share/gtk-doc/html/gtksourceview-3.0/pt01.html
/usr/share/gtk-doc/html/gtksourceview-3.0/pt02.html
/usr/share/gtk-doc/html/gtksourceview-3.0/pt03.html
/usr/share/gtk-doc/html/gtksourceview-3.0/pt04.html
/usr/share/gtk-doc/html/gtksourceview-3.0/right-insensitive.png
/usr/share/gtk-doc/html/gtksourceview-3.0/right.png
/usr/share/gtk-doc/html/gtksourceview-3.0/style-reference.html
/usr/share/gtk-doc/html/gtksourceview-3.0/style.css
/usr/share/gtk-doc/html/gtksourceview-3.0/up-insensitive.png
/usr/share/gtk-doc/html/gtksourceview-3.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgtksourceview-3.0.so.1
/usr/lib64/libgtksourceview-3.0.so.1.8.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-gtksourceview-soname3/caeb68c46fa36651acf592771d09de7937926bb3

%files locales -f gtksourceview-3.0.lang
%defattr(-,root,root,-)

