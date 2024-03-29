#! /usr/bin/env python
# -*- coding: utf-8 -*-

#robot podstawowy, wy�wietla w terminalu pozycj� aktualnego i atakowanego robota do wersji robota wykorzystuj�cej pomocnicz� zmienn� ruch
import rg


class Robot:

    def act(self, game):

        # wszystkie pola
        wszystkie = {(x,y) for x in xrange(19) for y in xrange(19)}
        # punkty wejścia
        wejscia = {poz for poz in wszystkie if 'spawn' in rg.loc_types(poz)}
        # pola zablokowane
        zablokowane = {poz for poz in wszystkie if 'obstacle' in rg.loc_types(poz)}
        przyjaciele = {poz for poz in game.robots if game.robots[poz].player_id == self.player_id}
        # pola zajęte przez wrogów
        wrogowie = set(game.robots) - przyjaciele
        # pola sąsiednie
        sasiednie = set(rg.locs_around(self.location)) - zablokowane
        # pola sąsiednie zajęte przez wrogów
        wrogowie_obok = sasiednie & wrogowie
        wrogowie_obok2 = { poz for poz in sasiednie if (set(rg.locs_around(poz)) & wrogowie)} - przyjaciele
        # pola bezpieczne
        bezpieczne = sasiednie -wrogowie_obok -wejscia - przyjaciele

        # działania domyslne:
        ruch = ['move', rg.toward(self.location, rg.CENTER_POINT)]
        # jeżeli jeteś wpkt wejścia opuść go
        if self.location in wejscia:
            ruch = ['move', rg.toward(self.location, rg.CENTER_POINT)]
        # jeżeli jesteś w środku broń się
        if self.location == rg.CENTER_POINT:
            ruch = ['guard']

        # jeżeli obok są przeciwnicy, atakuj o ile to bezpieczne
        if wrogowie_obok:
            if 9*len(wrogowie_obok) >= self.hp:
                if bezpieczne:
                    ruch ['move',bezpieczne.pop()]
            else:
                ruch = ['attack', wrogowie_obok.pop()]

        if wrogowie_obok2:
            ruch = ['attack', wrogowie_obok2.pop()]

        return ruch