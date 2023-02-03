xCenter = display.contentCenterX



button1 = display.newImage("button.png", xCenter, 0)
button2 = display.newImage("button.png", xCenter, 140)
button3 = display.newImage("button.png", xCenter, 280)
button4 = display.newImage("button.png", xCenter, 420)

button1sound = audio.loadSound("si.mp3")
button2sound = audio.loadSound("ci.wav")
button3sound = audio.loadSound("do.wav")
button4sound = audio.loadSound("fe.wav")

function but1()
    audio.play(button1sound)
end

function but2()
    audio.play(button2sound)
end

function but3()
    audio.play(button3sound)
end

function but4()
    audio.play(button4sound)
end

button1:addEventListener("tap", but1)
button2:addEventListener("tap", but2)
button3:addEventListener("tap", but3)
button4:addEventListener("tap", but4)
