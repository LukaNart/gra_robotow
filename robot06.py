#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

class Robot:

    def act(self, game):

        def czy_wejscie(poz):
            if 'spawn' in rg.loc_types(poz):
                return True
            return False

        def czy_wrog(poz):
            if game.robots.get(poz) != None:
                if game.robots[poz].player_id != self.player_id:
                    return True
            return False
        def czy_atak():
            if 9*len(wrogowie_obok) < self.hp:
                return True
            return False
        def czy_puste(poz):
            if ('normal' in rg.loc_types(poz)) and not ('obstacle' in rg.loc_types(poz)):
                if game.robots.get(poz) == None:
                    return True
            return False
        
        puste = [] # lista pustych p�l obok
        bezpieczne = [] # lista bezpiecznych p�l obok
        for poz in rg.locs_around(self.location):
            if czy_puste(poz):
                puste.append(poz)
            if czy_puste(poz) and not czy_wejscie(poz):
                bezpieczne.append(poz)
        
        # funkcja zwr�ci prawd�, je�eli w odleg�o�ci 2 krok�w z przodu jest wr�g
        def zprzodu(l1, l2):
            if rg.wdist(l1, l2) == 2:
                if abs(l1[0] - l2[0]) == 1:
                    return False
                else:
                    return True
            return False
        
        # funkcja zwr�ci wsp�rz�dne pola �rodkowego mi�dzy dwoma innymi
        # oddalonymi o 2 kroki
        def miedzypole(p1, p2):
            return (int((p1[0]+p2[0]) / 2), int((p1[1]+p2[1]) / 2))

    
        # lista wrog�w obok
        wrogowie_obok = []
        for poz in rg.locs_around(self.location):
            if czy_wrog(poz):
                wrogowie_obok.append(poz)
        
        # je�eli jeste� w punkcie wej�cia, opu�� go
        if czy_wejscie(self.location):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        # je�eli obok s� przeciwnicy, atakuj, o ile to bezpieczne
        if len(wrogowie_obok):
            if czy_atak():
                return ['attack', wrogowie_obok.pop()]
            elif bezpieczne:
                return ['move', bezpieczne.pop()]
        
        # je�eli wr�g jest o dwa kroki, atakuj
        for poz, robot in game.get('robots').items():
            if czy_wrog(poz) and rg.wdist(poz, self.location) == 2:
                if zprzodu(poz, self.location):
                    return ['attack', miedzypole(poz, self.location)]
                if rg.wdist(rg.toward(poz, rg.CENTER_POINT), self.location) == 1:
                    return ['attack', rg.toward(poz, rg.CENTER_POINT)]
                else:
                    return ['attack', (self.location[0], poz[1])]

        # je�eli jeste� w �rodku, bro� si�
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # id� do �rodka planszy
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]