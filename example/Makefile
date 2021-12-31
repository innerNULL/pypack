# file: Makefile
# date: 2021-12-31


BUILD:=$(shell wget -qO - https://raw.githubusercontent.com/innerNULL/pypack/main/pypack.sh | bash /dev/stdin ./pypack.json)
UNZIP:=$(shell cd _build && mkdir runtime && cd runtime && tar -xvzf ../pyenv.tar.gz && cd ../..)
LINK:=$(shell ln -s _build/runtime/bin/python ./python)
PREPROCESS:=$(shell ./python -c "import stanza; stanza.download('zh', processors='tokenize,ner')")

all:
    @echo $(BUILD)
    @echo $(UNZIP)
    @echo $(LINK)
    @echo $(PREPROCESS)
