#paintproject.py
#Rahma Gillan
#League of Legends themed paint program

#imports
from pygame import *
from tkinter import *
from random import *
from math import *

#window and screen
import os

init()
#center the window
inf = display.Info()
w,h = inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '60,25'

screen = display.set_mode((w,h),NOFRAME)

display.flip()

#set screen size
screen = display.set_mode((1400,800))
screenRect = Rect(0,0,1400,800)

#background
backgroundPic = image.load("pictures/league_background2.jpg")
screen.blit(backgroundPic,(0,0))

#logo pictureloading, resizing, and bliting onto screen on top of coloured rectangle
loadlogoPic = image.load("pictures/League_of_Legends_logo.png")
logoPic = transform.scale(loadlogoPic,(200,75))
screen.blit(logoPic,(1055,20))

###########################################################################################

#for saving and loading pictures
root = Tk()
root.withdraw()

###################################################################################################################################

#canvas rectangle and drawing canvas rectangle
canvasRect = Rect(20,20,900,695)
draw.rect(screen,(255,255,255),canvasRect)

#upload and save button rectangles
uploadRect = Rect(1285,20,45,45)
saveRect = Rect(1335,20,45,45)
#undo and redo rectangles
undoRect = Rect(935,20,45,45)
redoRect = Rect(985,20,45,45)

#tool button rects
pencilRect = Rect(20,725,65,65)
highlighterRect = Rect(230,725,30,30)
spraypaintRect = Rect(90,725,65,65)
eraserRect = Rect(160,725,65,65)
clearRect = Rect(230,760,30,30)
drawlineRect = Rect(265,725,65,65)
drawrectangleRect = Rect(335,725,30,30)
drawellipseRect = Rect(335,760,30,30)
drawtriangleRect = Rect(370,725,30,30)
drawpolygonRect = Rect(370,760,30,30)
palettebuttonRect = Rect(545,725,65,65)
fillRect = Rect(405,725,65,65)
eyedropperRect = Rect(475,725,65,65)
colourblocksRect = Rect(650,725,270,65)
box1Rect = Rect(655,730,48,55)
box2Rect = Rect(708,730,48,55)
box3Rect = Rect(761,730,48,55)
box4Rect = Rect(814,730,48,55)
box5Rect = Rect(867,730,48,55)

toolRects = [pencilRect,highlighterRect,spraypaintRect,eraserRect,clearRect,
             drawlineRect,drawrectangleRect,drawellipseRect,drawtriangleRect,drawpolygonRect,
             palettebuttonRect,fillRect,eyedropperRect,colourblocksRect,box1Rect,box2Rect,box3Rect,
             box4Rect,box5Rect]

toolPics = ["pencil","highlighter","spraypaint","eraser","clear",
             "drawline","drawrectangle","drawellipse","drawtriangle","drawpolygon",
             "palettebutton","fill","eyedropper","colourblocks"]


#blit images onto the screen
toolIndex = 0                   #to correspond tools with toolRects list
while True: 
    for tool in toolRects:
        if toolIndex < 14:              #len(toolPics) not accounting for 5 extra rectangles in toolRects        
            blit_x = tool.x
            blit_y = tool.y
            #get file name of already resized pictures from toolPics list using toolIndex
            toolPic = image.load("pictures/"+toolPics[toolIndex]+".png")
            #blit image using blit_x and blit_y
            screen.blit(toolPic,(blit_x,blit_y))
            
            toolIndex += 1
        
    else:
        break
    
#draw tool button rectangles
for tool in toolRects:
    draw.rect(screen,(0,0,0),tool,1)


    
###################################################################################################################################
#rect containing all stamps
stampRect = Rect(975,100,360,180)
#rectangles for stamp buttons
stampRects = []

#Pictures for stamp buttons

loadchampButtons = ["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Ashe","AurelionSol",
          "Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia",
          "Chogath","Corki","Darius","Diana","Draven","DrMundo","Ekko","Elise","Evelynn","Ezreal",
          "Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim",
          "Heimerdinger","Illaoi","Irelia","Ivern","Janna","Jarvan","Jax","Jayce","Jhin","Jinx",
          "Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kennen","Khazix","Kindred","Kled",
          "Kogmaw","Leblanc","LeeSin","Leona","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar",
          "Maokai","MasterYi","MissFortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Nidalee","Nocturne",
          "Nunu","Olaf","Orianna","Pantheon","Poppy","Quinn","Rammus","Reksai","Renekton","Rengar",
          "Riven","Rumble","Ryze","Sejuani","Shaco","Shen","Shyvana","Singed","Sion","Sivir",
          "Skarner","Sona","Soraka","Swain","Syndra","TahmKench","Taliyah","Talon","Taric","Teemo",
          "Thresh","Tristana","Trundle","Tryndamere","Twistedfate","Twitch","Udyr","Urgot","Varus","Vayne",
          "Veigar","Velkoz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xerath","XinZhao",
          "Yasuo","Yorick","Zac","Zed","Ziggs","Zilean","Zyra"]

#loaded and resized images
champButtons = []
#champ counter
champ = 0

