# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:39:30 2022

@author: Enes
"""
# GEN HAVUZUNU DOĞRU OLUŞTURMAK ÇOK ÖNEMLİ
#MUTASYONU DOĞRU KURMAK ÇOK ÖNEMLİ MUTASYON OLMAZSA SONUCA ULAŞAMAYIZ.

import random 


class Genetic:
    def __init__(self, Target, Population_Number):
        self.Gene_Pool = '''abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHİIJKLMNOÖPQRŞSTUÜVWXYZ 1234567890,.-;:_!"#%&/()=?@${[]}'''
        self.Target = Target
        self.Population_Number = Population_Number          #popülasyon genişliği(birey sayısı).
        self.Target_Text_Lenght = len(Target)               #dışarıdan gelen text uzunluğu.
        self.Population = []
        self.Next_Generation = []                           #çiftleşme yaparken işimize yarayacak.
        self.Found = False                                  #hedefe ulaşınca False durumu True olacak.
        self.Generation_Timer = 0                           #kaç jenerasyon ilerlediğimizi gösterecek.
        
        
    class Member:                                           #bireylerimizi tanımlayacağımız sınıfımızı oluşturduk.
        def __init__(self, chromosome):                     #üyemizin kromozomu olacak ve dna bilgilerini taşıyacak.
            self. Chromosome = chromosome                   #Gene_Pool dan gen çekip bu genleri birleştirip kromozom oluşturacağız.
            self.Fitness = 0                                #sağlık durumu. Başlangıç olarak 0.
            
    def random_gene(self):                                  #sadece 1 gen almamıza yarayan fonksiyon.
        Gene = random.choice(self.Gene_Pool)                #gen havuzundan rastgele bir şey seçecek.
        return Gene          
    
    def create_chromosome(self):   #random_gene i belirli sayıda çalıştırıp bunun içinde kromozom üreteceğiz ve listeye ekleyeceğiz.
        chromosome = [self.random_gene() for i in range(self.Target_Text_Lenght)]
        return chromosome
    
    def calculate_fitness(self):         #tüm bireylerin sağlık durumunu hesaplarız.
        for Member in self.Population:
            Member.Fitness = 0                              #önceki nesilden gelmiş olabilir. Fitness a yapılacak eklemeler belli bi sayıdan değil 0 dan başlasın.
            for i in range(self.Target_Text_Lenght):         #kromozomla targeti karşılştırmamız gerekiyor. o yüzden target uzunluğu kadar döner.
                if Member.Chromosome[i] == self.Target[i]:   #eğer kromozomla hedefin belirli indexleri aynı değerdeyse, yakınlık durumumuz artar.
                    Member.Fitness += 1
            
            if Member.Fitness == self.Target_Text_Lenght:  #fitness = hedef uzunlugu ise her eleman aynıdır hedefe ulasılmıstır.
                self.Found_Text = Member.Chromosome
                self.Found = True                          #bulduğumuz text hedef text olmuş ve döngüyü bitirmiştir.
 
    
    def crossover(self):
        last_best = int((90 * self.Population_Number) / 100 ) #listedeki son 10 eleman en iyi %10 u olmuş oluyor. Bu yüzden 90 la çarptık.
        self.Next_Generation = []
        self.Next_Generation.extend(self.Population[last_best:]) #burada Populationdaki en iyi %10u Next_Generation'a geçirdik.
        
        while True:
            #eğer next_generation uzunluğu populasyondan kucukse burda çiftleştir ve çocuğu ekle
            if len(self.Next_Generation) < self.Population_Number:
                member_1 = random.choice(self.Population[last_best:]).Chromosome  #populasyonun en ıyılerınden bır tane sec ve Chromosomunu ekle Member_1a.
                member_2 = random.choice(self.Population[last_best:]).Chromosome
                new_member = []
                
                for gene1,gene2 in zip(member_1, member_2): #zip ile member_1in indisini gene_1e member_2nin indisini gene_2 ye aynı anda döndürüyo. 
                    prob = random.random()  #olasılık belirledik. Bu 0-1 arasında bir değer verecek bize.
                    if prob < 0.47:
                        new_member.append(gene1)
                    elif prob < 0.94:
                        new_member.append(gene2)
                    else: #geri kalan %6 lık şansta ise mutasyona uğratacağız.
                        new_member.append(self.random_gene())
                
                self.Next_Generation.append(self.Member(new_member)) #burada yeni üyemizin kromozomunu taşıyan üye ekledik.        
                
            else: #next_generation uzunlugu populasyondan kucuk değilse donguyu sonlandır.
                break
        
        self.Population = self.Next_Generation    
    
    def main(self):     #Başlangıç popülasyonu yarattık.
        for i in range(self.Population_Number):            #kromozom oluşturup sonra üye oluşturacağız ve sonra üyeyi popülasyona ekleyeceğiz.
            self.Population.append(self.Member(self.create_chromosome()))
            
        while not self.Found:   #Found False den True ye dönene kadar döngü dönecek.
            self.calculate_fitness()
            #fitness değerlerine göre dizimizi sıraladık. Member'ın fitnessına göre sıraladık.
            #bu sayede listede fitness değeri en yüksek olanları sıraladık.
            self.Population = sorted(self.Population, key=lambda Member: Member.Fitness) 
            self.crossover()   # crossover fonksiyonunu çalıştırdık.
            self.Generation_Timer += 1
            
        print(f"You found = {self.Found_Text}, you did it {self.Generation_Timer} steps."
              f"\n Your Target = {self.Target}")  
            
            
            
            
        
Target = "Mustafa Kemal Atatürk"
Population_Number = 1000   #populasyon numarasını artırırsak adım sayısını azaltırız.

Go = Genetic(Target, Population_Number)       #nesne oluşturduk.
Go.main()