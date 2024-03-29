# Tree Tool By Rory Gardner 2024

import maya.cmds as cmds
import random
import re

flower_Var = False
noise_Var = True
Canopy_V1_Var = False
Canopy_V2_Var = False
branchLeaf_Var = False
trunkLeaf_Var = False
extrudeVertex_Var = True
noiseAmount = 1.1
trunkStems = 1

## Shaders ##
StemShader = cmds.shadingNode( 'lambert', asShader = True)     
cmds.setAttr( StemShader + '.color', 0.497, 0.426, 0.312, type = 'double3' )
 
CapShader = cmds.shadingNode( 'lambert', asShader = True)   
cmds.setAttr( CapShader + '.color', 0.258, 0.092, 0.049, type = 'double3' )  

def bigTree(winID, noiseAmount, branchLength, numberOfBranches, branchRandomLength, branchSections, branchY, 
flowerSize, flowerLength, trunkWidth, trunkHeight, trunkRandom, trunkRandomMove, branchTaper, 
canopySize, canopyHeight, trunkRotate, branchSpread, bushWidth, bushSize, flowerDivisions, branchStart, 
iterations, canopyShape2, canopySize2, leafIterations, leafLength, leafWidth, trunkSecondHalf, trunkStems):
    
    cmds.delete (cmds.ls(type='shadingDependNode'))
    #cmds.delete (cmds.ls(type='sets'))
    
    ## Shaders ##
    StemShader = cmds.shadingNode( 'lambert', asShader = True)     
    cmds.setAttr( StemShader + '.color', 0.497, 0.426, 0.312, type = 'double3' )
 
    CapShader = cmds.shadingNode( 'lambert', asShader = True)   
    cmds.setAttr( CapShader + '.color', 0.258, 0.092, 0.049, type = 'double3' )    
    
    ## Remove Old Tree ##
    if cmds.objExists('TreeOriginal'): 
        cmds.select("TreeOriginal")
        cmds.delete()
    if cmds.objExists('Canopy*'): 
        cmds.select("Canopy*")
        cmds.delete()
    if cmds.objExists('Trunk*'): 
        cmds.select("Trunk*")
        cmds.delete()              
        
    canopySet = cmds.sets(n='Canopy') 
    trunkSet = cmds.sets(n='Trunk')
          
    ### Random Numbers ##
    randomFloatScaleZXY = random.uniform(-0.1,0.1)
    randomTrunk = random.randint(32,32)
    randomBase = random.uniform(1.4,1.8)
    
    ### Make Trunk primitive ##
    Cylinder=cmds.polyCylinder (h=0.5,r=trunkWidth,sx=42,sy=1,name='TreeOriginal')
    cmds.hyperShade(assign = StemShader)       
    cmds.sets(add='Trunk')
    
    ## Leaf Vars ##
    leafLength = 20
    leafDown = 6
    
    ### Trunk First Half ##    
    for i in range (8): #8
        randomFloatScale = random.uniform(0.99+trunkRandom,1.0+trunkRandom)
        randomFloatX = random.uniform(-0.3,0.3)
        randomFloatZ = random.uniform(-0.3,0.3)
        randomFloatY = random.uniform(6.8,8.2)
        randomFloatTopY = random.uniform(0.8,3.2)
        randomFloatTopYsmall = random.uniform(0.1,0.3)        
        cmds.select(Cylinder[0]+'.f[43]') 
        cmds.polyExtrudeFacet(s=(randomFloatScale,randomFloatScale,randomFloatScale), t=(0, 0, 0), d=1)   
        cmds.rotate(random.uniform(-trunkRotate,trunkRotate),random.uniform(0,0),random.uniform(-trunkRotate,trunkRotate), r=True)
        cmds.move (randomFloatX*trunkRandomMove, randomFloatY+trunkHeight, randomFloatZ*trunkRandomMove, r=True)
    
    ## Create Base ##    
    cmds.select(Cylinder[0]+'.f[42]')
    cmds.scale(5.5,60.0,5.5, r=True)
    cmds.polySubdivideFacet (dv=1)    
    cmds.select(Cylinder[0]+'.f[44:85]')
    cmds.scale(randomBase,1.0,randomBase, r=True)
    cmds.select(Cylinder[0]+'.f[128:169]')
    cmds.scale(randomBase-0.2,1.0,randomBase-0.2, r=True)
    cmds.select(Cylinder[0]+'.f[212:253]')
    cmds.scale(randomBase-0.4,1.0,randomBase-0.4, r=True)
    cmds.select(Cylinder[0]+'.f[296:337]')
    cmds.scale(randomBase-0.5,1.0,randomBase-0.5, r=True)
    
    ## Base Roots ##  
    rootFaces = [Cylinder[0]+'.f[41]',Cylinder[0]+'.f[4]',Cylinder[0]+'.f[9]',Cylinder[0]+'.f[14]',Cylinder[0]+'.f[18]',Cylinder[0]+'.f[24]',Cylinder[0]+'.f[29]',Cylinder[0]+'.f[33]',Cylinder[0]+'.f[37]']
    index = 0
    for each in rootFaces:
        randomRoot = random.uniform(2.8,5.2)     
        randomRoot2 = random.uniform(-2.8,2.8)    
        cmds.select(rootFaces[index])  
        #cmds.polyExtrudeFacet()      
        cmds.polySubdivideFacet (dv=1)
        cmds.move(randomRoot2,randomRoot,randomRoot2, r=True)
        index +=1
    
    cmds.select(Cylinder[0]+'.f[81]',Cylinder[0]+'.f[85]',Cylinder[0]+'.f[48]',Cylinder[0]+'.f[53]',Cylinder[0]+'.f[58]',Cylinder[0]+'.f[62]',Cylinder[0]+'.f[68]',Cylinder[0]+'.f[73]',Cylinder[0]+'.f[77]')
    cmds.scale(randomBase-0.2,1.0,randomBase-0.2, r=True)
    
    ## Longer Roots ##    
    longerRoots = [Cylinder[0]+'.f[27]',Cylinder[0]+'.f[21]',Cylinder[0]+'.f[16]',Cylinder[0]+'.f[7]',Cylinder[0]+'.f[2]',Cylinder[0]+'.f[12]',Cylinder[0]+'.f[31]',Cylinder[0]+'.f[35]',Cylinder[0]+'.f[39]']
    index2 = 0
    for each in rootFaces:
        
        randomRoot = random.uniform(-4.0,-8.0)     
        randomRoot2 = random.uniform(-1.2,1.2)    
        cmds.select(rootFaces[index2])               
        cmds.polySubdivideFacet (dv=1)
        #cmds.move(randomRoot2,randomRoot,randomRoot2, r=True)
        cmds.scale(random.uniform(1.1,2.0),1.0,random.uniform(1.1,2.0), r=True)
        index2 +=1
    
    if trunkStems == 1:          
        ### Trunk Second Half ##       
        for i in range (trunkSecondHalf): #24      
            trunkLeafscale = 1.0        
            randomFloatScale = random.uniform(0.99+trunkRandom,1.0+trunkRandom)
            randomFloatX = random.uniform(-0.3,0.3)
            randomFloatZ = random.uniform(-0.3,0.3)
            randomFloatY = random.uniform(4.8,8.2)
            randomFloatTopY = random.uniform(0.8,3.2)
            randomFloatTopYsmall = random.uniform(0.1,0.3)        
            cmds.select(Cylinder[0]+'.f[43]') 
            cmds.polyExtrudeFacet(s=(randomFloatScale,randomFloatScale,randomFloatScale), t=(0, 0, 0), d=1)   
            cmds.rotate(random.uniform(-trunkRotate,trunkRotate),random.uniform(0,0),random.uniform(-trunkRotate,trunkRotate), r=True)
            cmds.move (randomFloatX*trunkRandomMove, randomFloatY+trunkHeight, randomFloatZ*trunkRandomMove, r=True)
            
            
            
            #addNoiseCanopy(2)
            ### Trunk Leafs ###       
            if trunkLeaf_Var: 
                cmds.selectType( surfaceEdge=True ) 
  
                trunkEDscale = 1.2 
    
                for i in range (4):
                    cmds.polyExtrudeEdge(kft=False, lty=leafLength, ls=(trunkEDscale, trunkEDscale, trunkEDscale), s=(1.0,1.0,1.0 ), ro= (0,0,0), tp=0.1, d=2)
                    cmds.scale(trunkLeafscale,trunkLeafscale,trunkLeafscale, r=True, cs=True)
                    cmds.move(0,-leafDown,0, r=True)             
                    trunkEDscale -=0.02
                    trunkLeafscale -= 0.2
                
                trunkLeafs = cmds.polyListComponentConversion(toFace=True)
                cmds.select(trunkLeafs)
                cmds.sets(add='Canopy')    
                cmds.select('Canopy') 
                cmds.polySelectConstraint( pp=1 )
                cmds.polySelectConstraint( pp=1 )
                cmds.polySelectConstraint( pp=1 )
                cmds.polySelectConstraint( pp=1 )
                cmds.polySelectConstraint( pp=1 ) 
                cmds.hyperShade(assign = CapShader)                    
                leafLength -=0.5
                leafDown -=0.3
                
        ## Canopy's ##
        if Canopy_V2_Var:
            if trunkSecondHalf == 24:
                canopy_V2(iterations, canopySize2, canopyShape2 , trunkSecondHalf )     
            else:
                cmds.inViewMessage( amg='Error: Trunk Sections must be <hl>24</hl> For Canopy V2.', pos='midCenter', fts= 24, fade=True )
                
        if Canopy_V1_Var: 
            canopy_V1(trunkLeaf_Var, canopySize, canopyHeight, trunkSecondHalf )
                                            
    ## Trunk Top ##    
    cmds.select(Cylinder[0]+'.f[43]',  r=True)   
    cmds.scale(0.9,1,0.9, r=True)  
    cmds.sets(add='Canopy')         
    canopyEDscale = 2.0
        
    ## Create Multi Stem Tree ##    
    if trunkStems > 1: 
    
        ## Split Stem 1 ##
        cmds.select(Cylinder[0]+'.f[43]',  r=True)  
        cmds.polyPoke()
        cmds.select(Cylinder[0]+'.f[505:524]', Cylinder[0]+'.f[43]', r=True)
        cmds.polyCircularize(divisions=0, ws=True, twist=52)
        cmds.select(Cylinder[0]+'.f[505:524]', Cylinder[0]+'.f[43]', r=True)
        trunkExtrude(8,trunkRotate, trunkRandom, trunkHeight, 2)
    
        ## Split Stem 1 ##
        cmds.select(Cylinder[0]+'.f[484:504]', r=True)
        cmds.polyCircularize(divisions=0, ws=True, twist=-52)
        cmds.select(Cylinder[0]+'.f[484:504]', r=True)      
        trunkExtrude(8,trunkRotate, trunkRandom, trunkHeight, -2)   
        
        ## Stem Bush 1 ##  
        cmds.select(Cylinder[0]+'.vtx[725]',  r=True) 
        x,y,z = cmds.pointPosition();   
        cmds.polyPlatonic( r=22, subdivisions=2, sphericalInflation=random.uniform(4,6) )
        cmds.move(x,y+25,z) 
        
        addMovement(50,3)
        addNoiseCanopy(3) 
        cmds.scale(random.uniform(1,1.1),random.uniform(1,1.2),random.uniform(1,1.1))        
        cmds.rename("Bush_1")
        
        ## Stem Bush 1 ##
        cmds.select(Cylinder[0]+'.vtx[910]',  r=True) 
        x,y,z = cmds.pointPosition();   
        cmds.polyPlatonic( r=22, subdivisions=2, sphericalInflation=random.uniform(4,6) )
        cmds.move(x,y+25,z) 
        
        addMovement(50,3)
        addNoiseCanopy(3)
        cmds.scale(random.uniform(1,1.1),random.uniform(1,1.2),random.uniform(1,1.1))       
        cmds.rename("Bush_1")
        
            
        if trunkStems >= 3:
            cmds.select(Cylinder[0]+'.f[494:504]', r=True)
            cmds.polyCircularize(divisions=0, ws=True, twist=52)
            cmds.select(Cylinder[0]+'.f[495:504]', r=True)
            #cmds.rotate(50,0,0, r=True, pivot=(-2.053738, 164.376823, -19.828918),  os=True, fo=True)
            trunkExtrude(6,trunkRotate, trunkRandom, trunkHeight, -2)
            
            cmds.select(Cylinder[0]+'.f[484:493]', r=True)
            cmds.polyCircularize(divisions=0, ws=True, twist=0)
            cmds.select(Cylinder[0]+'.f[484:493]', r=True)
            trunkExtrude(6,trunkRotate, trunkRandom, trunkHeight, 2)
            
            cmds.select(Cylinder[0]+'.f[514:524]', r=True)
            cmds.polyCircularize(divisions=0, ws=True, twist=0)
            cmds.select(Cylinder[0]+'.f[514:524]', r=True)            
            trunkExtrude(6,trunkRotate, trunkRandom, trunkHeight, -2)
            
            cmds.select(Cylinder[0]+'.f[505:513]', Cylinder[0]+'.f[43]', r=True)
            cmds.polyCircularize(divisions=0, ws=True, twist=0)
            cmds.select(Cylinder[0]+'.f[505:513]', Cylinder[0]+'.f[43]', r=True)         
            trunkExtrude(6,trunkRotate, trunkRandom, trunkHeight, 2)
            
            cmds.polyPlatonic( r=22, subdivisions=2, sphericalInflation=5 ) 
            addMovement(50,2)   
                     
    ## Make Branches ##      
    if trunkLeaf_Var == False:
        cmds.setToolTo('Move')
        cmds.manipMoveContext( 'Move', e=True, m=0) 
        branches(numberOfBranches, branchSections, branchRandomLength, bushSize, leafIterations, bushWidth, flowerDivisions, branchStart, branchLength, branchY, branchSpread, branchTaper, leafLength, leafWidth, flowerLength, flowerSize)       
               
    ## Add Noise ##
    if noise_Var:
        cmds.select(clear=True)
        addNoise(noiseAmount)
    
    ## Extra Branches ##
    #for j in range (0):    
        #randomFace = random.randint(12000,25000)
        #cmds.select(Cylinder[0]+'.f['+str(randomFace)+']')
        #makeBranch()    

