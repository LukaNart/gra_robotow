#! /usr/bin/env python
# -*- coding: utf-8 -*-
#robot podstawowy

import rg


class Robot:

    def act(self, game):
        # je¿eli jesteœ w œrodku, broñ siê
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # je¿eli wokó³ s¹ przeciwnicy, atakuj
        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) <= 1:
                    return ['attack', poz]

        # idŸ do œrodka planszy
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]