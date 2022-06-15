# inheritance.py
# Name:
# Collaborators: 

class Spell():
    def __init__(self,  incantation,  name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'


def study_spell(spell):
    print(spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