def trunkExtrude(sectionsT, trunkRotate, trunkRandom, trunkHeight, trunkMove):
    
    cmds.scale(1.1,1.0,1.1, r=True)  
    for i in range (sectionsT):         
        
        randomFloatScale = random.uniform(0.99+trunkRandom,1.0+trunkRandom)
        randomFloatX = random.uniform(-1.0,1.0)
        randomFloatZ = random.uniform(0.1,1.0)
        randomFloatY = random.uniform(1.8,12.2)  
        
        polyInfo = cmds.polyInfo(fn=True)
        polyInfoArray = re.findall(r"[\w.-]+", polyInfo[0])
        polyInfoX = float(polyInfoArray[2])
        polyInfoY = float(polyInfoArray[3])
        polyInfoZ = float(polyInfoArray[4])
        
   
        cmds.polyExtrudeFacet(s=(randomFloatScale,randomFloatScale,randomFloatScale), t=(0, 0, 0), d=1) 
        cmds.rotate(random.uniform(-trunkRotate,trunkRotate),random.uniform(0,0),random.uniform(-trunkRotate,trunkRotate), r=True)
        #cmds.move (randomFloatX*trunkMove, randomFloatY+trunkHeight, randomFloatZ*trunkMove, r=True)
        cmds.move(polyInfoX+randomFloatX*trunkMove,polyInfoY+randomFloatY+trunkHeight,polyInfoZ+randomFloatZ*trunkMove,r=True,os=True,wd=True)
           
