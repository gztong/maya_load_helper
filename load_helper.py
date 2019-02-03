import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds
import maya.mel as mel

#plugin_mel_path = '"E:/CIS660/load_plugin.mel"'
plugin_path = ' "E:/CIS660/hw02/MayaPluginHw2/x64/Debug/LSystemMaya.mll"'

commandName = 'pyLoadHelper'

cmd_str = 'global string $gMainWindow; \
    setParent $gMainWindow; \
    menu \
    -label "load"\
    -parent $gMainWindow\
    -tearOff on\
    load_menu;\
    menuItem\
    -c "load"\
    -ann "load"\
    -label "load"\
    -echoCommand true;\
    menuItem\
    -c "unload"\
    -ann "unload"\
    -label "unload"\
    -echoCommand true;\
\
global proc load()\
{\
    loadPlugin -n "lsystem" +'plugin_path+'\
}\
\
global proc unload()\
{\
    unloadPlugin -force lsystem;\
}'

class MyCommandClass( OpenMayaMPx.MPxCommand ):
    
    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxCommand.__init__(self)
    
    def doIt(self, args):
        ''' Command execution. '''
        #mel.eval('source ' + plugin_mel_path)
        mel.eval(cmd_str)

def cmdCreator():
    ''' Create an instance of our command. '''
    return OpenMayaMPx.asMPxPtr( MyCommandClass() )

def initializePlugin( mobject ):
    ''' Initialize the plug-in when Maya loads it. '''
    mplugin = OpenMayaMPx.MFnPlugin( mobject )
    try:
        mplugin.registerCommand( commandName, cmdCreator )
        mel.eval(cmd_str)
    except:
        sys.stderr.write( 'Failed to register command: ' + commandName )

def uninitializePlugin( mobject ):
    ''' Uninitialize the plug-in when Maya un-loads it. '''
    mplugin = OpenMayaMPx.MFnPlugin( mobject )
    try:
        mplugin.deregisterCommand( commandName )
    except:
        sys.stderr.write( 'Failed to unregister command: ' + commandName )