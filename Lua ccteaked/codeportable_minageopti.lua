function minageoptimisé()
  coteduminage = "left"
  while true do
    for i = 1, 50 do
      rednet.send(nbturtle, "dig")
      rednet.send(nbturtle, "forward")
      retourturtle()
      rednet.send(nbturtle, "digUp")
      os.sleep(0.2) -- tempo pour pas saturer
    end
    if coteduminage == "left" then
      rednet.send(nbturtle, "left")
    elseif coteduminage == "right" then
      rednet.send(nbturtle, "right")
    end
    for i = 1, 3 do
      rednet.send(nbturtle, "dig")
      rednet.send(nbturtle, "forward")
      retourturtle()
      rednet.send(nbturtle, "digUp")
      os.sleep(0.2)
    end
    if coteduminage == "left" then
      rednet.send(nbturtle, "left")
      coteduminage = "right"
    elseif coteduminage == "right" then
      rednet.send(nbturtle, "right")
      coteduminage = "left"
    end
  end
end

function controleClavier()
  while true do
    local event, key = os.pullEvent("key")
    if keys.getName(key) == "q" then
      print("Arrêt demandé par l’utilisateur")
      return  -- cette fonction se termine → le parallel s’arrête
    end
  end
end

parallel.waitForAny(minage, controleClavier)





function retourturtle()
  local id, msg = rednet.receive(1)
  if id == nbturtle and msg = true then
    -- alerte retour de la turtle
  else
    -- alerte pas de reponses
  end
end

  



function tunnel()
  for i = 1, longeurtunnel do
    rednet.send(nbturtle, "dig")
    rednet.send(nbturtle, "forward")
    retourturtle()
    rednet.send(nbturtle, "digUp")
  end
end

parallel.waitForAny(minage, controleClavier)








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

parallel.waitForAny(escalier, controleClavier)