def branches(numberOfBranches, branchSections, branchRandomLength, bushSize, leafIterations, bushWidth, flowerDivisions, branchStart, branchLength, branchY, branchSpread, branchTaper, leafLength, leafWidth, flowerLength, flowerSize): 

    CapShader = cmds.shadingNode( 'lambert', asShader = True)   
    cmds.setAttr( CapShader + '.color', 0.258, 0.092, 0.049, type = 'double3' )   
    cmds.select( clear=True )
    faceSelection = (branchStart)
    Cylinder = "TreeOriginal"  
                     
    ## Branch Base ##                 
    for i in range (numberOfBranches): 
                                  
        cmds.select(Cylinder+'.f['+str(faceSelection)+']')
        cmds.polyCircularize(divisions=1, ws=True)
        cmds.select(Cylinder+'.f['+str(faceSelection)+']')
            
        polyInfo = cmds.polyInfo(fn=True)
        polyInfoArray = re.findall(r"[\w.-]+", polyInfo[0])
        polyInfoX = float(polyInfoArray[2])
        polyInfoY = float(polyInfoArray[3])
        polyInfoZ = float(polyInfoArray[4])
                      
        #cmds.polyExtrudeFacet(s=(1.1,0.5,1.1), t=(0, 0, 0), kft=False) #SPLIT BRANCHES 
                 
        cmds.move(polyInfoX/15,polyInfoY/15,polyInfoZ/15,r=True,os=True,wd=True)
        cmds.scale(1.1,1.0,1.1, r=True)
            
        ## Branch Sections ##          
        for i in range (random.randint(branchSections,branchSections)):
                
            cmds.select(Cylinder+'.f['+str(faceSelection)+']')
            floatRotate = random.uniform(-20,20)
            floatBranch = random.uniform(branchLength,branchLength)           
            floatBranchX = random.uniform(-branchRandomLength,branchRandomLength)
            floatBranchY = random.uniform(branchRandomLength,branchRandomLength)
            floatBranchZ = random.uniform(-branchRandomLength,branchRandomLength)
            
            cmds.polyExtrudeFacet (s = (0.8,0.8,0.8), t=(0, 0, 0)) 
                      
            #cmds.rotate(0, floatRotate, 0, r=True, cs=True)
            cmds.move    (polyInfoX*branchLength+floatBranchX,    polyInfoY*branchLength+floatBranchY,    polyInfoZ*branchLength+floatBranchZ,r=True,os=True,wd=True)
            cmds.move    (0,polyInfoY+branchY,0,r=True)
            cmds.scale   (random.uniform(0.8,0.9),random.uniform(0.8,0.9),random.uniform(0.8,0.9), r=True, cs=True)
                
            ## Add Branch Leaves ##
            if branchLeaf_Var:
                              
                cmds.selectType( surfaceEdge=True ) 
                for i in range (leafIterations):
                    if extrudeVertex_Var:                       
                        cmds.polyExtrudeEdge(kft=False, lty=bushWidth, ls=(bushSize, bushSize, bushSize), s=(1.0,1.0,1.0 ), ro= (0,0,0), d=3)
                        cmds.polyCircularize(constructionHistory=1, smoothingAngle=30, evenlyDistribute=1, divisions=0, supportingEdges=1, twist=0, relaxInterior=1)
                    else:
                        cmds.polyExtrudeEdge(kft=True, lty=bushWidth, ls=(bushSize, bushSize, bushSize), s=(2.5,2.5,2.5 ), ro= (0,0,0), d=3)
                        cmds.polyCircularize(constructionHistory=1, smoothingAngle=30, evenlyDistribute=1, divisions=1, supportingEdges=1, twist=0, relaxInterior=1)
                        
                    
                    cmds.scale (random.uniform(0.8,1.9),random.uniform(0.8,1.9),random.uniform(0.8,1.9), r=True, cs=True)
                    cmds.move(0,-0.1,0, r=True)             
                    bushSize -=0.02
                    bushWidth -=0.2
                
                if extrudeVertex_Var:                       
                    cmds.polyExtrudeVertex(length=leafLength,width=leafWidth,d=1)            
                facesLeaf = cmds.polyListComponentConversion( toFace=True)
                cmds.select(facesLeaf)
                cmds.sets(add='Canopy')    
                cmds.select('Canopy')
                cmds.polySelectConstraint( pp=1, border=True)                                                    
                cmds.hyperShade(assign = CapShader)   
                #cmds.polyCircularize(constructionHistory=1, smoothingAngle=30, evenlyDistribute=1, divisions=1, supportingEdges=1, twist=10, relaxInterior=1)  
                                                                                     
        ## Make Flowers ##
        if flower_Var:
                
            floatBushRandomSize = random.uniform(0.1,0.2) 
            cmds.select(Cylinder+'.f['+str(faceSelection)+']')
            cmds.polySubdivideFacet (dv=flowerDivisions)                 
            for i in range (4):
                
                randomScaleBush = random.uniform(0.5,1.2)
                cmds.polyExtrudeFacet(s=(randomScaleBush,randomScaleBush,randomScaleBush), t=(polyInfoX/10,polyInfoY/2,polyInfoZ/10), d=1, kft=False)
                cmds.scale (random.uniform(0.8,1.4),random.uniform(0.8,1.4),random.uniform(0.8,1.4), r=True, cs=True)  
                #cmds.polySelectConstraint( pp=1 ) 
                cmds.hyperShade(assign = CapShader) 
                #cmds.polySelectConstraint( pp=2 )
            for i in range (1):
                cmds.polyExtrudeVertex(length=flowerLength,w=flowerSize+floatBushRandomSize) 
           
        faceSelection +=branchSpread
        branchLength -=branchTaper
                           
