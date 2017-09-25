#!/usr/bin/env python

from graphviz import Digraph

           
conditions = {
            "incap": "Incapacitated",
            "paral": "Paralyzed",
            "uncon": "Unconcscious",
            "blind": "Blinded",
            "charm": "Charmed",
            "deaf": "Deafened",
            "fright": "Frightened",
            "grapp": "Grappled",
            "petri": "Petrified",
            "pois": "Poisoned",
            "petri": "Petrified",
            "prone": "Prone",
            "restr": "Restrained",
            "stun": "Stunned"
        }

effects = {
            "fail_dex": "Automatically fail dex saving throws",
            "fail_str": "Automatically fail str saving throws",
            "grant_adv": "Attacks have advantage",
            "melee_crit": "Melee attacks automatically crit",
            "attk_dis": "Has disadvantage on attacks",
            "no_act": "Can't take actions or reactions"
        }
 
 
edges = [
            ("paral", "incap"),
            ("uncon", "incap"),
            ("incap", "no_act"),
            ("paral", "fail_dex"),
            ("paral", "fail_str"),
            ("paral", "grant_adv"),
            ("paral", "melee_crit"),
            ("uncon", "fail_dex"),
            ("uncon", "fail_str"),
            ("uncon", "grant_adv"),
            ("uncon", "melee_crit"),
            ("blind", "grant_adv"),
            ("blind", "attk_dis"),
            ("fright", "attk_dis"),
            ("petri", "incap"),
            ("petri", "grant_adv"),
            ("petri", "fail_dex"),
            ("petri", "fail_str"),
            ("pois", "attk_dis"),
            ("prone", "attk_dis"),
            ("prone", "grant_adv"),
            ("restr", "grant_adv"),
            ("restr", "attk_dis"),
            ("restr", "dis_dex"),
            ("stun", "incap"),
            ("stun", "fail_dex"),
            ("stun", "fail_str"),
            ("stun", "grant_adv")
        ]

status_effects = Digraph(comment = "Status Effects")

for label in conditions:
    status_effects.node(label, conditions[label])

for label in effects:
    status_effects.node(label, effects[label], shape="box")

status_effects.edges(edges)

status_effects.render("graph-test.gv", view=True)
