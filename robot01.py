#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

class Robot:
    def act(self,game):
        #id� do �rodka planszy, ruch domy�lny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        # je�eli jeste� w �rodku, bro� si�
        if self.location == rg.CENTER_POINT:
            return ['guard']
            LUB
            # je�eli jeste� w �rodku, pope�nij samob�jstwo
            if self.location == rg.CENTER_POINT:
                return ['suicide']
            # je�eli obok s� przeciwnicy, atakuj
            # wersja z p�tl� przegl�daj�c� wszystkie pola zaj�te przez roboty
            for poz, robot in game.robots.iteritems():
                if robot.player_id != self.player_id:
                    if rg.dist(poz, self.location) <= 1:
                        return ['attack', poz]
						