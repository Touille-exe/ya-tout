-- test des pixels sur l'écran du portable  x = --> et y = ↓  26 par 20 pour le portable
x, y = term.getSize()
print(x, y)

-- on dessine un bouton
function drawButton(x, y, w, h, text, color)
    paintutils.drawFilledBox(x, y, x + w, y + h, color)
    term.setCursorPos(x + 1, y + math.floor(h/2))
    term.setTextColor(colors.white)
    term.write(text)
end

-- on affiche un bouton vert
drawButton(5, 5, 10, 3, "Avancer", colors.green)

function miaou()
  while true do
      local event, button, x, y = os.pullEvent("mouse_click")
      -- si clic gauche (button == 1) et dans la zone du bouton
      if button == 1 and x >= 5 and x <= 15 and y >= 5 and y <= 8 then
          print("Bouton AVANCER cliqué")
          -- ici tu pourrais envoyer la commande à la turtle
    end
  end
end