#loading stamp button images
for c in loadchampButtons:
    loadButton = image.load("champs/"+c+".png")
    buttonPic = transform.scale(loadButton,(45,45))
    champButtons.append(buttonPic)

#keep track of stamp page 
stampPage = 1

#stamp page arrows
#right arrow
loadrightArrow = image.load("pictures/rightArrow.png")
rightArrow = transform.scale(loadrightArrow,(45,45))
screen.blit(rightArrow,(1330,235))
#rect
rightarrowRect = Rect(1330,235,45,45)
#left arrow
loadleftArrow = image.load("pictures/leftArrow.png")
leftArrow = transform.scale(loadleftArrow,(45,45))
screen.blit(leftArrow,(933,235))
#rect
leftarrowRect = Rect(933,235,45,45)

##stamp background
loadstampBackground = image.load("pictures/black.jpg")
stampBackground = transform.scale(loadstampBackground,(360,180))

###################################################################################################################################

#stamps
#list for loading stamps
loadchampStamps = ["aatrox","ahri","akali","alistar","amumu","anivia","annie","ashe","aurelionsol",
          "azir","bard","blitzcrank","brand","braum","caitlyn","camille","cassiopeia",
          "chogath","corki","darius","diana","draven","drmundo","ekko","elise","evelynn","ezreal",
          "fiddlesticks","fiora","fizz","galio","gangplank","garen","gnar","gragas","graves","hecarim",
          "heimerdinger","illaoi","irelia","ivern","janna","jarvan","jax","jayce","jhin","jinx",
          "kalista","karma","karthus","kassadin","katarina","kayle","kennen","khazix","kindred","kled",
          "kogmaw","leblanc","leesin","leona","lissandra","lucian","lulu","lux","malphite","malzahar",
          "maokai","masteryi","missfortune","mordekaiser","morgana","nami","nasus","nautilus","nidalee","nocturne",
          "nunu","olaf","orianna","pantheon","poppy","quinn","rammus","reksai","renekton","rengar",
          "riven","rumble","ryze","sejuani","shaco","shen","shyvana","singed","sion","sivir",
          "skarner","sona","soraka","swain","syndra","tahmkench","taliyah","talon","taric","teemo",
          "thresh","tristana","trundle","tryndamere","twistedfate","twitch","udyr","urgot","varus","vayne",
          "veigar","velkoz","vi","viktor","vladimir","volibear","warwick","wukong","xerath","xinzhao",
          "yasuo","yorick","zac","zed","ziggs","zilean","zyra"]

#list of resized champion stamps
champStamps = []

for c in loadchampStamps:
    loadStamp = image.load("stamps/"+c+"stamp.png")
    stampWidth = loadStamp.get_width()
    stampHeight = loadStamp.get_height()
    #divide dimensions of picture by two 
    stampPic = transform.scale(loadStamp,(int(stampWidth/2),int(stampHeight/2)))
    #append picture into list 
    champStamps.append(stampPic)


###################################################################################################################################

#load, resize and blit upload and save icon
loaduploadPic = image.load("pictures/uploadicon.jpg")
uploadPic = transform.scale(loaduploadPic,(45,45))
screen.blit(uploadPic,(1285,20))

loadsavePic = image.load("pictures/saveicon.jpg")
savePic = transform.scale(loadsavePic,(45,45))
screen.blit(savePic,(1335,20))

#load, resize and blit undo and redo pictures
loadundoPic = image.load("pictures/undo.png")
undoPic = transform.scale(loadundoPic,(45,45))
screen.blit(undoPic,(935,20))

loadredoPic = image.load("pictures/redo.png")
redoPic = transform.scale(loadredoPic,(45,45))
screen.blit(redoPic,(985,20))


###################################################################################################################################

#canvas background pictures Rects
background_1Rect = Rect(935,290,215,100)
background_2Rect = Rect(935,395,215,100)
background_3Rect = Rect(1155,290,215,100)
background_4Rect = Rect(1155,395,215,100)
background_5Rect = Rect(935,500,215,100)
background_6Rect = Rect(1155,500,215,100)

loadbackgroundPics = ["canback1.jpg","canback2.png","canback3.jpg","canback4.jpg",
                      "canback5.jpg","canback6.png"]
backgroundPics = []
blitbackgroundPics = []

for picture in loadbackgroundPics:
    loadbackgroundPic = image.load("pictures/"+picture)
    #load and resize background pictures into two seperate lists
    backgroundPic = transform.scale(loadbackgroundPic,(215,100))
    backgroundPics.append(backgroundPic)
    blitbackgroundPic = transform.scale(loadbackgroundPic,(900,695))
    blitbackgroundPics.append(blitbackgroundPic)

#drawing background changing buttons
screen.blit(backgroundPics[0],(935,290))
screen.blit(backgroundPics[1],(935,395))
screen.blit(backgroundPics[2],(1155,290))
screen.blit(backgroundPics[3],(1155,395))
screen.blit(backgroundPics[4],(935,500))
screen.blit(backgroundPics[5],(1155,500))
#drawing background changing button rectangles 
draw.rect(screen,(0,0,0),background_1Rect,1)
draw.rect(screen,(0,0,0),background_2Rect,1)
draw.rect(screen,(0,0,0),background_3Rect,1)
draw.rect(screen,(0,0,0),background_4Rect,1)
draw.rect(screen,(0,0,0),background_5Rect,1)
draw.rect(screen,(0,0,0),background_6Rect,1)

