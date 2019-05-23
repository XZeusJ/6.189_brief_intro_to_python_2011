#coding=utf-8
#Zhangjin Xiao

#4.5
class Spell:
	def __init__(self, incantation, name):
		self.name = name
		self.incantation = incantation
	def __str__(self):
		return self.name + ' ' + self.incantation + '\n' + self.get_description()
	def get_description(self):
		return 'No description'
	def execute(self):
		print self.incantation
class Accio(Spell):
	def __init__(self):
		Spell.__init__(self, 'Accio', 'Summoning Charm')
	def get_description(self):
		return 'fuck you'
class Confundo(Spell):
	def __init__(self):
		Spell.__init__(self, 'Confundo', 'Confundus Charm')
	def get_description(self):
		return 'Causes the victim to become confused and befuddled.'
def study_spell(spell):
	print spell
spell = Accio()
print 1
spell.execute()
print 2
study_spell(spell)
print 3
study_spell(Confundo())
print 4
print spell

#4.6
class Address:
	def __init__(self, street, num):
		self.street_name = street
		self.number = num

class CampusAddress(Address):
	def __init__(self, office_number):
		Address.__init__(self, 'Massachusetts Ave', 77 )
		self.office_number = office_number

Sarina_addr = CampusAddress("32-G904")
print Sarina_addr.office_number
print Sarina_addr.street_name
print Sarina_addr.number