def canopy_V1(trunkLeaf_Var, canopyWidth, canopyHeight, trunkSecondHalf):  
    
    CapShader = cmds.shadingNode( 'lambert', asShader = True)   
    cmds.setAttr( CapShader + '.color', 0.258, 0.092, 0.049, type = 'double3' )  
    
    canopyHeight2=canopyHeight*2
    canopyWidth2= 0.95 
    cmds.select( clear=True )
    
    #Base   
    for i in range (8):
          
        Cylinder = "TreeOriginal"  
        cmds.select(Cylinder+'.f[43]')
            
        #cmds.scale(0.9,1,0.9, r=True)
        randomFloatCanopyV1 = random.uniform(-0.4,0.4)
        cmds.polyExtrudeFacet(s=(canopyWidth,1,canopyWidth), t=(randomFloatCanopyV1, canopyHeight/2-12, randomFloatCanopyV1), d=1)                  
        #cmds.polyExtrudeVertex(length=1,w=0.1)        
        #cmds.rotate(random.uniform(-5,5),random.uniform(0,0),random.uniform(-5,5))
        cmds.hyperShade(assign = CapShader)
    
    #Top                   
    for i in range (8):
        cmds.polyExtrudeFacet(s=(canopyWidth2,1,canopyWidth2), t=(randomFloatCanopyV1, canopyHeight2-2, randomFloatCanopyV1), d=1)  
        cmds.hyperShade(assign = CapShader)
        canopyWidth2 -=0.1
        canopyHeight2 -=2.5
    
    #Modify Shape        
    for j in range (40):
        floatRock = random.uniform(15,25)
        floatRockMove = random.uniform(60,80)
        floatRockMoveY = random.uniform(60,80)
        floatRockScale = random.uniform(0.8,1.9)
        floatRockSelect = random.randint(3,5)
        
        #Random Face Selection Range
        randomFace = random.randint(1640,1975)
           
        if trunkLeaf_Var:
            randomFace = random.randint(9788,10123)
        
        #For each Branch Section Amounts   
        modifyRanges = [
        (random.randint(884,1261)), (random.randint(926,1261)), (random.randint(968,1303)), (random.randint(1010,1345)), (random.randint(1052,1387)),       
        (random.randint(1094,1429)),(random.randint(1136,1471)),(random.randint(1178,1513)), (random.randint(1220,1555)), (random.randint(1262,1597)), 
        (random.randint(1304,1639)), (random.randint(1346,1681)), (random.randint(1388,1723)), (random.randint(1430,1765)), (random.randint(1472,1807)),         
        (random.randint(1514,1849)), (random.randint(1556,1891)), (random.randint(1598,1933)), (random.randint(1640,1975))]

        for x in range (0,18):                    
            if trunkSecondHalf == x+6:
                randomFace = modifyRanges[x]
                x+=1
        
        #Add Effect                               
        cmds.select(Cylinder+'.f['+str(randomFace)+']')
        cmds.polySelectConstraint( pp=1 )     
        polyInfo = cmds.polyInfo(fn=True)
        polyInfoArray = re.findall(r"[\w.-]+", polyInfo[0]) 
        polyInfoX = float(polyInfoArray[2])
        polyInfoY = float(polyInfoArray[3])
        polyInfoZ = float(polyInfoArray[4])   
        cmds.move (polyInfoX/floatRockMove,polyInfoY/floatRockMoveY,polyInfoZ/floatRockMove, r=True)
            
    cmds.sets(add='Canopy')         
    cmds.select( clear=True )
       