#keep track of current background
currentBackground = 0

#######################################################################################

#decoration pictures
loadRanks = ["BronzeBadge","SilverBadge","GoldBadge","PlatinumBadge","DiamondBadge",
             "MasterBadge","ChallengerBadge"]
Ranks= []

for r in loadRanks:
    loadrankPic = image.load("pictures/"+r+".png")
    rankPic = transform.scale(loadrankPic,(55,55))
    Ranks.append(rankPic)

rank_index = 0
#blit resized images onto the screen
for i in range(1005,1390,55):
    screen.blit(Ranks[rank_index],(i,739))
    rank_index += 1
    
#################################################################################################################################################

#instructions box
instructionsRect = Rect(935,610,435,105)
#instryction rectangle background
loadinstrucPic = image.load("pictures/instruction.jpg")
instrucPic = transform.scale(loadinstrucPic,(435,105))
screen.blit(instrucPic,(935,610))

#load arial font
font.init()
arialFont = font.SysFont("Arial",24)

#text
text = ["Pencil Tool","Left click and drag on canvas to draw","Highlighter Tool",
        "Spray Paint Tool","Eraser Tool","Left click and drag on canvas to erase",
        "Draw Line Tool","Left click and drag to draw a straight line",
        "Draw Rectangle Tool","Left click and drag on canvas to draw shape",
        "Right click and drag to draw filled shape","Draw Triangle Tool","Draw Ellipse Tool",
        "Draw Polygon Tool","Right click to plot the points of shape","Left click to draw shape",
        "Fill Tool","Click anywhere on canvas to fill area","Eyedropper Tool",
        "Get colour from location on canvas", "Stamps Tool","Choose stamp and drag onto canvas",
        "Scroll up and down to adjust size"]

############################################################################################################################################################

#colour palette
paletteRect = Rect(50,75,1300,650)
loadpalettePic = image.load("pictures/colourpalette.png")
palettePic = transform.scale(loadpalettePic,(1300,650))
palette = False

#drawing polygons tool list
polygonPoints = []

#upload flag
upload = False

#undo/redo lists
undo = []
redo = []
#undo/redo flags
undoBox = False
redoBox = False

#variables
tool = "pencil"
colour = (0,0,0)
tool_size = 2

#tool change flag
tool_change = False 
#colour change flag
colour_flag = False
#fill flag
filling = False

colours = [(255,255,0),(0,0,255),(0,255,0),(255,0,0),(0,0,0)]
draw.rect(screen,(colours[4]),box1Rect)#current colour box       
draw.rect(screen,(colours[3]),box2Rect)#red box
draw.rect(screen,(colours[2]),box3Rect)#green box
draw.rect(screen,(colours[1]),box4Rect)#blue box
draw.rect(screen,(colours[0]),box5Rect)#yellow box
    
#paint brush surface
brushCover = Surface((1400,800)).convert()
brushCover.set_alpha(55)
brushCover.set_colorkey((255,0,255))

#loop
running = True
while running:
    click = False
    clickUp = False

    for e in event.get():
        if e.type == QUIT:
            #ask for save on quit
            #input file name to save as
            result = filedialog.asksaveasfilename()
            #make sure something was input 
            if result != "":
                #make sure extension is there if not add extension 
                if result.find('.png') > 0:
                    image.save(screen.subsurface(canvasRect),result)
                else:
                    result += '.png'
                    image.save(screen.subsurface(canvasRect),result)
                     
            running = False

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                click = True

            #for drawing straight lines and shapes
            canCopy = screen.subsurface(canvasRect).copy()

            #mx,my at mouse button down
            startx,starty = mouse.get_pos()

            #for highlighter surface
            brushCover.fill((255,0,255))

            #changing size
            #scroll up
            if e.button == 4 and tool_size!= 30:
                tool_size += 1
            #scroll down
            if e.button == 5 and tool_size != 1:
                tool_size -= 1

        if e.type == MOUSEBUTTONUP:
            clickUp = True

            #mx,my at mousebuttonup
            endx,endy = mouse.get_pos()

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

#####################################################################################

    #tool size displaying rect
    tool_sizeRect = Rect(935,725,65,65)
    draw.rect(screen,(0,0,0),tool_sizeRect)
    #draw circle in the center of the rectangle
    draw.circle(screen,(255,255,255),(968,758),tool_size)

