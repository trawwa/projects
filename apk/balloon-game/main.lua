background = display.newImage("background.png")
background.x = display.contentCenterX
background.y = display.contentCenterY

platform = display.newImage("platform.png", 0, 0)
platform.x = display.contentCenterX
platform.y = display.contentCenterY+250

balloon = display.newImage("balloon.png", 0, 0)
balloon.x = display.contentCenterX
balloon.y = display.contentCenterY

physics = require("physics")
physics.start()

physics.addBody(platform, "static")
physics.addBody(balloon, "dynamic")

function pushBalloon()
    balloon:applyLinearImpulse(0, -0.75, balloon.x, balloon.y)
end

background:addEventListener("tap", pushBalloon)
