#! /usr/bin/env python
# -*- coding: utf-8 -*-

#robot podstawowy, wy�wietla w terminalu pozycj� aktualnego i atakowanego robota do wersji robota wykorzystuj�cej pomocnicz� zmienn� ruch
import rg


class Robot:

    def act(self, game):
        # dzia�anie domy�lne:
        print "dziala robot 05b\n"
        ruch = ['move', rg.toward(self.location, rg.CENTER_POINT)]

        if self.location == rg.CENTER_POINT:
            ruch = ['guard']

        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) <= 1:
                    print "Atakuje05b", self.location, "=>", poz
                    ruch = ['attack', poz]
                    #print ruch[0], self.location, "=>",
                    #if (len(ruch) > 1):
                        #print ruch[1]
                    #else:
                        #print
        print ruch[0], self.location, "=>",
        if (len(ruch) > 1):
            print ruch[1]
        else:
            print
        return ruch