###################################################################################################################################

    #clearing instructions rectangle
    if tool_change == True:
        #blit background rectangle
        screen.blit(instrucPic,(935,610))
        #change sizes back to default sizes
        tool_size = 2
        #change flag back to false 
        tool_change = False 

    #highlighting and unhighlighting tools and drawing button rectangles
    if tool == "pencil":
        draw.rect(screen,(255,255,255),pencilRect,1)
        #lines of text for instructions
        text1 = arialFont.render(text[0],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[1],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[22],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "pencil":
        draw.rect(screen,(0,0,0),pencilRect,1)
        
    if tool == "highlighter":
        draw.rect(screen,(255,255,255),highlighterRect,1)
        text1 = arialFont.render(text[2],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[1],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[22],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "highlighter":
        draw.rect(screen,(0,0,0),highlighterRect,1)
            
    if tool == "spraypaint":
        draw.rect(screen,(255,255,255),spraypaintRect,1)
        text1 = arialFont.render(text[3],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[1],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[22],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "spraypaint":
        draw.rect(screen,(0,0,0),spraypaintRect,1)

    if tool == "eraser":
        draw.rect(screen,(255,255,255),eraserRect,1)
        text1 = arialFont.render(text[4],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[5],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[22],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "eraser":
        draw.rect(screen,(0,0,0),eraserRect,1)

    if tool == "clear":
        draw.rect(screen,(255,255,255),clearRect,1)
    if tool != "clear":
        draw.rect(screen,(0,0,0),clearRect,1)

    if tool == "drawline":
        draw.rect(screen,(255,255,255),drawlineRect,1)
        text1 = arialFont.render(text[6],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[7],True,(255,255,255))
        screen.blit(text2,(945,645))
    if tool != "drawline":
        draw.rect(screen,(0,0,0),drawlineRect,1)

    if tool == "drawrectangle":
        draw.rect(screen,(255,255,255),drawrectangleRect,1)
        text1 = arialFont.render(text[8],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[9],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[10],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "drawrectangle":
        draw.rect(screen,(0,0,0),drawrectangleRect,1)

    if tool == "drawellipse":
        draw.rect(screen,(255,255,255),drawellipseRect,1)
        text1 = arialFont.render(text[12],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[9],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[10],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "drawellipse":
        draw.rect(screen,(0,0,0),drawellipseRect,1)

    if tool == "drawtriangle":
        draw.rect(screen,(255,255,255),drawtriangleRect,1)
        text1 = arialFont.render(text[11],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[9],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[10],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "drawtriangle":
        draw.rect(screen,(0,0,0),drawtriangleRect,1)

    if tool == "drawpolygon":
        draw.rect(screen,(255,255,255),drawpolygonRect,1)
        text1 = arialFont.render(text[13],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[14],True,(255,255,255))
        screen.blit(text2,(945,645))
        text3 = arialFont.render(text[15],True,(255,255,255))
        screen.blit(text3,(945,670))
    if tool != "drawpolygon":
        draw.rect(screen,(0,0,0),drawpolygonRect,1)

    if tool == "fill":
        draw.rect(screen,(255,255,255),fillRect,1)
        text1 = arialFont.render(text[16],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[17],True,(255,255,255))
        screen.blit(text2,(945,645))
    if tool != "fill":
        draw.rect(screen,(0,0,0),fillRect,1)

    if tool == "eyedropper":
        draw.rect(screen,(255,255,255),eyedropperRect,1)
        text1 = arialFont.render(text[18],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[19],True,(255,255,255))
        screen.blit(text2,(945,645))
    if tool != "eyedropper":
        draw.rect(screen,(0,0,0),eyedropperRect,1)

    if tool == "stamps":
        draw.rect(screen,(255,255,255),eyedropperRect,1)
        text1 = arialFont.render(text[20],True,(255,255,255))
        screen.blit(text1,(945,620))
        text2 = arialFont.render(text[21],True,(255,255,255))
        screen.blit(text2,(945,645))


####################################################################################################################################

    if click and palette == False:
        #changing tools when buttons are clicked
        if pencilRect.collidepoint(mx,my):
            tool = "pencil"
            tool_change = True
        if highlighterRect.collidepoint(mx,my):
            tool = "highlighter"
            tool_change = True
        if spraypaintRect.collidepoint(mx,my):
            tool = "spraypaint"
            tool_change = True
        if eraserRect.collidepoint(mx,my):
            tool = "eraser"
            tool_change = True
        if clearRect.collidepoint(mx,my):
            tool = "clear"
            tool_change = True
        if drawlineRect.collidepoint(mx,my):
            tool = "drawline"
            tool_change = True
        if drawrectangleRect.collidepoint(mx,my):
            tool = "drawrectangle"
            tool_change = True
        if drawellipseRect.collidepoint(mx,my):
            tool = "drawellipse"
            tool_change = True
        if drawtriangleRect.collidepoint(mx,my):
            tool = "drawtriangle"
            tool_change = True
        if drawpolygonRect.collidepoint(mx,my):
            tool = "drawpolygon"
            tool_change = True
        if fillRect.collidepoint(mx,my):
            tool = "fill"
            tool_change = True
        if eyedropperRect.collidepoint(mx,my):
            tool = "eyedropper"
            tool_change = True
        if stampRect.collidepoint(mx,my):
            tool = "stamps"
            tool_change = True

            
###########################################################################################################################

    #drawing undo and redo button rectangles
    draw.rect(screen,(0,0,0),undoRect,2)
    draw.rect(screen,(0,0,0),redoRect,2)

    #copy blank canvas and append into list for undo tool
    if click == True and len(undo) == 0 and canvasRect.collidepoint(mx,my) and palette == False:
        canCopy = screen.subsurface(canvasRect).copy()
        undo.append(canCopy)

    #make a list of copied canvases at clickUp for undo list
    if clickUp == True and canvasRect.collidepoint(mx,my) and palette == False:
        canCopy = screen.subsurface(canvasRect).copy()
        undo.append(canCopy)
        #remove everything from redo list when click up happens on canvas
        del redo[:]

    #undo tool
    if undoRect.collidepoint(mx,my) and palette == False:
        if click:
            undoBox = True
        #highlight undo button box
        if undoBox == True:
            draw.rect(screen,(255,255,255),undoRect,2)
        #undo when mouse button goes up after click
        if clickUp:
            undoBox = False
            #check to make sure list is not empty after blank canvas
            if len(undo) > 1:
                #blit last canvas copy in undo list onto screen
                screen.blit(undo[-2],(20,20))
                #append blit surface into redo list from undo list
                redo.append(undo[-1])
                #remove from undo list
                del undo[-1]

    #redo tool
    if redoRect.collidepoint(mx,my) and palette == False:
        if click:
            redoBox = True
        #highlight redo button box
        if redoBox == True:
            draw.rect(screen,(255,255,255),redoRect,2)
        #redo when mouse button goes up after click
        if clickUp:
            redoBox = False
            draw.rect(screen,(255,255,255),redoRect,2)
            #make sure redo list is not empty
            if len(redo) > 0:
                #blit last canvas copy from undo list onto screen
                screen.blit(redo[-1],(20,20))
                #append redo copy back into undo
                undo.append(redo[-1])
                #remove blited copy from list
                del redo[-1]

###################################################################################################################################

    #highlighting and drawing upload button
    draw.rect(screen,(0,0,0),uploadRect,2)

    if uploadRect.collidepoint(mx,my) and palette == False:
        if mb[0] == 1:
            draw.rect(screen,(255,255,255),uploadRect,2)
        #activate tool at click
        if click:
            #upload file using Tk, only upload .jpg and .png files
            result = filedialog.askopenfilename(filetypes=[("Pictures","*.png;*.jpg")])
            #check if a file was opened
            if result != "":
                useruploadPic = image.load(result)
                #change upload flag
                upload = True
            
    #blit image onto canvas at desired location if upload is true
    if canvasRect.collidepoint(mx,my) and upload == True:
        screen.set_clip(canvasRect)
        #change tool to nothing and save old tool
        oldTool = tool
        tool = ""
        #blit uploaded picture if canvas is pressed
        if mb[0] == 1:
            screen.blit(canCopy,(20,20))
            #get the width and the height of the image
            picWidth = useruploadPic.get_width()
            picHeight = useruploadPic.get_height()
            #center (mx,my) onuploaded picture
            screen.blit(useruploadPic,(mx - (picWidth//2),my - (picHeight//2)))
            #change tool back
            tool = oldTool
            upload = False
        screen.set_clip(None)

    #highlighting and drawing save button
    draw.rect(screen,(0,0,0),saveRect,2)

    if saveRect.collidepoint(mx,my) and palette == False:
        if mb[0] == 1:
            draw.rect(screen,(255,255,255),saveRect,2)
        #activate tool at click
        if click:
            #input file name to save as
            result = filedialog.asksaveasfilename()
            #make sure something was input 
            if result != "":
                #make sure extension is there if not add extension 
                if result.find('.png') > 0:
                    image.save(screen.subsurface(canvasRect),result)
                else:
                    result += '.png'
                    image.save(screen.subsurface(canvasRect),result)
                     
###################################################################################################################################

    #if palette button pressed
    if click:
        #make sure palette is false when button pressed
        if palettebuttonRect.collidepoint(mx,my) and palette == False:
            palette = True
            oldTool = tool
            #change tool to nothing so no marks left when click on palette
            tool = ""
            #copy palette before picture of palette blit onto screen
            prepaletteScreen = screen.copy()
            #highlight palette button rect
            draw.rect(screen,(255,255,255),palettebuttonRect,1)
            #blit palette picture
            screen.blit(palettePic,(50,75))
        if palette == True:
            if paletteRect.collidepoint(mx,my):
                #gets colour
                colour = screen.get_at((mx,my))
                #blits back old screen
                screen.blit(prepaletteScreen,(0,0))

    #make sure mouse button up and tool goes back to old tool
    if clickUp and palette == True:
        if paletteRect.collidepoint(mx,my):
            tool = oldTool
            palette = False
            #keep track of if colour was changed
            colour_flag = True


    ##colour boxes
    draw.rect(screen,(255,255,255),box1Rect,2)#highlighted current colour box
    #whenever colour has been changed
    if colour_flag == True:
        #adjust list according to chosen colours
        colours.append(colour)
        del colours[0]
        #redraw rectangles
        draw.rect(screen,(colours[4]),box1Rect)
        draw.rect(screen,(colours[3]),box2Rect)        
        draw.rect(screen,(colours[2]),box3Rect)
        draw.rect(screen,(colours[1]),box4Rect)
        draw.rect(screen,(colours[0]),box5Rect)
        
        colour_flag = False

    #changing colour when presseing boxes
    if colourblocksRect.collidepoint((mx,my)):
        if click:
            colour = screen.get_at((mx,my))
            colour_flag = True

############################################################################################################

    if click and palette == False:
        if background_1Rect.collidepoint((mx,my)):
            #change tool to prevent canvas copies
            tool = "pencil"
            tool_change = True
            #blit background onto canvas from resized images list
            screen.blit(blitbackgroundPics[0],(20,20))
            #change value of current background for highlighting 
            currentBackground = 1
        if background_2Rect.collidepoint((mx,my)):
            tool = "pencil"
            tool_change = True
            screen.blit(blitbackgroundPics[1],(20,20))
            currentBackground = 2
        if background_3Rect.collidepoint((mx,my)):
            tool = "pencil"
            tool_change = True
            screen.blit(blitbackgroundPics[2],(20,20))
            currentBackground = 3
        if background_4Rect.collidepoint((mx,my)):
            tool = "pencil"
            tool_change = True
            screen.blit(blitbackgroundPics[3],(20,20))
            currentBackground = 4
        if background_5Rect.collidepoint((mx,my)):
            tool = "pencil"
            tool_change = True
            screen.blit(blitbackgroundPics[4],(20,20))
            currentBackground = 5
        if background_6Rect.collidepoint((mx,my)):
            tool = "pencil"
            tool_change = True
            screen.blit(blitbackgroundPics[5],(20,20))
            currentBackground = 6

    #highlighting and unhighlighting background changing boxes
    #make sure boxes are not drawn on top of palette
    if palette == False:
        if currentBackground == 1:
            draw.rect(screen,(255,255,255),background_1Rect,1)
        if currentBackground != 1:
            draw.rect(screen,(0,0,0),background_1Rect,1)
            
        if currentBackground == 2:
                draw.rect(screen,(255,255,255),background_2Rect,1)
        if currentBackground != 2:
            draw.rect(screen,(0,0,0),background_2Rect,1)

        if currentBackground == 3:
                draw.rect(screen,(255,255,255),background_3Rect,1)
        if currentBackground != 3:
            draw.rect(screen,(0,0,0),background_3Rect,1)

        if currentBackground == 4:
                draw.rect(screen,(255,255,255),background_4Rect,1)
        if currentBackground != 4:
            draw.rect(screen,(0,0,0),background_4Rect,1)

        if currentBackground == 5:
                draw.rect(screen,(255,255,255),background_5Rect,1)
        if currentBackground != 5:
            draw.rect(screen,(0,0,0),background_5Rect,1)

        if currentBackground == 6:
                draw.rect(screen,(255,255,255),background_6Rect,1)
        if currentBackground != 6:
            draw.rect(screen,(0,0,0),background_6Rect,1)

#################################################################################################################################

   ##changing stamp pages
    if click and palette == False:
        #when right arrow clicked
        if rightarrowRect.collidepoint((mx,my)):
            
            if stampPage == 5:
                #change champ counter according to new page (champ = stampPage*32 - 32)
                champ = 0 
                #go back to first page
                stampPage = 1
            elif stampPage == 4:
                champ = 96
                stampPage = 5
            elif stampPage == 3:
                champ = 96
                stampPage = 4
            elif stampPage == 2:
                champ = 64
                stampPage = 3
            elif stampPage == 1:
                champ = 32
                stampPage = 2
                

        #when left arrow clicked 
        if leftarrowRect.collidepoint((mx,my)):
            if stampPage == 1:
                #change champ counter according to new page (champ = stampPage*32 - 32)
                champ = 96
                stampPage = 5
            elif stampPage == 2:
                champ = 0
                stampPage = 1
            elif stampPage == 3:
                champ = 32
                stampPage = 2
            elif stampPage == 4:
                champ = 64
                stampPage = 3
            elif stampPage == 5:
                champ = 96
                stampPage = 4

               
    ##stampbuttons
    if stampPage == 1:        ##Page 1
        #Row 1
        if champ < 8: #based on champs per row
            #blit images to locations using for loop
            for i in range (975,1296,45):
                #blit on the picture
                screen.blit(champButtons[champ],(i,100))
                #change index for next time around loop 
                champ += 1
                #append rect of button into list
                stampRects.append((Rect(i,100,45,45)))
        #Row 2      
        elif champ < 16:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,145)) 
                champ += 1
                stampRects.append((Rect(i,145,45,45)))
        #Row 3
        elif champ < 24:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,190)) 
                champ += 1
                stampRects.append((Rect(i,190,45,45)))
        #Row 4
        elif champ < 32:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,235)) 
                champ += 1
                stampRects.append((Rect(i,235,45,45)))
                
    elif stampPage == 2:        ##Page 2
        #Row 1
        if champ < 40: 
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,100))
                champ += 1
                stampRects.append((Rect(i,100,45,45)))
        #Row 2      
        elif champ < 48:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,145)) 
                champ += 1
                stampRects.append((Rect(i,145,45,45)))
        #Row 3
        elif champ < 56:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,190)) 
                champ += 1
                stampRects.append((Rect(i,190,45,45)))
        #Row 4
        elif champ < 64:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,235)) 
                champ += 1
                stampRects.append((Rect(i,235,45,45)))

    elif stampPage == 3:        ##Page 3
       #Row 1
        if champ < 72: 
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,100))
                champ += 1
                stampRects.append((Rect(i,100,45,45)))
        #Row 2      
        elif champ < 80:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,145)) 
                champ += 1
                stampRects.append((Rect(i,145,45,45)))
        #Row 3
        elif champ < 88:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,190)) 
                champ += 1
                stampRects.append((Rect(i,190,45,45)))
        #Row 4
        elif champ < 96:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,235)) 
                champ += 1
                stampRects.append((Rect(i,235,45,45)))
                
    elif stampPage == 4:        ##Page 4
        #Row 1
        if champ < 104: 
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,100))
                champ += 1
                stampRects.append((Rect(i,100,45,45)))
        #Row 2      
        elif champ < 112:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,145)) 
                champ += 1
                stampRects.append((Rect(i,145,45,45)))
        #Row 3
        elif champ < 120:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,190)) 
                champ += 1
                stampRects.append((Rect(i,190,45,45)))
        #Row 4
        elif champ < 128:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,235)) 
                champ += 1
                stampRects.append((Rect(i,235,45,45)))

                
    elif stampPage == 5:        ##Page 5
        #blit page 4 onto page 5 first because only 6 stamps
        #Row 1
        if champ < 104: 
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,100))
                champ += 1
                stampRects.append((Rect(i,100,45,45)))
        #Row 2      
        elif champ < 112:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,145)) 
                champ += 1
                stampRects.append((Rect(i,145,45,45)))
        #Row 3
        elif champ < 120:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,190)) 
                champ += 1
                stampRects.append((Rect(i,190,45,45)))
        #Row 4
        elif champ < 128:
            for i in range (975,1296,45):
                screen.blit(champButtons[champ],(i,235)) 
                champ += 1
                stampRects.append((Rect(i,235,45,45)))

        else:
            for i in range (975,1296,45):
                if champ < 134:
                    screen.blit(champButtons[champ],(i,100))
                    champ += 1                
                    stampRects.append((Rect(i,100,45,45)))
                    #blit on final missing image
                    screen.blit(champButtons[-1],(1200,100))
            
               
