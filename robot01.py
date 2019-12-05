#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

class Robot:
    def act(self,game):
        #id« do ˜rodka planszy, ruch domy˜lny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        # je¿eli jesteœ w œrodku, broñ siê
        if self.location == rg.CENTER_POINT:
            return ['guard']
            LUB
            # je¿eli jesteœ w œrodku, pope³nij samobójstwo
            if self.location == rg.CENTER_POINT:
                return ['suicide']
            # je¿eli obok s¹ przeciwnicy, atakuj
            # wersja z pêtl¹ przegl¹daj¹c¹ wszystkie pola zajête przez roboty
            for poz, robot in game.robots.iteritems():
                if robot.player_id != self.player_id:
                    if rg.dist(poz, self.location) <= 1:
                        return ['attack', poz]
						