def canopy_V2(iterations, canopySize2, canopyShape2, trunkSecondHalf):   
     
    CapShader = cmds.shadingNode( 'lambert', asShader = True)   
    cmds.setAttr( CapShader + '.color', 0.258, 0.092, 0.049, type = 'double3' )  
        
    Cylinder = 'TreeOriginal'          
    cmds.select(Cylinder+'.f[43]')           
    cmds.scale(2.9,2.9,2.9, r=True, cs=True) 
    cmds.polySubdivideFacet(dv=1) 
    cmds.select(Cylinder+'.vtx[1428]') 
    cmds.move(0,5,0, r=True) 
          
    canopyFaces = [Cylinder+'.f[1379]',Cylinder+'.f[1385]',Cylinder+'.f[1349]',Cylinder+'.f[1356]',Cylinder+'.f[1364]',Cylinder+'.f[1371]',        
    Cylinder+'.f[1410]',Cylinder+'.f[1417]',Cylinder+'.f[1425]',Cylinder+'.f[1390]',Cylinder+'.f[1396]',Cylinder+'.f[1401]']    
    indexCF = 0
        
    for each in canopyFaces:
        randomCF = random.uniform(0.8,1.2)     
        randomFB = random.uniform(0.5,0.8)  
        cmds.select(canopyFaces[indexCF]) 
        polyInfo = cmds.polyInfo(fn=True)
        polyInfoArray = re.findall(r"[\w.-]+", polyInfo[0])
        polyInfoX = float(polyInfoArray[2])
        polyInfoY = float(polyInfoArray[3])
        polyInfoZ = float(polyInfoArray[4])   
             
        cmds.polyExtrudeFacet(s=(randomCF,randomCF,randomCF), t=(0, 0, 0), d=1)                              
        cmds.move(polyInfoX*randomFB,polyInfoY*randomFB,polyInfoZ*randomFB, r=True)
        #cmds.scale(1,1,0.4, r=True, cs=True) 
        cmds.polyCircularize(divisions=1, supportingEdges=1, ws=True)  
        cmds.select(canopyFaces[indexCF])
        #cmds.scale(1.2,1.2,1.2, r=True, cs=True)  
            
        for i in range(iterations):
            randomLB = random.uniform(0.2,0.4) 
            randomLBMOVE = random.uniform(-2.5,2.5)
            randomLBMOVEY = random.uniform(-0.5,2.5)  
            cmds.polyExtrudeVertex(length=canopySize2,width=canopyShape2)                             
            cmds.move(polyInfoX*randomLB+randomLBMOVE,polyInfoY*randomLB+randomLBMOVEY,polyInfoZ*randomLB+randomLBMOVE, r=True)
            cmds.scale(3.2,3.2,3.2, r=True, cs=True) 
                      
        indexCF +=1
        cmds.sets(add='Canopy') 
        cmds.select('Canopy')
        faces = cmds.polyListComponentConversion( toFace=True)
        cmds.select(faces)
        cmds.hyperShade(assign = CapShader)              
                 
