#!/usr/bin/env python2

import javarandom
import math
import sys

class GalacticraftDung:
    def __init__(self, Seed, Spacing = 704):
        self.Seed = Seed
        self.Spacing = Spacing
        self.nearestDistance = 0x7fefffffffffffff # java double.max_value

    def getDungeonPosForCoords(self, chunkX, chunkZ, Dimension):
        numChunks = self.Spacing / 16
        chunkX = int(chunkX)
        chunkZ = int(chunkZ)

        if chunkX < 0:
            chunkX -= numChunks - 1

        if chunkZ < 0:
            chunkZ -= numChunks - 1

        k = chunkX / numChunks
        l = chunkZ / numChunks

        seed = (k * 341873128712) + (l * 132897987541) + self.Seed + (10387340 + Dimension)

        random = javarandom.Random()
        random.setSeed(seed)

        k = (k * numChunks) + random.nextInt(numChunks)
        l = (l * numChunks) + random.nextInt(numChunks)

        return k, l

    def directionToNearestDungeon(self, xpos, zpos, Dimention):
        x = math.floor(xpos)
        z = math.floor(zpos)
        quadrantX = x % self.Spacing;
        quadrantZ = z % self.Spacing;
        searchOffsetX = int(quadrantX / (self.Spacing / 2))  # 0 or 1
        searchOffsetZ = int(quadrantZ / (self.Spacing / 2))  # 0 or 1
        nearestX = 0
        nearestZ = 0
        for cx in range(searchOffsetX - 1, searchOffsetX + 1):
            for cz in range(searchOffsetZ - 1, searchOffsetZ + 1):
                k, l = self.getDungeonPosForCoords((x + cx * self.Spacing) / 16, (z + cz * self.Spacing) / 16, Dimention)
#                print("k: {}, l: {}".format(k, l))
                i = 2 + k
                j = 2 + l
                oX = i - xpos
                oZ = j - zpos
                distanceSq = oX * oX + oZ * oZ
                if distanceSq < self.nearestDistance:
                    return distanceSq, -oX, -oZ

g = GalacticraftDung(-1400251488)

print("Location: 1327, -544")
d,x,z = g.directionToNearestDungeon(1327, -544, -12)
print("X: {}, Z: {}, D: {}".format(x, z, d))
print("dat file shows (Chunk): [78,-31], which is: 1248, -496")

#print("Location: 1428, -639")
#d,x,z = g.directionToNearestDungeon(1428, -639, -14)
#print("X: {}, Z: {}, D: {}".format(x, z, d))
#print("Should be close to: 1249, -492")

