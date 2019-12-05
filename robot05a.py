#! /usr/bin/env python
# -*- coding: utf-8 -*-
#robot podstawowy wy�wietla w terminalu pozycj� aktualnego i atakowanego robota

import rg


class Robot:

    def act(self, game):
        print "dziala robot 05a\n"
        # je�eli jeste� w �rodku, bro� si�
        if self.location == rg.CENTER_POINT:
            print "guard"
            return ['guard']

        # je�eli wok� s� przeciwnicy, atakuj
        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) <= 1:
                    print "Atakuje05a", self.location, "=>", poz
                    return ['attack', poz]

        # id� do �rodka planszy
        print "move", self.location, "=>" , poz
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]