def addNoise(amount):
    
    cmds.select( clear=True )    
    cmds.select('TreeOriginal')

    vtxCount = list(range(cmds.polyEvaluate(v=True)))
    random.shuffle(vtxCount)
    values = [random.triangular(amount,0,0) for i in range(10)]
    values_count = len(values)
    optimize_setter = []
    
    for x in vtxCount:
        mod = x % values_count
        optimize_setter += [values[mod-1]*1,values[mod-1]*1,values[mod-1]*1]
    cmds.setAttr('TreeOriginal.vtx[:]', *optimize_setter)
    cmds.polySmooth(c=1,dv=2,kb=True,ro=1)


def addMovement(number, amount):
    
    for j in range (number):
        floatRock = random.uniform(150,300)
        floatRockMove = random.uniform(50,100)
        floatRockScale = random.uniform(0.8,0.9)
        floatRockSelect = random.randint(3,5)
        
        randomFace = random.randint(10,800) 
        cmds.select('pPlatonic1'+'.f['+str(randomFace)+']')
        cmds.polySelectConstraint( pp=floatRockSelect )     
        polyInfo = cmds.polyInfo(fn=True)
        polyInfoArray = re.findall(r"[\w.-]+", polyInfo[0]) # convert the string to array with regular expression
        polyInfoX = float(polyInfoArray[2])
        polyInfoY = float(polyInfoArray[3])
        polyInfoZ = float(polyInfoArray[4])    
        cmds.move (polyInfoX/floatRockMove*amount,polyInfoY/floatRockMove*amount,polyInfoZ/floatRockMove*amount, r=True)
        cmds.polyExtrudeFacet(s=(floatRockScale,floatRockScale,floatRockScale), t=(polyInfoX/floatRock, polyInfoY/floatRock, polyInfoZ/floatRock))  
        
def addNoiseCanopy (amount):
         
    cmds.select( clear=True )    
    cmds.select('pPlatonic1')
        
    vtxCount2 = list(range(cmds.polyEvaluate(v=True)))
    random.shuffle(vtxCount2)
    values = [random.triangular(amount,0,0) for i in range(50)]
    values_count = len(values)
    optimize_setter = []
    
    for x in vtxCount2:
        mod = x % values_count
        optimize_setter += [values[mod-1]*1,values[mod-1]*1,values[mod-1]*1]
    cmds.setAttr('pPlatonic1.vtx[:]', *optimize_setter)
    cmds.polySmooth(c=1,dv=2,kb=True,ro=1)
      
def noise(input):
    global noise_Var
    noise_Var = input
    
def flower(flowerInput):
    global flower_Var
    flower_Var = flowerInput

def canopyV1(canopyInput1):
    global Canopy_V1_Var
    Canopy_V1_Var = canopyInput1    
        
def canopyV2(canopyInput2):
    global Canopy_V2_Var
    Canopy_V2_Var = canopyInput2
    
def leaf(leafInput):
    global trunkLeaf_Var
    trunkLeaf_Var = leafInput
    
def branchLeaf(branchLeafInput):
    global branchLeaf_Var
    branchLeaf_Var = branchLeafInput
    
def extrudeVertex (extrudeVertexInput):
    global extrudeVertex_Var
    extrudeVertex_Var = extrudeVertexInput
               
def makeBranch():
    
    selectionList = cmds.ls(selection=True)
    for objectName in selectionList:
        
        polyInfo = cmds.polyInfo(fn=True)
        polyInfoArray = re.findall(r"[\w.-]+", polyInfo[0])
        polyInfoX = float(polyInfoArray[2])
        polyInfoY = float(polyInfoArray[3])
        polyInfoZ = float(polyInfoArray[4])
        
        cmds.polyExtrudeFacet(s=(1.1,0.8,1.1), t=(0, 0, 0), kft=False)
          
        cmds.move(polyInfoX,polyInfoY,polyInfoZ,r=True,os=True,wd=True)
   
        for i in range (random.randint(3,4)):
            extraBranchX = random.uniform(1.8,8.2)
            extraBranchY = random.uniform(1.5,8.5)
            extraBranchZ = random.uniform(1.5,8.5)
            cmds.polyExtrudeFacet (s = (0.9,0.9,0.9), t=(0, 0, 0))
            #cmds.rotate(0, 0, 0, r=True, cs=True)
            cmds.move(polyInfoX*extraBranchX, polyInfoY*extraBranchY, polyInfoZ*extraBranchZ, r=True,os=True,wd=True)
            cmds.scale (random.uniform(0.8,0.99),random.uniform(0.8,0.99),random.uniform(0.8,0.99), r=True, cs=True)
            
def uvw(winID):
    
    cmds.select("TreeOriginal")
    cmds.ls( selection=True )
    cmds.polyProjection('TreeOriginal.f[*]', type='Cylindrical', ch=1, ibd=True, sf=True) 
        
    cmds.select ('Canopy')
    cmds.ls( selection=True )
    cmds.polyAutoProjection()
      
	#Close UI
def cancelProc(winID, *pArgs):
    cmds.deleteUI(winID)
    
def undoAction(winID):   
    cmds.undo()

    #Create UI            
