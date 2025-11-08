function init()
  rednet.open("back")
  term.clear()
  term.setBackgroundColor(colors.lightGray)
  term.setTextColor(colors.white)
  boucle = true
  nbturtle = ""
  while boucle do
    term.clear()
	term.setCursorPos(2,18)
	term.write("Entierement devloppe")
	term.setCursorPos(2,19)
	term.write("par :  Touille_exe")
    term.setCursorPos(2,2)
	term.write("Numero de la turtle: " .. nbturtle)
    local event, keyCode = os.pullEvent("key")
	if keyCode == keys.backspace then
	  if #nbturtle > 0  then
	    nbturtle = nbturtle:sub(1, #nbturtle - 1)
      end
	elseif keyCode == keys.zero or keyCode == keys.numPad0 then
	  nbturtle = nbturtle .. "0"
	elseif keyCode == keys.one or keyCode == keys.numPad1 then
	  nbturtle = nbturtle .. "1"
	elseif keyCode == keys.two or keyCode == keys.numPad2 then
	  nbturtle = nbturtle .. "2"
	elseif keyCode == keys.three or keyCode == keys.numPad3 then
	  nbturtle = nbturtle .. "3"
	elseif keyCode == keys.four or keyCode == keys.numPad4 then
	  nbturtle = nbturtle .. "4"
	elseif keyCode == keys.five or keyCode == keys.numPad5 then
	  nbturtle = nbturtle .. "5"
	elseif keyCode == keys.six or keyCode == keys.numPad6 then
	  nbturtle = nbturtle .. "6"
	elseif keyCode == keys.seven or keyCode == keys.numPad7 then
	  nbturtle = nbturtle .. "7"
	elseif keyCode == keys.eight or keyCode == keys.numPad8 then
	  nbturtle = nbturtle .. "8"
	elseif keyCode == keys.nine or keyCode == keys.numPad9 then
	  nbturtle = nbturtle .. "9"
	elseif keyCode == keys.enter or keyCode == keys.numPadEnter then
	  nbturtle = tonumber(nbturtle)
	  return
	end
  end
end

function commandesmanuelles()  
  menu = true
  while menu do
    term.clear()
    term.setBackgroundColor(colors.lightGray)
    -- Num turtle
    term.setCursorPos(12, 20)
    term.write("Num. turtle: " .. nbturtle)
    -- Bouton avancer
    paintutils.drawFilledBox(2,2,12,2,colors.black)
    term.setCursorPos(2,2)
    term.write("Avancer (z)")
    -- Bouton reculer
    paintutils.drawFilledBox(2,4,12,4,colors.black)
    term.setCursorPos(2,4)
    term.write("Reculer (s)")
    -- Bouton droite
    paintutils.drawFilledBox(2,6,12,6,colors.black)
    term.setCursorPos(2,6)
    term.write("Droite  (d)")
    -- Bouton gauche
    paintutils.drawFilledBox(2,8,12,8,colors.black)
    term.setCursorPos(2,8)
    term.write("Gauche  (q)")
    -- Bouton haut
    paintutils.drawFilledBox(2,10,12,10,colors.black)
    term.setCursorPos(2,10)
    term.write("haut    (a)")
    -- Bouton bas
    paintutils.drawFilledBox(2,12,12,12,colors.black)
    term.setCursorPos(2,12)
    term.write("bas     (e)")
	-- bouton retour
	paintutils.drawFilledBox(1,20,6,20,colors.red)
    term.setCursorPos(1,20)
    term.write("Retour")
	
	term.setBackgroundColor(colors.lightGray)
	--if des boutons
    local event, button, x, y = os.pullEvent("mouse_click")
    if button == 1 and x >= 2 and y == 2 and x <= 12 then      --avancer
	  rednet.send(nbturtle, "forward")
	  retourturtle()
	elseif button == 1 and x >= 2 and y == 4 and x <= 12 then  --reculer
	  rednet.send(nbturtle, "back")
	  retourturtle()
	elseif button == 1 and x >= 2 and y == 6 and x <= 12 then   --droite
	  rednet.send(nbturtle, "right")
	  retourturtle()
	elseif button == 1 and x >= 2 and y == 8 and x <= 12 then   --gauche
	  rednet.send(nbturtle, "left")
	  retourturtle()
	elseif button == 1 and x >= 2 and y == 10 and x <= 12 then   --haut
	  rednet.send(nbturtle, "top")
	  retourturtle()
	elseif button == 1 and x >= 2 and y == 12 and x <= 12 then   --bas
	  rednet.send(nbturtle, "bottom")
	  retourturtle()
	elseif button == 1 and x >= 1 and y == 20 and x <= 6 then   --retour
	  menu = false
	  mainmenu()
	  return
	end
  end
end


function minageoptimise()
  term.clear()
  term.setBackgroundColor(colors.lightGray)
  -- Num turtle
  term.setCursorPos(12, 20)
  term.write("Num. turtle: " .. nbturtle)
  coteduminage = "left"
  while true do
    for i = 1, 50 do
      rednet.send(nbturtle, "dig")
	  retourturtle()
      rednet.send(nbturtle, "forward")
      retourturtle()
      rednet.send(nbturtle, "digUp")
	  retourturtle()
      os.sleep(0.2) -- tempo pour pas saturer
    end
    if coteduminage == "left" then
      rednet.send(nbturtle, "left")
	  retourturtle()
    elseif coteduminage == "right" then
      rednet.send(nbturtle, "right")
	  retourturtle()
    end
    for i = 1, 3 do
      rednet.send(nbturtle, "dig")
	  retourturtle()
      rednet.send(nbturtle, "forward")
      retourturtle()
      rednet.send(nbturtle, "digUp")
	  retourturtle()
      os.sleep(0.2)
    end
    if coteduminage == "left" then
      rednet.send(nbturtle, "left")
	  retourturtle()
      coteduminage = "right"
    elseif coteduminage == "right" then
      rednet.send(nbturtle, "right")
	  retourturtle()
      coteduminage = "left"
    end
  end
end


function controleClavier()
  while true do
    local event, key = os.pullEvent("key")
    if keys.getName(key) == "q" then
      print("Arrêt demandé par l’utilisateur")
	  mainmenu()
      return  -- cette fonction se termine → le parallel s’arrête
    end
  end
end

function retourturtle()
  local id, msg = rednet.receive(60)
  if id == nbturtle then
    paintutils.drawFilledBox(2,3,25,3,colors.red)
	term.setCursorPos(2,3)
	term.write(msg)
  else
    term.clear()
	term.setCursorPos(2,3)
	error("Code erreur : 502")
  end
end


function tunnel()
  local tunnelchoice = true
  longeurtunnel = 50
  while tunnelchoice do
    term.clear()
    term.setBackgroundColor(colors.lightGray)
    -- boutton plus
    paintutils.drawFilledBox(2,2,4,2,colors.green)
    term.setCursorPos(2,2)
    term.write("<+>")
    -- boutton moins
    paintutils.drawFilledBox(12,2,14,2,colors.red)
    term.setCursorPos(12,2)
    term.write("<->")
    -- boutton start
    paintutils.drawFilledBox(6,2,10,2,colors.cyan)
    term.setCursorPos(6,2)
    term.write("Start")
    term.setCursorPos(6,3)
    term.write(longeurtunnel)
    local event, button, x, y = os.pullEvent("mouse_click")
    if button == 1 and x >= 2 and y == 2 and x <= 4 then -- boutton +
	  longeurtunnel = longeurtunnel + 10
    elseif button == 1 and x >= 12 and y == 2 and x <= 14 then -- boutton -
	  longeurtunnel = longeurtunnel - 10
	elseif button == 1 and x >= 6 and y == 2 and x <= 10 then -- boutton start
	  tunnelchoice = false
	end
  end
  for i = 1, longeurtunnel do
    rednet.send(nbturtle, "dig")
	retourturtle()
    rednet.send(nbturtle, "forward")
    retourturtle()
    rednet.send(nbturtle, "digUp")
	retourturtle()
  end
  mainmenu()
  return
end


function escalier()
  rednet.send(nbturtle, "up")
  for i = 1, longueurescalier do
    rednet.send(nbturtle, "dig")
    os.sleep(0.2)
    rednet.send(nbturtle, "forward")
    retourturtle()
    rednet.send(nbturtle, "digUp")
    rednet.send(nbturtle, "digDown")
    os.sleep(0.2)
    rednet.send(nbturtle, "down")
    retourturtle()
    rednet.send(nbturtle, "digDown")
  end
end


function mainmenu()
  term.clear()
  -- Num turtle
  term.setCursorPos(12, 20)
  term.write("Num. turtle: " .. nbturtle)
  -- Bouton commandes manuelles
  paintutils.drawFilledBox(2,2,21,2,colors.green)
  term.setCursorPos(2,2)
  term.write("Commandes manuelles")
  -- Bouton minage optimisé
  paintutils.drawFilledBox(2,4,17,4,colors.pink)
  term.setCursorPos(2,4)
  term.write("Minage optimise")
  -- Bouton tunnel
  paintutils.drawFilledBox(2,6,8,6,colors.cyan)
  term.setCursorPos(2,6)
  term.write("Tunnel")
  --if des boutons
  menu = true
  while menu do
    local event, button, x, y = os.pullEvent("mouse_click")
    if button == 1 and x >= 2 and y == 2 and x <= 21 then      --manuelles
	  commandesmanuelles()
	elseif button == 1 and x >= 2 and y == 4 and x <= 17 then  --opti
	  parallel.waitForAny(minageoptimise, controleClavier)
	elseif button == 1 and x >= 2 and y == 6 and x <= 8 then   --tunnel
	  parallel.waitForAny(tunnel, controleClavier)
	end
  end
end

init()
if nbturtle then
  mainmenu()
else
  term.clear()
  error("Code ereur : 404")
end