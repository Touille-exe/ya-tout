function init(...)
  local mode = ...
  if mode == "local" then
    print("\n Local mode choisi")
	loc()
	return
  end
  rednet.open("left")
  print("\n 1 -- appairage automatique \n\n 2 -- appairage manuel" .. string.rep("\n", 7) .. " Entirement devloppe\n par Touille_exe")
  write(">> ")
  local choice = read()
  if choice == "1" then
    local id, msg = rednet.receive(30)
    if msg == "miaou" then
	  pcmaitre = id
	else
	  term.clear()
	  print(" Appairage automatique deffectueux.")
	  return
	end
  elseif choice == "2" then
    term.clear()
	term.setCursorPos(1,1)
	write("\n Quel est le numero du pc portable ?\n\n  pour le trouver :\n  mettre 'id' dans la console du pc" .. string.rep("\n", 9) .. ">> ")
	local choice = read()
	pcmaitre = tonumber(choice)
  else
    term.clear()
	print(" Choix invalide.")
	return
  end
end

function loc()
  print("non commence")
end

function main()
  term.clear()
  print("\n pas fini mais fonctionnel\n les commandes sonts atribuées au pc : " .. pcmaitre)
  boucle = true
  local id, cmd = rednet.receive()
  while boucle do
    if cmd == "forward" then      -- avancer
      local reponce
      	local ui, miaou = turtle.inspect()
      if miaou.name == "minecraft:lava" or miaou.name == "minecraft:water" then
      	  os.sleep(0.2)
      	  rednet.send(pcmaitre, "code1")
      	elseif miaou.name == "minecraft:gravel" or miaou.name == "minecraft:sand" then
      	  os.sleep(0.2)
      	  rednet.send(pcmaitre, "code2")
      	  local boucle = true
      	  while boucle do
      	    turtle.dig()
      		    local ui, miaou = turtle.inspect()
      		    if ui == false then
      		      boucle = false
      		    end
      	  end
      	else
      	  if turtle.forward() then
      	    local ui, reponse = turtle.inspect()
      	    if ui then
      	      reponce = "Bloc devant : " .. reponse.name
      	    else
      	      reponce = "Bloc indetectable"
      	    end
      	  else
      	    local ui, reponse = turtle.inspect()
      	    reponce = "Impossible d'avancer  " .. reponse.name .. " devant"
      	  end
      	  os.sleep(0.2)
      	  rednet.send(pcmaitre, reponce)
      	end
    elseif cmd == "dig" then       -- miner
      local ui, miaou = turtle.inspect()
      	if ui then
      	  if turtle.dig() then
      	    reponce = "Bloc mine : " .. miaou.name
      	  else
      	    reponce = "Bloc PAS mine : " .. miaou.name
      	  end
      	else
      	  if turtle.dig() then
      	    reponce = "Bloc mine"
      	  else
      	    reponce = "Bloc indetectable ou inexistant impossible a miner"
      	  end
      	end
      	os.sleep(0.2)
      	rednet.send(pcmaitre, reponce)
    elseif cmd == "digUp" then         -- miner vers le haut
      local ui, miaou = turtle.inspectUp()
      if ui then
        if turtle.digUp() then
          reponce = "Bloc mine : " .. miaou.name
        else
          reponce = "Bloc PAS mine : " .. miaou.name
        end
      else
        if turtle.digUp() then
          reponce = "Bloc mine"
        else
          reponce = "Bloc indetectable ou inexistant impossible a miner"
        end
      end
      os.sleep(0.2)
      rednet.send(pcmaitre, reponce)
    elseif cmd == "digDown" then       -- miner vers le bas
      local ui, miaou = turtle.inspectDown()
      if ui then
        if turtle.digDown() then
          reponce = "Bloc mine : " .. miaou.name
        else
          reponce = "Bloc PAS mine : " .. miaou.name
        end
      else
        if turtle.digDown() then
          reponce = "Bloc mine"
        else
          reponce = "Bloc indetectable ou inexistant impossible a miner"
        end
      end
      os.sleep(0.2)
      rednet.send(pcmaitre, reponce)
    elseif cmd == "left" then        -- tourner a gauche
      if turtle.turnLeft() then
        reponce = "Effectue"
      else
        reponce = "Impossible"
      end
      os.sleep(0.2)
      rednet.send(pcmaitre, reponce)
    elseif cmd == "right" then       -- tourner a droite
      if turtle.turnRight() then
        reponce = "Effectue"
      else
        reponce = "Impossible"
      end
      os.sleep(0.2)
      rednet.send(pcmaitre, reponce)
    elseif cmd == "back" then             -- reculer
      if turtle.back() then
        reponce = "Effectue"
      	else
      	  reponce = "Impossible"
      	end
      	os.sleep(0.2)
      	rednet.send(pcmaitre, reponce)
    elseif cmd == "up" then             -- monter
      if turtle.up() then
        reponce = "Effectue"
      	else
      	  reponce = "Impossible"
      	end
      	os.sleep(0.2)
      	rednet.send(pcmaitre, reponce)
    elseif cmd == "down" then              -- dessandre
      if turtle.down() then
      	  reponce = "Effectue"
      	else
      	  reponce = "Impossible"
      	end
      	os.sleep(0.2)
      	rednet.send(pcmaitre, reponce)
    elseif cmd == "check" then
      local ui1, miaou1 = turtle.inspect()
      	local ui2, miaou2 = turtle.inspectDown()
      	local ui3, miaou3 = turtle.inspectUp()
      	if ui1 then
      	  reponce = "  Devant : " .. miaou1.name
      	else
      	  reponce = "  Pas de bloc devant"
      	end
      	if ui2 then
      	  reponce = reponce .. "\n  En dessous : " .. miaou2.name
      	else
      	  reponce = reponce .. "\n  Pas de bloc en dessous"
      	end
      	if ui3 then
      	  reponce = reponce .. "\n  Au dessus : " .. miaou3.name
      	else
      	  reponce = reponce .. "\n  Pas de bloc au dessus"
      	end
      	os.sleep(0.2)
      	rednet.send(pcmaitre, reponce)
    elseif cmd == "" then
    end
  end
end

init()

if pcmaitre and rednet.isOpen() then
  main()
end