def createUI():
         
    winID = cmds.window( title = 'Tree Tool', w = 200, h = 100)
    if cmds.window(winID, exists = True):
        cmds.deleteUI(winID)
    winID = cmds.window( title = 'Tree Tool', w = 200, h = 100)
    cmds.rowColumnLayout( numberOfRows=29, columnSpacing=[10,10], rowHeight=[(1, 60)], adjustableColumn=True)

    cmds.text( label='Tree Tool', align='center', h=40, fn='boldLabelFont', bgc=(0.1,0.1,0.1) )
       
    #Tree
    cmds.separator(h=10)      
    cmds.button(label = "Make Tree", h=40,command = lambda *args: bigTree(winID, 
    cmds.floatSliderGrp(noiseAmount, query=True, value=True), 
    cmds.floatSliderGrp(branchLength, query=True, value=True), 
    cmds.intSliderGrp(numberOfBranches, query=True, value=True), 
    cmds.floatSliderGrp(branchRandomLength, query=True, value=True), 
    cmds.intSliderGrp(branchSections, query=True, value=True), 
    cmds.floatSliderGrp(branchY, query=True, value=True), 
    #cmds.intSliderGrp(extraBranches, query=True, value=True), 
    cmds.floatSliderGrp(flowerSize, query=True, value=True), 
    cmds.floatSliderGrp(flowerLength, query=True, value=True), 
    cmds.floatSliderGrp(trunkWidth, query=True, value=True),   
    cmds.floatSliderGrp(trunkHeight, query=True, value=True),
    cmds.floatSliderGrp(trunkRandom, query=True, value=True),
    cmds.floatSliderGrp(trunkRandomMove, query=True, value=True),
    cmds.floatSliderGrp(branchTaper, query=True, value=True),
    cmds.floatSliderGrp(canopyWidth, query=True, value=True),
    cmds.floatSliderGrp(canopyHeight, query=True, value=True),
    cmds.floatSliderGrp(trunkRotate, query=True, value=True),
    cmds.intSliderGrp(branchSpread, query=True, value=True), 
    cmds.floatSliderGrp(bushWidth, query=True, value=True),
    cmds.floatSliderGrp(bushSize, query=True, value=True),
    cmds.intSliderGrp(flowerDivisions, query=True, value=True),  
    cmds.intSliderGrp(branchStart, query=True, value=True), 
    cmds.intSliderGrp(iterations, query=True, value=True),  
    cmds.floatSliderGrp(canopyShape2, query=True, value=True),
    cmds.floatSliderGrp(canopySize2, query=True, value=True), 
    cmds.intSliderGrp(leafIterations, query=True, value=True), 
    cmds.floatSliderGrp(leafLength, query=True, value=True),
    cmds.floatSliderGrp(leafWidth, query=True, value=True),
    cmds.intSliderGrp(trunkSecondHalf, query=True, value=True), 
    cmds.intSliderGrp(trunkStems, query=True, value=True))) 
                     
    cmds.separator(h=10)
    
    #Trunk
    cmds.text( label='Trunk', align='center', h=40, fn='boldLabelFont' ,  bgc=(0.1,0.2,0.1) )
    cmds.separator(h=10) 
    cmds.radioCollection()
    cmds.radioButton( label='Trunk Leaves On (Does not work with branches)', align='center', onCommand=lambda x:leaf(True))
    cmds.radioButton( label='Trunk Leaves Off', align='center', sl=True, onCommand=lambda x:leaf(False))
    cmds.separator(h=10)
    trunkStems = cmds.intSliderGrp(label='Trunk Stems', minValue=1, maxValue=6, value=1.0, field=True) 
    trunkWidth = cmds.floatSliderGrp(label='Trunk Width', minValue=1, maxValue=50, value=15.0, step=0.1, field=True)
    trunkHeight = cmds.floatSliderGrp(label='Trunk Height', minValue=0.1, maxValue=10, value=0.5, step=0.1, field=True)
    trunkRandom = cmds.floatSliderGrp(label='Trunk Taper', minValue=-0.1, maxValue=0.0, value=-0.04, step=0.01, pre=2, field=True)
    trunkRandomMove = cmds.floatSliderGrp(label='Trunk Random Move', minValue=-25, maxValue=25.0, value=5.00, step=0.01, pre=2, field=True)
    trunkRotate = cmds.floatSliderGrp(label='Trunk Curl', minValue=-15, maxValue=15.0, value=0.00, step=0.01, pre=1, field=True)
    trunkSecondHalf = cmds.intSliderGrp(label='Trunk Sections', minValue=6, maxValue=24, value=24, step=1,  field=True)
    cmds.separator(h=10) 
    
    #Branches
    cmds.text( label='Branches', align='center', h=40, fn='boldLabelFont', bgc=(0.1,0.2,0.1) )
    cmds.separator(h=10) 
    
    #Branch Extra Options
    cmds.radioButtonGrp( label='Leaves ', labelArray2=['On', 'Off'], numberOfRadioButtons=2, h=25, 
    onCommand1=lambda x:branchLeaf(True), 
    onCommand2=lambda x:branchLeaf(False))
    cmds.radioButtonGrp( label='Flowers ', labelArray2=['On', 'Off'], numberOfRadioButtons=2, h=25, 
    onCommand1=lambda x:flower(True), 
    onCommand2=lambda x:flower(False))   
    cmds.separator(h=10)  
    
    #Branch Adjustments  
    numberOfBranches = cmds.intSliderGrp(label='Branch Number', minValue= 0, maxValue=34, value=0, step=1, field=True) 
    branchStart = cmds.intSliderGrp(label='Branch Start', minValue=250, maxValue= 1000, value=500, step=1, field=True)
    branchLength = cmds.floatSliderGrp(label='Length', minValue= 0, maxValue=2, value=0.3, step=0.1, field=True)  
    branchRandomLength = cmds.floatSliderGrp(label='Curvyness', minValue=0, maxValue= 30, value=10, step=0.1, field=True)  
    branchSections = cmds.intSliderGrp(label='Branch Sections', minValue=0, maxValue= 10, value=3, step=1, field=True)
    branchY = cmds.floatSliderGrp(label='Branch Up', minValue=-10, maxValue=10, value=0, step=0.1, field=True)
    branchTaper = cmds.floatSliderGrp(label='Branch Taper', minValue=-0.1, maxValue=0.1, value=0.004, step=0.001,  pre=3, field=True)
    #extraBranches = cmds.intSliderGrp(label='Extra Branches (Dodgy!)', minValue=0, maxValue= 100, value=0, step=1, field=True)
    branchSpread = cmds.intSliderGrp(label='Branch Spread', minValue=30, maxValue= 120, value=53, step=1, field=True)
    
    
    cmds.separator(h=10) 
    
    #Flowers
    cmds.text( label='Flowers', align='center', h=40, fn='boldLabelFont',  bgc=(0.1,0.2,0.1)  )
    cmds.separator(h=10) 
    flowerSize = cmds.floatSliderGrp(label='Flower Shape', minValue=-5.0, maxValue=10, value=0.6, step=0.1, field=True)
    flowerLength = cmds.floatSliderGrp(label='Flower Size', minValue=1, maxValue=40, value=25.0, step=0.1, field=True)
    flowerDivisions = cmds.intSliderGrp(label='Flower Divisions', minValue=0, maxValue=5, value=1, step=1, field=True)     
    cmds.separator(h=10) 
    
    #Leaves
    cmds.text( label='Leaves', align='center', h=40, fn='boldLabelFont', bgc=(0.1,0.2,0.1)  )
    cmds.separator(h=10) 
    cmds.radioButtonGrp( label='Leaf Vertex Extrude ', labelArray2=['On', 'Off'], numberOfRadioButtons=2, h=25, 
    onCommand1=lambda x:extrudeVertex(True), 
    onCommand2=lambda x:extrudeVertex(False))
    bushSize = cmds.floatSliderGrp(label='Bush Size', minValue=0.1, maxValue=10, value=1.5, step=0.1, field=True)
    bushWidth = cmds.floatSliderGrp(label='Bush Width', minValue=0.1, maxValue=20, value=9, step=0.1, field=True)
    leafLength = cmds.floatSliderGrp(label='Leaf Length', minValue=0.1, maxValue=50, value=30, step=0.1, field=True)
    leafWidth = cmds.floatSliderGrp(label='Leaf Width', minValue=0.1, maxValue=20, value=1.5, step=0.1, field=True)
    leafIterations = cmds.intSliderGrp(label='Leaf Iterations (careful!)', minValue=0, maxValue= 3, value=1, step=1, field=True)
    cmds.separator(h=10) 
     
    #Canopy
    cmds.text( label='Canopy', align='center', h=40, fn='boldLabelFont', bgc=(0.1,0.2,0.1) )
    cmds.separator(h=10)
    cmds.radioButtonGrp( label='Canopy ',  labelArray3=['v1', 'v2', 'Off'], numberOfRadioButtons=3, h=50, 
    on1=lambda x:canopyV1(True), 
    on2=lambda x:canopyV2(True),
    of1=lambda x:canopyV1(False), 
    of2=lambda x:canopyV2(False))
    
    cmds.separator(h=10)
    canopyWidth = cmds.floatSliderGrp(label='Canopy V1 Width', minValue=1, maxValue=2, value=1.45, step=0.01, pre=2, field=True)
    canopyHeight = cmds.floatSliderGrp(label='Canopy V1 Height', minValue=1, maxValue=30, value=10, step=1, field=True)
    cmds.separator(h=10)
    iterations = cmds.intSliderGrp(label='Canopy V2 Iterations', minValue=0, maxValue=4, value=2, step=1, field=True)
    canopyShape2 = cmds.floatSliderGrp(label='Canopy V2 Shape', minValue=0.01, maxValue=2, value=0.2, step=0.01, pre=2, field=True)
    canopySize2 = cmds.floatSliderGrp(label='Canopy V2 Size', minValue=1, maxValue=30, value=5, step=0.1, field=True)    
    cmds.separator(h=10)
    
    #Noise
    cmds.text( label='Noise', align='center', h=40, fn='boldLabelFont',  bgc=(0.1,0.2,0.1)  )
    cmds.separator(h=10) 
    cmds.radioCollection()
    cmds.radioButton( label='On', align='center', sl=True, onCommand=lambda x:noise(True))
    cmds.radioButton( label='Off', align='center',  onCommand=lambda x:noise(False))
    noiseAmount = cmds.floatSliderGrp(label='Noise Amount', minValue=0.1, maxValue=10, value=1.1, step=0.1, field=True)   
    cmds.separator(h=10)  
    
    #UV
    cmds.button(label = "UVs", h=40,command = lambda *args: uvw(winID))   
    cmds.separator(h=10)     
    #Remove All
    cmds.button(label = "Undo", h=40,command = lambda *args: undoAction(winID))       
    cmds.separator(h=10) 
     
    #Exit    
    cmds.button(label = "Exit", h=40, command = lambda *args: cancelProc(winID))
    cmds.showWindow()
    

if __name__ == "__main__":
    createUI()
