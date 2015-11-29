from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

x, y, z = mc.player.getPos()

tnt = 46
mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, tnt, 1)