#######################################################################################
                    
    #using tools
    screen.set_clip(canvasRect)

    if tool == "pencil":
        #make sure on pencil clicks canvas
        if canvasRect.collidepoint(mx,my):
            if mb[0] == 1:
                draw.circle(screen,(colour),(mx,my),tool_size)
                #prevent spaces in between circles one pixel greater than twice the radius of the circle
                draw.line(screen,(colour),(oldx,oldy),(mx,my),tool_size*2+1)

            oldx = mx
            oldy = my

    elif tool == "highlighter":
        #make sure on canvas
        if canvasRect.collidepoint(mx,my):
            if mb[0]==1:
                #draw line on alpha surface
                draw.circle(brushCover,(colour),(mx-20,my-20),tool_size)
                draw.line(brushCover,(colour),(oldx-20,oldy-20),(mx-20,my-20),tool_size*2+1)

            if 1 in mb:
                #blit surface and screen
                screen.blit(canCopy,(20,20))
                screen.blit(brushCover,(20,20))

            oldx = mx
            oldy = my

    elif tool == "spraypaint":
        rmx = randint(-2*tool_size,2*tool_size)
        rmy = randint(-2*tool_size,2*tool_size)
        r  = (rmx**2+rmy**2)**0.5
        #check if random pixel outside circle radius
        if r <= tool_size*2:
            if mb[0] == 1:
                screen.set_at((mx+rmx,my+rmy),(colour))

    elif tool == "eraser":
        #make sure eraser on canvas
        if canvasRect.collidepoint(mx,my):
            if mb[0] == 1:
                draw.circle(screen,(255,255,255),(mx,my),tool_size)
                #prevent spaces in between circles when mouse moves fast
                draw.line(screen,(255,255,255),(oldx,oldy),(mx,my),tool_size*2+1)

            oldx = mx
            oldy = my

    elif tool == "clear":
        #draw a new Rect on top of canvas to clear canvas
        draw.rect(screen,(255,255,255),canvasRect)
        #change current background back to 0
        currentBackground = 0
        #change tool back to pencil
        tool = "pencil"

    elif tool == "drawline":
        if mb[0] == 1:
            screen.blit(canCopy,(20,20))
            draw.line(screen,(colour),(startx,starty),(mx,my),2)

    elif tool == "drawrectangle":
        #unfilled rectangle left click and drag
        if mb[0] == 1:
            screen.blit(canCopy,(20,20))
            rectWidth = my-starty
            rectLength = mx-startx
            draw.rect(screen,(colour),(startx,starty,rectLength,rectWidth),2)
        #filled rectangle right click and drag
        if mb[2] == 1:
            screen.blit(canCopy,(20,20))
            width = my-starty
            length = mx-startx
            draw.rect(screen,(colour),(startx,starty,length,width))

    elif tool == "drawtriangle":
        #unfilled triangle left click and drag
        if mb[0] == 1:
            screen.blit(canCopy,(20,20))
            #draw 3 lines for isosceles triangle
            draw.line(screen,(colour),(startx,starty),(mx,my),2)
            #(mx-(mx-startx)*2) is x coordinate of third point 
            draw.line(screen,(colour),(mx,my),(mx-(mx-startx)*2,my),2)
            draw.line(screen,(colour),(startx,starty),(mx-(mx-startx)*2,my),2)
        #filled triangle on right click
        if mb[2] == 1:
            screen.blit(canCopy,(20,20))
            #draw polygon to create filled triangle
            draw.polygon(screen,(colour),((startx,starty),(mx,my),((mx-(mx-startx)*2),my)))
              
    elif tool == "drawellipse":
        #unfilled ellipse left click and drag
        if mb[0] == 1:
            screen.blit(canCopy,(20,20))
            rectWidth = my-starty
            rectLength = mx-startx
            #rectangle ellipse is draw inside
            dimensions = Rect(startx,starty,rectLength,rectWidth)
            #prevent negative width and height values
            dimensions.normalize()

            #draw ellipse make sure the height and width > than the thickness
            if dimensions.height < 4 or dimensions.width < 4:
                draw.ellipse(screen,(colour),(dimensions))
            else:
                draw.ellipse(screen,(colour),(dimensions),2)

        #filled ellipse right click and drag
        if mb[2] == 1:
            screen.blit(canCopy,(20,20))
            rectWidth = my-starty
            rectLength = mx-startx
            dimensions = Rect(startx,starty,rectLength,rectWidth)
            dimensions.normalize()

            draw.ellipse(screen,(colour),(dimensions))

    elif tool == "drawpolygon":
        #append plotted points on right click into polygonPoints list
        if mb[2] == 1 and canvasRect.collidepoint((mx,my)):
            if click:
                polygonPoints.append((mx,my))
        if mb[0] == 1 and canvasRect.collidepoint((mx,my)):
            #draw polygon on left click if more than one point in the list
            if len(polygonPoints) > 1:
                draw.polygon(screen,(colour),polygonPoints,2)
                #delete all points in list for new polygon
                del polygonPoints[:]
            #reset polygon drawing on left click if only one point in list
            elif len(polygonPoints) == 1:
                del polygonPoints[:]
    
    elif tool == "fill":
        if click:
            filling = True
            #get colour of pixel before changed
            oldColour = screen.get_at((mx,my))
            #make list of points
            points=[(mx,my)] 

            #loop if len of list is not empty
            while len(points) > 0:
                #list for points already filled set to empty list 
                filledPoints = []
                for fill_x,fill_y in points:
                    #check if spilled points are on canvas and see if the point has the colour of old colour to keep looping until boundary hit
                    if canvasRect.collidepoint((fill_x,fill_y)) and screen.get_at((fill_x,fill_y)) == oldColour: 
                        #fill the pixel
                        screen.set_at((fill_x,fill_y),colour)                  

                        #add surrounding points to check them
                        filledPoints += [(fill_x+1,fill_y),(fill_x-1,fill_y),(fill_x,fill_y+1),(fill_x,fill_y-1)]  
                
                    #add filled points list to the points list to have their surround checked
                    points = filledPoints

        #delete lists after filling complete 
        if filling == True:
            del filledPoints[:]
            del points [:]
            filling = False
            
    elif tool  == "eyedropper":
        #get colour at click
        if click:
            if canvasRect.collidepoint((mx,my)):
                colour = screen.get_at((mx,my))
                colour_flag = True 

    elif tool == "stamps":
        if click:
    
            #check all the rectangles in stampRects list
            for rect in stampRects:
                #if rect is in the list
                if rect.collidepoint((mx,my)):
                    #get index location of the rect in the list
                    location = stampRects.index(rect)

                    #adjust location according to stamp page
                    if stampPage == 2:
                        location += 32
                    if stampPage == 3:
                        location += 64
                    if stampPage == 4:
                        location += 96
                    if stampPage == 5:
                        #only top 6 stamps change on page 5
                        if location < 6:
                            location += 128
                        #add page 4 values to the rest of the stamps
                        elif location >= 6:
                            #add on page 4 location
                            location += 96

                    #the location of rect in the rect list = the location of the stamp in the stamp list
                    stamp = champStamps[location]
            
                    
                    #get height and width of the stamp and divide by 2 to get mouse centered on stamp
                    stampx = int(champStamps[location].get_width()/2)
                    stampy = int(champStamps[location].get_height()/2)

        #blit stamp onto canvas    
        if canvasRect.collidepoint(mx,my):
            #make it so stamp can be dragged on the canvas
            if mb[0] == 1:
                screen.blit(canCopy,(20,20))
                screen.blit(stamp,(mx-stampx,my-stampy))


    screen.set_clip(None)

###################################################################################################################################

    display.flip()

quit()
