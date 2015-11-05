TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    metropolis.cpp \
    random.cpp

INCLUDEPATH += /usr/local/include
LIBS += -L/usr/local/lib

LIBS += -larmadillo -llapack -lblas

HEADERS += \
    metropolis.h \
    random.h
