%global tl_name texblend
%global tl_revision 68961

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Compile segments of LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texblend
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texblend.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texblend.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texblend.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This tool compiles individual files that are included as parts of larger
documents. It utilizes the preamble of the main document but disregards
all other included files. The main purpose is to allow fast compilation
of particular chapters or sections, eliminating the need to recompile
the entire document. This facilitates an efficient way to check for
formatting or syntax errors in the particular part of the document being
worked on.

