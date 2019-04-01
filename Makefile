all : init update dspsr

# LOC definations #
astrosoft_git = ~/astrosoft_git/src

GIT_COMMIT_DATE=$(shell git show -s --pretty=format:%cI)

# SRC website collection #
DSPSR_NAME			= dspsr
DSPSR_WEBSITE		= git://git.code.sf.net/p/dspsr/code
TEMPO_NAME	 		= tempo
TEMPO_WEBSITE 		= git://git.code.sf.net/p/tempo/tempo
TEMPO2_NAME  		= tempo2
TEMPO2_WEBSITE		= https://bitbucket.org/psrsoft/tempo2.git
PRESTO_NAME  		= presto
PRESTO_WEBSITE		= git://github.com/scottransom/presto.git
PSRCHIVE_NAME   	= psrchive
PSRCHIVE_WEBSITE 	= git://git.code.sf.net/p/psrchive/code


init:
	-mkdir ${astrosoft_git};
	cd ${astrosoft_git};
	git clone ${DSPSR_WEBSITE};
	git clone ${TEMPO_WEBSITE};
	git clone ${TEMPO2_WEBSITE};
	git clone ${PRESTO_WEBSITE};
	git clone ${PSRCHIVE_WEBSITE}

update : dspsr
	@echo "Update releated softwares"

dspsr :
	GIT_COMMIT_DATE=$(shell git show -s --pretty=format:%cI)
	cd ${astrosoft_git}/${DSPSR_NAME} && git pull && commit_date = `git show -s --pretty=format:%cI` && cd .. && tar zcvf ${DSPSR_NAME}-${commit_date}.tar.gz ${DSPSR_NAME}
