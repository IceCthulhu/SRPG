#RPG del espacio - humanos vs aliens - arma pistolas
from time import *
from random import *


class Seres():
   def  __init__(self,nombre,salud,ataque,xp=0):
       self.name=nombre #"cadena"
       self.vida=salud #número entero
       self.atq=ataque #número entero
       self.xp=xp
class Humano(Seres):
   def atacar(self, alien):
       dmg=randint(self.atq-5,self.atq)
       crit=randint(1,10)
       if crit==5:
           dmg=dmg*2
       print(self.name+" ataca🤺 a "+alien.name,"le hace",dmg,"de daño💔")
       sleep(1.2)
       alien.vida -= dmg
       if alien.vida<=0:
           alien.vida=0
       print("...al "+alien.name+"🦂 le quedan ", alien.vida ,"de vida")
       sleep(0.8)
   def combate(self,PC):
       while self.vida>0 and PC.vida>0:
           self.atacar(PC)
           if PC.vida<=0:
               PC.vida=0
               print(PC.name,"ha perdido la batalla\n")
               break
           PC.atacar(self)
           if self.vida<=0:
               self.vida=0
               print(self.name,"ha perdido la batalla")
               break


class Alien(Seres):
   def SHOW(self):
       shuffle(texto)
       print(texto[0])
       sleep(3)
       print("resulta ser un alien de",str(self.vida)+"❤️.... se enfrentan a él")
       sleep(1)
   def atacar(self, hum):
        dmg=randint(3,self.atq)
        print(self.name+"👽 ataca a "+hum.name,"le hace",dmg,"de daño 💔")
        hum.vida -= dmg
        if hum.vida<=0:
            hum.vida=0
        sleep(1.5)
        print("Te quedan ", hum.vida ,"de vida❤️‍🩹")
        sleep(0.6)
#historia
texto=["El aire se volvía denso y opresivo a medida que avanzabas por los pasillos oscuros de la estación espacial abandonada."," La luz titilante de los paneles dañados parpadeaba intermitentemente, arrojando sombras que se retorcían y contorsionaban en las paredes como espectros danzantes.","De repente, un sonido sutil pero inconfundible se filtró en la penumbra: un susurro alienígena, un siseo letal que helaba la sangre.",
       "Aprietas con fuerza la empuñadura de su arma, sintiendo la vibración inminente de la batalla. ","Diez pares de ojos negros y relucientes se asomaban desde las sombras, revelando la presencia de los Xenomorfos, criaturas pesadillescas que acechaban en la oscuridad.","Los colmillos afilados de los Xenomorfos destellaron a la luz intermitente, reflejando una malevolencia innata.",
       "Te preparas para el enfrentamiento, su corazón latiendo con la cadencia de la anticipación y la supervivencia. Las criaturas se movían con una gracia siniestra, serpenteando entre las estructuras deterioradas con una agilidad mortal.","Oh no…","Una silueta negra sin forma a lo lejos…"]
#los aliens
nave=[]
for x in range(20):#N° de aliens
   PC1 = Alien("Xenomorfo", randint(20,40), randint(5,15))
   nave.append(PC1)  
#Historia1:
print("Bienvenido al espacio💪🗿⚜️")
nombre=input("Ingresa tu nombre:")
print("En un rincón lejano del universo, la humanidad se encuentra en una lucha desesperada contra una raza de alienígenas hostiles.")
sleep(3.5)
print("Eres el Capitán ",nombre,", el comandante de la nave espacial 'Esperanza'. Tu misión es liderar a tu tripulación y defender la Tierra contra la invasión alienígena.")
sleep(4)
print("Capitán ",nombre,", la esperanza de la humanidad descansa en tus manos. ¡Prepárate para la batalla!\n")
sleep(2.5)
#creando un humano:}
J1=Humano(nombre,99,15)
for alien in nave:
    extravid=randint(1,10)
    exp=randint(3, 10)
    alien.SHOW()
    J1.combate(alien)
    if J1.vida<=0:
       J1.vida=0
       break
    elif J1.xp>=64:
        print("🎆Subiste de nivel🔆")
        sleep(1.5)
        print("Recuperas 20⚕️ de vida❤️")
        J1.vida+=20
        sleep(0.4)
        print("Ahora eres más fuerte🎢🗡️")
        J1.atq+=2
        sleep(0.4)
        J1.xp-=64

    else:
        print("Ganaste",exp,"🔅 de experiencia")
        J1.xp+=exp
        sleep(0.4)
        print(J1.name,"recupera",extravid,"⚕️ de vida\n")
        J1.vida+=extravid
        sleep(0.4)
    print("⚜️ /////////////////⚜️\n")
if J1.vida<=0:
    print("GAME OVER")
else:
    print("Lo lograste!🎆🎉, venciste a los aliens👽👾")
    sleep(3)
    print("Cuenta final",J1.name,J1.vida,"❤️")


